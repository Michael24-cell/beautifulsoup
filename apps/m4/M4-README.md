# Milestone-4

I added an `__iter__` method to the BeautifulSoup class in `bs4/__init__.py`. A normal loop over soup now visits all nested nodes instead of only direct children. This includes tags, text, and comments.

BeautifulSoup already had a descendants iterator that could visit these nodes. I reused it by returning self.descendants from `__iter__`. Python gets this iterator when the loop starts, then requests one node at a time until iteration finishes.

I did not collect the nodes into another list. The existing iterator follows the tree’s next_element links and yields each node as needed. Visiting all n nodes takes O(n) time, and the iterator uses constant extra space. The document tree is still stored in memory.

The change makes a normal for loop use the existing deeper traversal. The soup object still has its other methods, such as find_all and prettify. Regular Tag objects keep their existing iteration behavior. Users who only want soup’s direct children can still loop over soup.children.

I wrote five tests checking nested node counts, multiple text nodes in order, empty soup, continuing after an empty tag, and visiting comment objects.

Run from the beautifulsoup folder with the virtual environment activated.

To run the new tests:

python -m pytest bs4/tests/test_iteration.py

To run the full test suite:

python -m pytest bs4/tests