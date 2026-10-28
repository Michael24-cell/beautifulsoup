import sys
from bs4 import BeautifulSoup, SoupStrainer

# check that a file path was supplied
if len(sys.argv) < 2:
    sys.exit("No input file supplied. Usage: python3 task4.py <path-to-input-file>")

file_path = sys.argv[1]

# read the file into text, stop if it can't be opened or read as UTF-8
try:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
except OSError:
    sys.exit("Could not open or read input file:" + file_path)
except UnicodeDecodeError:
    sys.exit("Input file could not be read as UTF-8: " + file_path)

# choose the parser from the file ending, stop if neither matches
if file_path.endswith(".xml"):
    parser = "xml"
elif file_path.endswith(".html"):
    parser = "html.parser"
else:
    sys.exit("Please supply an HTML or XML file.")

# select tags with an id and their contents while building the tree
only_tags_with_id = SoupStrainer(id=True)
soup = BeautifulSoup(text, parser, parse_only=only_tags_with_id)

for tag in soup.find_all(id=True):
    print(tag)

