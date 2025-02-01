
import logging
import requests
from pytube import YouTube
from instagram_scraper import InstagramScraper
from pinterest_scraper import PinterestScraper
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = 'YOUR_BOT_API_TOKEN'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Command to start the bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Videolarni ssilka orqali yuboring.")

# Handling YouTube video download
@dp.message_handler(lambda message: 'youtube.com' in message.text)
async def download_youtube_video(message: types.Message):
    url = message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video = stream.download()
        await bot.send_video(message.chat.id, video)
    except Exception as e:
        await message.reply("YouTube videosini yuklab olishda xatolik yuz berdi.")

# Handling Instagram video download
@dp.message_handler(lambda message: 'instagram.com' in message.text)
async def download_instagram_video(message: types.Message):
    url = message.text
    try:
        scraper = InstagramScraper()
        video_url = scraper.get_video_url(url)
        await bot.send_video(message.chat.id, video_url)
    except Exception as e:
        await message.reply("Instagram videosini yuklab olishda xatolik yuz berdi.")

# Handling Pinterest video download
@dp.message_handler(lambda message: 'pinterest.com' in message.text)
async def download_pinterest_video(message: types.Message):
    url = message.text
    try:
        scraper = PinterestScraper()
        video_url = scraper.get_video_url(url)
        await bot.send_video(message.chat.id, video_url)
    except Exception as e:
        await message.reply("Pinterest videosini yuklab olishda xatolik yuz berdi.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
