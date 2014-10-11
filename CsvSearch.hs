-- This program takes a (formatted) query as a command line agument and returns a list of (formatted) lines that match the query
import System.Environment
import Text.JSON.Generic (toJSON)
import Text.CSV (parseCSV)
import Data.List (isInfixOf)

main = do
    args <- getArgs
    let query = read $ head args :: [(String, String)]
    -- print query
    contents <- readFile "BIGBOOK.csv"
    let (ts:ls) = lines contents
    let titles = head . toNice $ parseCSV "BIGBOOK.csv" ts
    let eithErrCsv = map (parseCSV "BIGBOOK.csv") ls
    let lazyLines = map toNice eithErrCsv
    
    -- return . toJSON $ search titles query lazyLines
    print . toJSON . take 2 $ search titles query lazyLines
    -- return . toJSON $ search titles [("Data", "Kokang")] lazyLines
    -- print . take 2 $ lazyLines
    -- print . take 2 $ search titles query lazyLines
    -- return $ take 2 lazyLines
    -- return $ toJSON titles

-- toCSV :: Either ParseError CSV -> [[String]]
toNice x = case x of
    Left  err  -> []
    Right cs -> cs :: [[String]]

search :: [String] -> [(String, String)] -> [[[String]]] -> [[String]]
search titles keyWords doc = foldr step [] doc
    where step :: [[String]] -> [[String]] -> [[String]]
          step entry acc = case matches titles keyWords entry of
                    True  -> (head entry):acc
                    False -> acc

matches ts kw entr = foldr step False $ zip ts (head entr)
    where step (t,e) acc = case lookup t kw of
            Just value -> if value `isInfixOf` e
                            then True
                            else acc
            Nothing    ->        acc
