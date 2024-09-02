from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import bot_additions.keyboard as kb
import func_addition.launch_game as games
from config import GAMES

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, chose a game to start", reply_markup=kb.games)


@router.callback_query(F.data == 'dota')
async def dota_start(callback: CallbackQuery):
    await callback.message.edit_text("Dota in process", reply_markup=kb.close_dota)
    program_id, program_name = GAMES['DOTA']
    await games.dota_start(program_id, program_name)
    await callback.message.edit_text("Dota process has ended. Something else?", reply_markup=kb.games)

#todo: сделать универсальную функцию для запуска приложений и игр
# def program_start(name):
#     await callback.message.edit_text("Dota in process", reply_markup=kb.close_dota)
#     program_id, program_name = GAMES['DOTA']
#     await games.dota_start(program_id, program_name)
#     await callback.message.edit_text("Dota process has ended. Something else?", reply_markup=kb.games)


@router.callback_query(F.data == 'close_dota')
async def close_dota_call(callback: CallbackQuery):
    program_id, program_name = GAMES['DOTA']
    await games.close_dota_fun(program_name)


@router.callback_query(F.data == 'under')
async def under_start(callback: CallbackQuery):
    await callback.message.edit_text("Under in process", reply_markup=kb.close_under)
    program_id, program_name = GAMES['UNDERMINE']
    await games.dota_start(program_id, program_name)
    await callback.message.edit_text("UnderMine process has ended. Something else?", reply_markup=kb.games)


@router.callback_query(F.data == 'close_under')
async def close_dota_call(callback: CallbackQuery):
    program_id, program_name = GAMES['UNDERMINE']
    await games.close_dota_fun(program_name)
