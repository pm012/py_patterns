"""
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

    cb = CodeBuilder('Person').add_field('name', '""') \
                              .add_field('age', '0')
    print(cb)

The expected output of the above code is:

    class Person:
      def __init__(self):
        self.name = ""
        self.age = 0

Please observe the same placement of spaces and indentation.
"""


class CodeBuilder:
    indent_size = 2

    def __init__(self, root_name):
        self.root_name = root_name
        self.code = []

    def add_field(self, name, value):
        field = f'self.{name} = {value}'
        self.code.append(field)
        return self

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'class {self.root_name}:')
        if len(self.code) > 0:
            i_def = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i_def}def __init__(self):')
        else:
            i_def = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i_def}pass')
        for e in self.code:
            i_def = ' ' * ((indent + 2) * self.indent_size)
            lines.append(f'{i_def}{e}')

        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)


cb = CodeBuilder('Person').add_field('name', '""') \
    .add_field('age', '0')
print(cb)

cd = CodeBuilder('Foo')
print(cd)
