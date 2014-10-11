-- This program takes a (formatted) query as a command line agument and returns a list of (formatted) lines that match the query
import System.Environment
import Text.JSON.Generic (toJSON)
import Text.CSV (parseCSV)
import Data.List (isInfixOf)
import qualified Data.Map.Lazy as M
import qualified Data.Text as T

main = do
    -- args <- getArgs
    -- let query = read $ head args :: [(String, String)]
    -- print query
    
    contents <- readFile "BIGBOOK.csv"
    
    let (ts:ls) = lines contents
    let titles = getTitles $ parseCSV "BIGBOOK.csv" ts
    let eithErrCsv = map (parseCSV "BIGBOOK.csv") ls
    
    let tupleLines = map lineToTuple eithErrCsv
    let listLines  = map lineToList  eithErrCsv
    
    let tree  = M.fromAscList tupleLines
    let index = indicise titles listLines
    
    
    
    -- return $ M.lookup 197000000002 tree
    -- print $ M.lookup "iyear" index
    return titles
    -- return index


getTitles x = case x of
    Left err -> []
    Right [cs] -> cs :: [String]

-- toCSV :: Either ParseError CSV -> [(Integer,[String])]
lineToTuple x = case x of
    Left err -> (0, ["ERROR"])
    Right [cs] -> (read $ head cs, cs) :: (Integer, [String])

lineToList x = case x of
    Left  err  -> []
    Right [cs] -> cs :: [String] -- :: [T.Text]


-- For both indexing functions the commented types are simplified;
-- the lists actually are M.Maps

-- Titles -> All entries -> [(title, [(word,[line IDs])])]
indicise :: [String] -> [[String]] -> M.Map String (M.Map String [Integer])
indicise titles entries = foldr step M.empty entries
    where step :: [String] -> M.Map String (M.Map String [Integer]) -> M.Map String (M.Map String [Integer])
          step entry acc = M.unionWith (M.unionWith (++)) acc newStuff
            where newStuff :: M.Map String (M.Map String [Integer])
                  newStuff = M.fromList $ zip titles (subIndicise entry)

-- Entry -> [(word, [line IDs])]
subIndicise :: [String] -> [M.Map String [Integer]]
subIndicise entry = foldr step [] entry
    where eID = read $ head entry :: Integer
          step :: String -> [M.Map String [Integer]] -> [M.Map String [Integer]]
          step field acc = newWords:acc
            where newWords :: M.Map String [Integer]
                  newWords = M.fromList $ zip (words field) (repeat [eID])






