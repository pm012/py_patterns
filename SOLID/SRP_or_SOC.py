class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


# The below is a bad solution because the persistance methods can be applied to another classes
# So this should be moved out to another class devoted to persistance
# def save(self, filename):
#     file = open(filename, 'w')
#     file.write(str(self))
#     file.close()
#
# def load(self, filename):
#     pass
#
# def low_from_web(self, url):
#     pass
import os
class PersistanceManager:

    @staticmethod
    def save_to_file(journal, filename):
        path = os.path.dirname(filename)
        try: 
            os.makedirs(path)
        except FileExistsError:
            pass
        
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(str(journal))    
        else:
            file = open(filename, 'w')
            file.write(str(journal))
            file.close()


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = r'SOLID/res/journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())
