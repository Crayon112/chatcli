import json


class Message(object):
    """消息类.
    
    Attributes:
        role: 消息发送者的角色.
        content: 消息内容.
        name: 消息名称.
    
    """

    def __init__(self, role: "Role", content: str, name: str = "") -> None:
        self.role = role
        self.content = content
        self.name = name
    
    def serialize(self):
        """序列化消息.
        
        Returns:
            序列化后的消息.
        
        """
        to_serialize = {
            'role': self.role,
            'content': self.content,
        }
        return to_serialize