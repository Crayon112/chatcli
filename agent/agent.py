class MetaAgent(type):

    bot_map = {}

    def __new__(cls, name, bases, attrs):
        cls_ = super().__new__(cls, name, bases, attrs)
        cls.bot_map[cls_.name] = cls_
        return cls_
    
    @classmethod
    def get_bot_class(cls, name):
        return cls.bot_map.get(name)


class Agent(object, metaclass=MetaAgent):

    name = "agent"

    def __init__(self) -> None:
        pass

    def send(self, message: str) -> None:
        """发送消息.
        
        Args:
            message: 要发送的消息.
        
        """
        pass