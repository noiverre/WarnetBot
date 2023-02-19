import asyncio

from bot.config import config
from bot.bot import WarnetBot


def main():
    bot = WarnetBot()
    try:
        # Set debug=True for local db testing
        asyncio.run(bot.start(debug=config.BOT_DEBUG))
    except KeyboardInterrupt:
        print("Logging Out...")


if __name__ == "__main__":
    main()
