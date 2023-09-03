

class TextEditorMemento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


class TextEditor:
    def __init__(self):
        self._content = ""

    def write(self, text):
        self._content += text

    def show_content(self):
        return self._content

    def create_memento(self):
        return TextEditorMemento(self._content)

    def restore_from_memento(self, memento):
        self._content = memento.get_content()


class History:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

if __name__ == "__main__":
    text_editor = TextEditor()
    history = History()

    # Escribimos en el editor de texto
    text_editor.write("Hola, ")
    history.add_memento(text_editor.create_memento())  # Guardamos el estado

    text_editor.write("Mundo!")
    history.add_memento(text_editor.create_memento())  # Guardamos el estado

    # Mostramos el contenido actual
    print("Contenido actual:", text_editor.show_content())

    # Restauramos el estado anterior
    text_editor.restore_from_memento(history.get_memento(0))

    # Mostramos el contenido restaurado
    print("Contenido restaurado:", text_editor.show_content())
