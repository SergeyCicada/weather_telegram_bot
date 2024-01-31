import asyncio
import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from app.functions.weather_api_service import get_weather


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start c простым ответом
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуй, надеемся на хорошую погоду! Введи название города:")


# Хэндлер на ответ при введении города с обработкой ошибок
@dp.message()
async def cmd_all(message: types.Message):
    try:
        weather = get_weather(f"{message.text}")
        await message.reply(f"Погода: {weather.weather_type}, температура: {weather.temperature}")
    except Exception:
        await message.answer(f"Прости, такой город не найден.")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
