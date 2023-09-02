

class CPU:
    def freeze(self):
        print("CPU: Freezing...")

    def jump(self, position):
        print(f"CPU: Jumping to address {position}")

    def execute(self):
        print("CPU: Executing...")

class Memory:
    def load(self, program):
        print(f"Memory: Loading program '{program}'")

class HardDrive:
    def read(self, sector, size):
        return f"Hard Drive: Reading {size} bytes from sector {sector}"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self, program):
        print("ComputerFacade: Starting the computer...")
        self.memory.load(program)
        self.cpu.freeze()
        self.cpu.jump(0)
        self.cpu.execute()
        print("ComputerFacade: Computer is now running.")



def main():
    computer = ComputerFacade()
    program = "My Awesome Program"
    computer.start(program)

if __name__ == "__main__":
    main()
