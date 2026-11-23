from bs4 import BeautifulSoup, Comment

# check that the loop reaches nested tags and text
def test_loop_visits_nested_nodes():
    soup = BeautifulSoup("<div><p>text</p></div>", "html.parser")

    count = 0
    for node in soup:
        count += 1

    assert count == 3

# check that loop collects all nested strings
def test_loop_returns_all_nested_text():
    soup = BeautifulSoup("<div>Instructions <p>correct text</p></div>", "html.parser")

    text = ''
    for node in soup:
        if isinstance(node, str):
            text += node

    assert text == 'Instructions correct text'

# check that empty soup counts 0 nodes
def test_loop_returns_if_empty():
    soup = BeautifulSoup("", "html.parser")

    count = 0
    for node in soup:
        count += 1

    assert count == 0

# check that the loop continues after an empty tag
def test_loop_continues_after_empty_tag():
    soup = BeautifulSoup("<div><p></p><p>text</p></div>", "html.parser")

    count = 0
    text = ""
    for node in soup:
        count += 1
        if isinstance(node, str):
            text += node

    assert count == 4
    assert text == "text"

# check that the loop visits nested comment objects
def test_loop_visits_comments():
    soup = BeautifulSoup("<div><!--a comment--><p>text</p></div>", "html.parser")

    count = 0
    for node in soup:
        if isinstance(node, Comment):
            assert str(node) == "a comment"
            count += 1

    assert count == 1
