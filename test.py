import asyncio
from twikit import Client

async def main():
    client = Client(language='en-US')
    client.load_cookies("cookies_fixed.json")

    user = await client.get_user_by_screen_name("elonmusk")
    tweets = await user.get_tweets("Tweets", count=10)

    for t in tweets:
        print(t.created_at, ":", t.text)

asyncio.run(main())
