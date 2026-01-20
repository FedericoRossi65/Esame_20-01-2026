from dataclasses import dataclass

@dataclass
class Collegamenti:
    a1 : str
    a2 : str
    peso: int

    def __str__(self):
        return f"{self.a1}, {self.a2}, {self.peso}"
    def __hash__(self):
        return hash((self.a1, self.a2, self.peso))

