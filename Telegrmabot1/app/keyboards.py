from aiogram.types import( ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


""" 
Sobshenyaga ulangan knopka //inline keyboard//

menyuda chiqadiga knopka //reply keyboard//

"""
#boshidagi sahifadagi knopka

main_kb = [
      [KeyboardButton(text='Zafar'),
       KeyboardButton(text='Sunnat')],
      [KeyboardButton(text='Anvar'),
       KeyboardButton(text='Munisa'),
       KeyboardButton(text='Dodasi'),
       KeyboardButton(text='Bizning kanal')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

socials = InlineKeyboardMarkup(inline_keyboard =[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/ITandDEVELOPER')],
    [InlineKeyboardButton(text='Youtube', url='https://youtube.com/shorts/I9OPI2hoCpg?si=uObh0BftG5rMHUEG')]

])

nomerS =  InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='+99893 105 05 15', callback_data='+99893 105 05 15')]
     
])
nomera =  InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='+99893 378 43 76', callback_data='+99893 378 43 76')]
          
])


nomerm =  InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='+99893 577 00 37', callback_data='+99893 577 00 37')]
])     


nomerd =  InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='+99894 639 69 30', callback_data='+99894 639 69 30')]
])


nomerz = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='+99893 171 14 15', callback_data='+99893 171 14 15')]
     
])


























