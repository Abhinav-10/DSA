## Duck typing 
"""
if it looks likes a duck swims like a duck
and quacks like a duck then it probably is a duck 
"""

class Vscode:
    def execute(self):
        print("Compiling")
        print('running')


class Laptop:

    def code(self, ide):
        ide.execute()

ide1 = Vscode()

lap1 = Laptop()

lap1.code(ide1)