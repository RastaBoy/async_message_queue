


class Serializable():
    
    def __dict__(self):
        ...

    def to_json(self):
        return self.__dict__()