from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
oylik_paket =ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ Internet paket-1'),
            KeyboardButton(text='๐ Internet paket-3')
        ],
        [
            KeyboardButton(text='๐ Internet paket-6'),
            KeyboardButton(text='๐ Internet paket-9')
        ],
        [
            KeyboardButton(text='๐ Internet paket-12'),
            KeyboardButton(text='๐ Internet paket-15')
        ],
        [
            KeyboardButton(text='๐ Internet paket-20'),
            KeyboardButton(text='๐ Internet paket-30')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ]
)
hafta_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ Hafta 100 MB')
        ],
        [
            KeyboardButton(text='๐ Hafta 400 MB')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)
kun_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ Kun 10 MB'),
            KeyboardButton(text='๐ Kun 20 MB'),
        ],
        [
            KeyboardButton(text='๐ Kun 30 MB'),
            KeyboardButton(text='๐ Kun+ 150 MB'),
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)
g_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ ยซ4G KUNยป'),
            KeyboardButton(text='๐ ยซ4G OYยป')
        ],
        [
            KeyboardButton(text='<--Orqaga')
        ]
    ],resize_keyboard=True
)