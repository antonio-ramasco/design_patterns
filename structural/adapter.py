class Target():
    def request(self) -> str:
        return "Target request"

class Adaptee:
    def specific_request(self) -> str:
        return "Adaptee request"

class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter request into {self.specific_request()}"

def client_code(target: "Target") -> str:
    return target.request()
