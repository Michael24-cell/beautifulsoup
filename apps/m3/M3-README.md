# Milestone-3

I recommend extending SoupReplacer to accept functions supplied by the user while keeping the original way of supplying two tag names. Supplying two names works for simple renaming, like changing b to blockquote. Functions let users check a tag’s name, attributes, or contents before deciding what to change.

The new approach gives users more freedom over how they change a document. They can add or remove attributes, keep an ID while replacing a class, or change a tag’s contents based on what is already there. Users write the rules for their own tasks, and SoupReplacer applies them during parsing. This also lets the library support different uses without adding a separate method for every kind of change.

The extension accepts three optional functions. name_xformer returns a replacement name. attrs_xformer returns a replacement attributes dictionary. xformer changes the tag directly and returns nothing. Each function receives the whole tag. I recommend using the name and attribute options for those specific changes and xformer when direct edits are needed.

In my implementation, popTag calls SoupReplacer’s apply method during parsing. It runs the original tag-name replacement first, followed by name_xformer, attrs_xformer, and xformer. After xformer runs, I update the most recent element reference so parsing can continue correctly if a node was removed or replaced.

Making changes during parsing avoids another full search afterward. There is still extra work from calling functions and copying attributes. Updating the most recent element follows the tree’s last-child path, so repeated updates can cost more on deeply nested documents. I keep that update limited to xformer. The tree remains in memory, and performance also depends on what the supplied functions do.

I added six new tests covering name changes, nested tags, adding and replacing attributes, removing attributes, and combining all three functions. The two original tests remain.

task7.py gives p tags class="test" while preserving their other attributes. It saves prettified output to a file ending in .class-test.

Run from the beautifulsoup folder with the virtual environment activated:

python apps/m3/task7.py path-to-input.html

Run the tests:

python -m pytest bs4/tests