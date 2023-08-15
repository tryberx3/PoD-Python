

class Server:
    def get(self, resource):
        print(f"Requesting the resource: {resource}")

class Proxy:
    def __init__(self):
        self.server = Server()

    def get(self, resource):
        if(self.auth()):
            self.log_get(resource=resource)
            self.server.get(resource=resource)
            self.log_access(resource=resource)

    def auth(self):
        print("Authenticating the customer...")
        return True

    def log_get(self, resource):
        print(f"Requesting the resource request: {resource}")

    def log_access(self, resource):
        print(f"Requesting access of the resource: {resource}")


proxy = Proxy()
proxy.get(resource="archivo1.txt")