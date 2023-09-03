

# State interface
class WritingState:
    def write(self, words):
        pass


# Concrete States
class UpperCase(WritingState):
    def write(self, words):
        print(words.upper())

class LowerCase(WritingState):
    def write(self, words):
        print(words.lower())

class DefaultState(WritingState):
    def write(self, words):
        print(words)


# Context
class TextEditor:
    def __init__(self):
        self._state = DefaultState()

    def set_state(self, state):
        self._state = state

    def type(self, words):
        self._state.write(words)


if __name__ == "__main__":
    editor = TextEditor()

    editor.type("Hello")  # Default state
    editor.set_state(UpperCase())
    editor.type("World")  # Uppercase state
    editor.set_state(LowerCase())
    editor.type("Python")  # Lowercase state
