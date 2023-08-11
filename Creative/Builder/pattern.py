

class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None

    def __str__(self):
        return f"Computer: CPU={self.cpu}, GPU={self.gpu}, RAM={self.ram}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_cpu(self, cpu):
        self.computer.cpu = cpu

    def configure_gpu(self, gpu):
        self.computer.gpu = gpu

    def configure_ram(self, ram):
        self.computer.ram = ram

class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_high_end_computer(self):
        self.builder.configure_cpu("Intel Core i9")
        self.builder.configure_gpu("NVIDIA RTX 3080")
        self.builder.configure_ram("32GB DDR4")

    def build_mid_range_computer(self):
        self.builder.configure_cpu("AMD Ryzen 7")
        self.builder.configure_gpu("NVIDIA GTX 1660")
        self.builder.configure_ram("16GB DDR4")

# Usage
builder = ComputerBuilder()
director = Director(builder)

director.build_high_end_computer()
high_end_computer = builder.computer
print(high_end_computer)  # Output: Computer: CPU=Intel Core i9, GPU=NVIDIA RTX 3080, RAM=32GB DDR4

director.build_mid_range_computer()
mid_range_computer = builder.computer
print(mid_range_computer)  # Output: Computer: CPU=AMD Ryzen 7, GPU=NVIDIA GTX 
