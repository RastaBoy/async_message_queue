from dataclasses import dataclass, asdict

@dataclass
class SerializableDTO:

    def serialize(self):
        return asdict(self)


@dataclass
class Message(SerializableDTO):
    title : str
    text : str


