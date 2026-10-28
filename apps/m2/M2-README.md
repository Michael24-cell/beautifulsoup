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

I added SoupReplacer in bs4/replacer.py. It takes an original tag name and a replacement tag name. BeautifulSoup accepts this object through the optional replacer argument.

I updated popTag to change the tag’s name after removing it from the stack of open tags. The tag stays in the document tree. This happens during parsing, so we do not need to search the completed tree again.

test_replace_ogtag_with_alttag checks that an em tag changes to a b tag and keeps its text.

test_id_and_text_survive_after_replacer checks that a section changes to a div while keeping its ID and text. It also checks that the p element after it stays outside the div.

Both tests passed. The full test suite had 622 passed and 216 skipped.

To run the tests from the beautifulsoup folder:

python -m pytest bs4/tests

task6.py uses SoupReplacer to change b tags to blockquote tags. It saves the prettified result to a new file ending in .blockquote.