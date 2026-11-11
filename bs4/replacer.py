class SoupReplacer:
    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def replace_name(self, name):
        if name == self.og_tag:
            return self.alt_tag
        return name

    def apply(self, tag):
        # apply the original replacement
        tag.name = self.replace_name(tag.name)

        # use the supplied functions if they exist
        if self.name_xformer is not None:
            tag.name = self.name_xformer(tag)

        if self.attrs_xformer is not None:
            tag.attrs = self.attrs_xformer(tag)

        if self.xformer is not None:
            self.xformer(tag)