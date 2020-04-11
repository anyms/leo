class Token:
    def __init__(self, is_block, label, value, block, identifier):
        self.is_block = is_block
        self.label = label
        self.value = value
        self.block = block
        self.identifier = identifier

    def __repr__(self):
        return "{{is_block: {}, label: {}, value: {}, block: {}}}".format(
            self.is_block,
            self.label,
            self.value,
            self.block,
            self.identifier
        )