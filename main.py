from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio
from aiogram.types import FSInputFile
import qrcode_generator
import clear

bot = Bot("5820873998:AAFiHN1P94CU0PO5xyJWaZ7scsirVlbXFUY")
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Введи ссылку или текст")


@dp.message(F.text)
async def send_photo(message: Message):
    qr_code = FSInputFile(qrcode_generator.generate(message.text, message.chat.id))
    await message.answer_photo(qr_code, caption=message.text)
    clear.delete_contents_of_directory()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Бот работает")
        asyncio.run(main())
    except:
        print("Бот перестал работать")
