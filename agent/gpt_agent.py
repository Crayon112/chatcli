import openai
from typing import List

from .agent import Agent
from .message import Message
from .role import Role
from ..exceptions import ResponseKeyNotFound


class GPTAgent(Agent):

    name = "gpt"

    def __init__(
        self,
        openai_key: str,
        init_messages: List[Message] = None,
        version = "turbo-3.5",
    ) -> None:
        self._openai_key = openai_key
        self.messages = init_messages or []
        self.version = version

    def send(
        self,
        message: str,
        save_to_history: bool = True,
    ) -> str:
        """Send a message to the bot."""
        message = Message(Role.User, message)
        input_ = self.messages + [message]

        openai.api_key = self._openai_key
        try:
            res = openai.ChatCompletion.create(
                model=f"gpt-{self.version}",
                messages=[i.serialize() for i in input_],
                timeout=10,
            )
        except Exception as e:
            raise e

        try:
            response = res["choices"][0]["message"]
        except KeyError:
            raise ResponseKeyNotFound("No response received from the server.")

        if save_to_history:
            self.messages.extend([
                message,
                Message(response["role"], response["content"]),
            ])

        return response["content"]
