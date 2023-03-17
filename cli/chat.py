import argparse


from .run import run
from ..agent.agent import MetaAgent


def choose_bot(api_key, name, version):
    """Choose a bot for the chat."""
    bot_class = MetaAgent.get_bot_class(name)
    bot = bot_class(openai_key=api_key, version=version)
    return bot


def chat():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='A simple CLI for Chat AI',
    )

    # OPENAI API KEY选项
    parser.add_argument(
        "--key",
        type=str,
        required=True,
        help="OpenAI API key"
    )

    # 机器人选项
    parser.add_argument(
        "--bot", type=str,
        default="gpt",
        help="Choose a bot for the chat"
    )

    # 版本选项
    # 机器人选项
    parser.add_argument(
        "--version", type=str,
        default="3.5-turbo",
        help="Choose a version for the bot"
    )
    

    args = parser.parse_args()
    chat_bot = choose_bot(args.key, args.bot, args.version)
    run(chat_bot)
