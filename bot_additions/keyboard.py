from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

games = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="UnderMine", callback_data='under')],
    [InlineKeyboardButton(text="Dota", callback_data='dota')]
])


close_dota = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Close Dota", callback_data='close_dota')]
])

close_under = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Close UnderMine", callback_data='close_under')]
])