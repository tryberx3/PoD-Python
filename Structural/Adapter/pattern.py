

class Printer:
    def print_message(self, message):
        print(f"Printing: {message}")


class Computer:
    def __init__(self, message):
        self.message = message

    def send_to_printer(self, printer):
        printer.print_message(self.message)


class Adapter:
    def __init__(self, printer):
        self.printer = printer

    def send(self, message):
        self.printer.print_message(message)


def main():
    printer = Printer()  
    computer = Computer("Hello, World!")  

    computer.send_to_printer(printer)  

    adapter = Adapter(printer)
    computer.send_to_printer(adapter)

if __name__ == "__main__":
    main()
