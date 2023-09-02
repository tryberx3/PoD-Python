

class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def render(self):
        print(f"Tree at ({self.x}, {self.y}) of type '{self.tree_type.name}' (Color: {self.tree_type.color}, Texture: {self.tree_type.texture})")


class Forest:
    def __init__(self):
        self.trees = []

    def plant_tree(self, x, y, tree_type_name):
        tree_type = self.get_tree_type(tree_type_name)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def get_tree_type(self, name):
        for tree_type in self.tree_types:
            if tree_type.name == name:
                return tree_type
        return None

    def report(self):
        for tree in self.trees:
            tree.render()

if __name__ == "__main__":
    forest = Forest()
    forest.tree_types = [TreeType("Oak", "Green", "Rough"), TreeType("Pine", "Green", "Smooth")]

    forest.plant_tree(1, 1, "Oak")
    forest.plant_tree(2, 2, "Pine")
    forest.plant_tree(3, 3, "Oak")
    forest.plant_tree(4, 4, "Pine")

    forest.report()
