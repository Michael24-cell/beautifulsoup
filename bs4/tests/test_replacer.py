from bs4 import BeautifulSoup, SoupReplacer

def test_replace_ogtag_with_alttag():
    replacer = SoupReplacer("em", "b")
    soup = BeautifulSoup("<em>Hello</em>", "html.parser", replacer=replacer)

    assert str(soup) == "<b>Hello</b>"

def test_id_and_text_survive_after_replacer():
    replacer = SoupReplacer("section", "div")
    html = '<section id="x">This is an example sentence.</section><p>testing</p>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == '<div id="x">This is an example sentence.</div><p>testing</p>'