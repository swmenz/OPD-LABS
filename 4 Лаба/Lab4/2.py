import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.fsm import FSMContext, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Ваш токен для бота
API_TOKEN = '7924800088:AAEFNMquSelra0EMgAjlnYae_SwNL3eS5Kk'

# Создаем объект бота
bot = Bot(token=API_TOKEN)

# Создаем объект MemoryStorage
storage = MemoryStorage()

# Создаем объект Dispatcher
dp = Dispatcher()

# Устанавливаем storage для диспетчера
dp.storage = storage

# Словарь для хранения данных игроков (их текущий вопрос и правильные ответы)
games = {}

# Список вопросов и ответов
questions = [
    {
        'question': 'Сколько будет 2 + 2?',
        'options': ['1', '2', '3', '4'],
        'answer': '4'
    },
    {
        'question': 'Какой океан самый большой?',
        'options': ['Атлантический', 'Индийский', 'Тихий', 'Северный Ледовитый'],
        'answer': 'Тихий'
    },
    {
        'question': 'Какой элемент имеет символ "O"?',
        'options': ['Кислород', 'Углерод', 'Азот', 'Водород'],
        'answer': 'Кислород'
    },
    {
        'question': 'Кто написал "Преступление и наказание"?',
        'options': ['Пушкин', 'Толстой', 'Чехов', 'Достоевский'],
        'answer': 'Достоевский'
    },
    {
        'question': 'В каком году началась Вторая мировая война?',
        'options': ['1914', '1939', '1941', '1945'],
        'answer': '1939'
    }
]

# Начало игры
@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! Я бот для игры 'Кто хочет стать миллионером?'.\n"
                        "Напиши /play, чтобы начать игру.")

# Команда для начала игры
@dp.message_handler(commands=['play'])
async def play_game(message: types.Message):
    # Инициализируем данные игрока
    games[message.from_user.id] = {
        'question_number': 0,
        'correct_answers': 0
    }

    # Отправляем первый вопрос
    await ask_question(message)

# Функция для отправки следующего вопроса
async def ask_question(message: types.Message):
    user_data = games[message.from_user.id]
    question_number = user_data['question_number']

    if question_number >= len(questions):
        # Если все вопросы заданы, подводим итоги
        await message.reply(f"Игра завершена! Ты ответил правильно на {user_data['correct_answers']} из {len(questions)} вопросов.")
        del games[message.from_user.id]  # Завершаем игру для игрока
        return

    # Получаем текущий вопрос
    question = questions[question_number]
    options = "\n".join([f"{i+1}. {option}" for i, option in enumerate(question['options'])])

    # Отправляем вопрос с вариантами ответа
    await message.reply(f"Вопрос {question_number + 1}: {question['question']}\n\n{options}")

# Обработка ответа пользователя
@dp.message_handler(lambda message: message.text.isdigit())
async def check_answer(message: types.Message):
    user_data = games.get(message.from_user.id)

    if not user_data:
        await message.reply("Для начала игры, напиши /play.")
        return

    question_number = user_data['question_number']
    question = questions[question_number]

    # Проверяем ответ пользователя
    if question['options'][int(message.text) - 1] == question['answer']:
        user_data['correct_answers'] += 1

    # Переход к следующему вопросу
    user_data['question_number'] += 1
    await ask_question(message)

# Обработка текстовых сообщений, которые не являются числом
@dp.message_handler(lambda message: not message.text.isdigit())
async def not_a_number(message: types.Message):
    await message.reply("Пожалуйста, отправь число, чтобы выбрать вариант ответа.")

# Запуск бота с использованием asyncio
if __name__ == '__main__':
    # Запускаем бота
    asyncio.run(dp.start_polling())
