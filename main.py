import os
import discord
import asyncio

from discord.ext import tasks
from dotenv import load_dotenv
from datetime import datetime, timedelta
from itemmania import check_attendance


load_dotenv(dotenv_path=".env")

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')


class MyDiscordClient(discord.Client):
    async def on_ready(self):
        channel = self.get_channel(int(CHANNEL_ID))
        self.daily_task.start()

    @tasks.loop(hours=24)
    async def daily_task(self):
        channel = self.get_channel(int(CHANNEL_ID))
        if channel:
            response = check_attendance()
            # response가 None이 아닌지 확인
            if response and isinstance(response, dict):
                await channel.send(f"result: {response.get('result', 'N/A')}")
                await channel.send(f"msg: {response.get('msg', 'N/A')}")
                await channel.send(f"data: {response.get('data', '없음')}")
            else:
                await channel.send("오류가 발생하여 데이터를 가져오지 못했습니다.")

    @daily_task.before_loop
    async def before_daily_task(self):
        await self.wait_until_ready()

        # 원하는 실행 시간 (매일 오전 9시로 설정)
        now = datetime.now()
        target_time = now.replace(hour=9, minute=0, second=0, microsecond=0)

        # 이미 9시가 지났다면 다음 날로 설정
        if now >= target_time:
            target_time += timedelta(days=1)

        # 지정된 시간까지 기다림
        await asyncio.sleep((target_time - now).total_seconds())


def run_bot():
    try:
        intents = discord.Intents.default()
        intents.message_content = True
        client = MyDiscordClient(intents=intents)
        client.run(TOKEN)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_bot()
