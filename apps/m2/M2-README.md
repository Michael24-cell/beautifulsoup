Milestone 2

Part 2

These are the BeautifulSoup APIs I used in Milestone 1 tasks 1-8 and Milestone 2 Part 1 tasks 2, 3, and 4. The line numbers are from the original source before any library changes. Repeated APIs are listed once.

BeautifulSoup constructor - bs4/__init__.py, line 209

prettify() - bs4/element.py, line 2601

find_all() - bs4/element.py, line 2715

get() - bs4/element.py, line 2160

get_text() - bs4/element.py, line 524

find_parent() - bs4/element.py, line 992

new_tag() - bs4/__init__.py, line 682

has_attr() - bs4/element.py, line 2196

replace_with() - bs4/element.py, line 552

SoupStrainer constructor - bs4/filter.py, line 345

tag["alt"] - bs4/element.py, line 2203

tag["class"] assignment - bs4/element.py, line 2223

paragraph.string assignment - bs4/element.py, line 1861

tag.name - bs4/element.py, line 1648 (attribute initialization)

tag.attrs - bs4/element.py, lines 1674-1689 (attribute initialization)

Part 3

I added SoupReplacer in bs4/replacer.py. It takes an original tag name and a replacement tag name. I updated BeautifulSoup to accept it through the optional replacer argument.

I updated popTag so that after an element is removed from the stack of open tags, its name is changed if it matches the replacement rule. The element stays in the document tree. This happens during parsing, so no additional search through the completed tree is needed.

test_replace_ogtag_with_alttag checks that an em tag is replaced with a b tag while keeping its text.

test_id_and_text_survive_after_replacer replaces a section with a div. The section has an ID and text, followed by a separate p element. It checks that the ID and text survive the replacement and that the p element stays outside the div.

Both tests passed. The full test suite finished with 622 passed and 216 skipped.

Run the tests from the beautifulsoup folder:

python -m pytest bs4/tests

task6.py uses SoupReplacer to change b tags to blockquote tags and writes the prettified result to a file ending in .blockquote.
