# Milestone-2

## Part 2: Original API definitions

These references use the original BeautifulSoup 4.13.0 source, before library changes.

Original commit: [23fe4f4da77e4de272168f4e49085c5def338b91](https://github.com/Michael24-cell/beautifulsoup/commit/23fe4f4da77e4de272168f4e49085c5def338b91).

Line numbers identify the first `def` line of each method. For constructors, the class declaration is also listed below. Links point to this original commit so they remain useful after later edits.

### API calls

| Call used in the applications | Definition | Original file | Start line | Used in |
| --- | --- | --- | ---: | --- |
| `BeautifulSoup(text, parser, ...)` | `BeautifulSoup.__init__` | [`bs4/__init__.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/__init__.py#L209) | 209 | All eight M1 tasks; M2 tasks 2–4 |
| `soup.prettify()` | `Tag.prettify` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2601) | 2601 | M1 tasks 1, 6, 7, 8 |
| `soup.find_all(...)` | `Tag.find_all` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2715) | 2715 | M1 tasks 2–8; M2 tasks 2–4 |
| `tag.get("href")` | `Tag.get` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2160) | 2160 | M1 task 2; M2 task 2 |
| `tag.get_text(" ", strip=True)` | `PageElement.get_text` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L524) | 524 | M1 task 5 |
| `paragraph.find_parent("div")` | `PageElement.find_parent` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L992) | 992 | M1 task 5 |
| `soup.new_tag("p")` | `BeautifulSoup.new_tag` | [`bs4/__init__.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/__init__.py#L682) | 682 | M1 task 8 |
| `tag.has_attr("alt")` | `Tag.has_attr` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2196) | 2196 | M1 task 8 |
| `tag.replace_with(paragraph)` | `PageElement.replace_with` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L552) | 552 | M1 task 8 |
| `SoupStrainer(...)` | `SoupStrainer.__init__` | [`bs4/filter.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/filter.py#L345) | 345 | M2 tasks 2–4 |

The BeautifulSoup class declaration is in `bs4/__init__.py`, line 133. Its constructor starts at line 209.
The SoupStrainer class declaration is in `bs4/filter.py`, line 313. Its constructor starts at line 345.

### What each call does in my programs

- `BeautifulSoup(text, parser, ...)`: Creates the soup object and starts parsing. `text` goes to `markup`; `parser` goes to `features`; `parse_only` receives the optional filter.
- `soup.prettify()`: Returns formatted markup. With no encoding argument, it returns a Python string that the script writes to a UTF-8 text file.
- `soup.find_all(...)`: Selects descendants to search and passes the filters to `_find_all`. `"a"` matches tag names, `True` matches all tags, and `id=True` matches an attribute's presence.
- `tag.get("href")`: Reads the href attribute. A missing attribute returns the default, which is None unless supplied.
- `tag.get_text(" ", strip=True)`: Collects descendant text, strips the individual text pieces, and joins them with spaces. It does not change the tree.
- `paragraph.find_parent("div")`: Searches upward and returns the nearest matching ancestor, or None if there is no match.
- `soup.new_tag("p")`: Creates a new Tag named p. Creating it does not insert it into the document.
- `tag.has_attr("alt")`: Checks whether the attribute key exists. An empty alt attribute still exists and passes this check.
- `tag.replace_with(paragraph)`: Detaches the old element and inserts the replacement in its position. It returns the detached old element; references to that object still work.
- `SoupStrainer(...)`: Builds matching rules. `SoupStrainer("a")`, `SoupStrainer(True)`, and `SoupStrainer(id=True)` describe the selections for tasks 2, 3, and 4.

### Attribute access and assignment

Some operations use a property or a special method instead of an explicit method call.

| Operation | Definition | Original file | Start line | Used in |
| --- | --- | --- | ---: | --- |
| `tag["alt"]` | `Tag.__getitem__` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2203) | 2203 | M1 task 8 |
| `tag["class"] = "test"` | `Tag.__setitem__` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L2223) | 2223 | M1 task 7 |
| `paragraph.string = tag["alt"]` | `Tag.string setter` | [`bs4/element.py`](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L1861) | 1861 | M1 task 8 |

- `tag["alt"]`: Reads an attribute using brackets. Unlike get(), a missing key raises KeyError.
- `tag["class"] = "test"`: Adds or replaces the class attribute in the tag's attribute dictionary.
- `paragraph.string = tag["alt"]`: Replaces the paragraph's contents with one text node containing the alt text.

`tag.name` and `tag.attrs` are ordinary instance attributes, so they do not have separate method definitions:

- `tag.name` is initialized by `Tag.__init__` at [`bs4/element.py`, line 1648](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L1648). Task 3 reads it to print the tag name. Task 5 reads the parent div's name. Task 6 assigns `"blockquote"` to rename each b element while preserving its attributes and contents.
- `tag.attrs` holds the attribute dictionary. Its initialization is in [`bs4/element.py`, lines 1674–1689](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/element.py#L1674); the assignment used depends on the parser and incoming attributes. Task 5 prints this dictionary. The type annotations for `name` and `attrs` are at lines 1740 and 1743.

### How SoupStrainer connects to parsing

`SoupStrainer(...)` constructs the rules. The `parse_only` constructor parameter is declared at `bs4/__init__.py`, line 214, and stored as `self.parse_only` at line 437.

During tag creation, [`BeautifulSoup.handle_starttag`, line 987](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/__init__.py#L987), checks the active filter at lines 1021–1026, before creating the Tag at line 1032. It calls [`SoupStrainer.allow_tag_creation`, `bs4/filter.py`, line 580](https://github.com/Michael24-cell/beautifulsoup/blob/23fe4f4da77e4de272168f4e49085c5def338b91/bs4/filter.py#L580) to apply the rules.

The filter check is made when there is no selected element currently open (`len(self.tagStack) <= 1`). Once a matching element is selected, its descendants are kept too. That is why the task 4 printing loop still uses `find_all(id=True)`: some descendants of selected elements may have no ID.

For task 3, `SoupStrainer(True)` accepts all tag names. Because the task needs every tag, this does not meaningfully reduce the retained tag tree; descendants and their contents remain.

### Why these methods are in different classes

`BeautifulSoup` extends `Tag`, and `Tag` extends `PageElement`. That lets a soup object use methods defined in those classes, such as `find_all`, `prettify`, and `get_text`.

Python operations such as `open`, `read`, `write`, `print`, `sys.exit`, and `endswith` are not BeautifulSoup APIs, so they are not included in the library-definition table.
