import wikipedia
import re

def all_text(inp):
    current_page = wikipedia.page(wikipedia.search(inp))# search finds what it thinks is most relivent not the exact right match
    section_heads = re.findall("== (.*) ==", current_page.content)
    output = {}
    for head in section_heads:
        output[head]= current_page.section(head)
    return output

