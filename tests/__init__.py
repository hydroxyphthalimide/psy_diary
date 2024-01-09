import asyncio
import telegram


async def main():
    bot = telegram.Bot("6972748303:AAEYkE3nyWE-i-lCz4GKC8-OuxqvagSh8X0")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())