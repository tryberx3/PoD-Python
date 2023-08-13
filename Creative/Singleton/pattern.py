

class EventLogger:
    instance = None

    def __init__(self):
        self.logs = []
    
    @staticmethod
    def get_instance():
        if(EventLogger.instance is None):
            EventLogger.instance = EventLogger()
        return EventLogger.instance
    
    def add_log(self, event):
        self.logs.append(event)
    
    def display_logs(self):
        for log in self.logs:
            print(log)


inst1 = EventLogger.get_instance()
inst2 = EventLogger.get_instance()

print(inst1 == inst2)
print(id(inst1))
print(id(inst2))

inst1.add_log(event="A")
inst2.add_log(event="B")

inst1.display_logs()