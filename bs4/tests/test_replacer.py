from bs4 import BeautifulSoup, SoupReplacer

# check that the original tag pair interface still works
def test_replace_ogtag_with_alttag():
    replacer = SoupReplacer("em", "b")
    soup = BeautifulSoup("<em>Hello</em>", "html.parser", replacer=replacer)

    assert str(soup) == "<b>Hello</b>"

# check that renaming keeps the id, text, and following p element
def test_id_and_text_survive_after_replacer():
    replacer = SoupReplacer("section", "div")
    html = '<section id="x">This is an example sentence.</section><p>testing</p>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == '<div id="x">This is an example sentence.</div><p>testing</p>'

# check that the name function changes em tags and leaves p tags alone
def test_name_xformer_changes_only_em_tags():
    def change_name(tag):
        if tag.name == "em":
            return "b"
        return tag.name

    replacer = SoupReplacer(name_xformer=change_name)
    html = "<em>Hello</em><p>Keep this</p>"
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == "<b>Hello</b><p>Keep this</p>"

# check that the name function changes only matching tags
def test_name_xformer_changes_only_em_tags():
    def change_name(tag):
        if tag.name == "em":
            return "b"
        return tag.name

    replacer = SoupReplacer(name_xformer=change_name)
    html = "<em>Hello</em><p>Keep this</p>"
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == "<b>Hello</b><p>Keep this</p>"


# check that nested tags are both renamed and stay nested
def test_name_xformer_handles_nested_tags():
    def change_name(tag):
        if tag.name == "section":
            return "div"
        return tag.name

    replacer = SoupReplacer(name_xformer=change_name)
    html = '<section id="outer"><section>Hello</section></section>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == '<div id="outer"><div>Hello</div></div>'


# check that adding a class keeps the existing id and text
def test_attrs_xformer_adds_class_and_keeps_id():
    def change_attrs(tag):
        attrs = tag.attrs.copy()
        if tag.name == "p":
            attrs["class"] = ["test"]
        return attrs

    replacer = SoupReplacer(attrs_xformer=change_attrs)
    html = '<p id="x">Hello</p>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    paragraph = soup.find("p")
    assert paragraph["class"] == ["test"]
    assert paragraph["id"] == "x"
    assert paragraph.get_text() == "Hello"


# check that an old class is replaced only on p tags
def test_attrs_xformer_replaces_existing_class():
    def change_attrs(tag):
        attrs = tag.attrs.copy()
        if tag.name == "p":
            attrs["class"] = ["test"]
        return attrs

    replacer = SoupReplacer(attrs_xformer=change_attrs)
    html = '<p class="old">Hello</p><div class="keep">Other</div>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert soup.find("p")["class"] == ["test"]
    assert soup.find("div")["class"] == ["keep"]


# check direct changes on tags with and without a class
def test_xformer_removes_class():
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    replacer = SoupReplacer(xformer=remove_class)
    html = '<p class="old" id="x">Hello</p><p>Keep this</p>'
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == '<p id="x">Hello</p><p>Keep this</p>'


# check that name, attributes, and direct changes run in order
def test_all_three_transformers_together():
    def change_name(tag):
        if tag.name == "em":
            return "b"
        return tag.name

    def change_attrs(tag):
        attrs = tag.attrs.copy()
        if tag.name == "b":
            attrs["class"] = ["strong"]
        return attrs

    def change_text(tag):
        if tag.get("class") == ["strong"]:
            tag.string = "Changed"

    replacer = SoupReplacer(
        name_xformer=change_name,
        attrs_xformer=change_attrs,
        xformer=change_text,
    )
    html = "<em>Hello</em><p>Keep this</p>"
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert str(soup) == '<b class="strong">Changed</b><p>Keep this</p>'