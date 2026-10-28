import sys
from bs4 import BeautifulSoup, SoupReplacer

# check that a file path was supplied
if len(sys.argv) < 2:
    sys.exit("No input file supplied. Usage: python3 task6.py <path-to-input-file>")

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


b_to_blockquote = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(text, parser, replacer=b_to_blockquote)

try:
    with open(file_path + ".blockquote", "w", encoding="utf-8") as output_file:
        output_file.write(soup.prettify())
except OSError:
    sys.exit("Could not write output file: " + file_path + ".blockquote")

