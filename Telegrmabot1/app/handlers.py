from aiogram import Router , F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter 
import app.keyboards as kb

router = Router()

class Admin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [5649321700]

@router.message(Admin(), F.text == '/admin')
async def cmd_admin(message: Message):
    await message.answer('Siz admin')

#Salomlashuv
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Hush kelibsiz Kimni no\'meri kerak!!' , reply_markup=kb.main)

#Zafarakamning nomeri
@router.message(F.text == 'Zafar')
async def nomerz(message: Message):
    await message.answer('Nomerlari', reply_markup=kb.nomerz)

#Mening nomerim
@router.message(F.text == 'Sunnat')
async def nomerS(message: Message):
    await message.answer('Nomerlari', reply_markup=kb.nomerS)
#Adamning nomer
@router.message(F.text == 'Anvar')
async def nomera(message: Message):
    await message.answer('Nomerlari', reply_markup=kb.nomera)
#Munis
@router.message(F.text == 'Munisa')
async def nomerm(message: Message):
    await message.answer('Nomerlari', reply_markup=kb.nomerm)
#Dodasi
@router.message(F.text == 'Dodasi')
async def nomerd(message: Message):
    await message.answer('Nomerlari', reply_markup=kb.nomerd)


@router.message(F.text == 'Bizning kanal')    
async def socials(message: Message):
    await message.answer('Bizning kanalga obun bo\'ling', reply_markup=kb.socials)


@router.callback_query(F.data == 'adidas')
async def adidas(callback: CallbackQuery):
    await callback.message.answer(f'Siz {callback.data}  brendini tanladiz ////')














 
