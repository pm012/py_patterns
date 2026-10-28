from abc import ABC
from enum import Enum, auto

class OutputFormats(Enum):
    JSON = auto()
    HTML = auto()
    MARKDOWN = auto()


class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass

class MarkdownListStrategy(ListStrategy):

    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')

class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')

    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')

class JSONListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('{\n  "ul": { \n    "li": [\n')
    
    def end(self, buffer):
        buffer.append('    ]\n  }\n}')
    
    def add_list_item(self, buffer, item):
        buffer.append(f'        {item},\n')    


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        
        self.list_strategy = list_strategy
        self.buffer = []

    def append_list(self, items):
        ls = self.list_strategy
        ls.start(self.buffer)
        for item in items:
            ls.add_list_item(self.buffer, item)
        ls.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormats.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormats.HTML:
            self.list_strategy = HtmlListStrategy()
        elif format == OutputFormats.JSON:
            self.list_strategy = JSONListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)

if __name__ == "__main__":
    items = ['foo', 'bar', 'baz']

    tp = TextProcessor()
    tp.set_output_format(OutputFormats.MARKDOWN)
    tp.append_list(items)
    
    print(tp)
    print('-------------------------------')

    tp.set_output_format(OutputFormats.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)

    print('--------------------------------')
    tp.set_output_format(OutputFormats.JSON)
    tp.clear()
    tp.append_list(items)
    print(tp)


