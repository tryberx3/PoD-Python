

import copy

class BaseTask:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def clone(self):
        return copy.deepcopy(self)
    

class DevTask(BaseTask):
    def __init__(self, name, description, devtool):
        super().__init__(name=name, description=description)
        self.devtool = devtool
    
    def __str__(self):
        return f"Task Name: {self.name}\nDescription: {self.description}\nDeveloper Tool: {self.devtool}"


class DesTask(BaseTask):
    def __init__(self, name, description, destool):
        super().__init__(name=name, description=description)
        self.destool = destool

    def __str__(self):
        return f"Task Name: {self.name}\nDescription: {self.description}\nDesigner Tool: {self.destool}"


DevTGenerator = DevTask(name="Development Task", description="AAAA", devtool="Python")
DesTGenerator = DesTask(name="Design Task", description="BBBB", destool="Adobe Photoshop")

task1 = DevTGenerator.clone()
task1.name = "Implement Login Feature"
print(task1)

task2 = DesTGenerator.clone()
task2.name = "Create Logo Design"
print(task2)