from aiogram import types
from keyboards.default.tariflar import *
from keyboards.default.usel_tariflar import *
from keyboards.default.asosiy_menu import *
from loader import dp


@dp.message_handler(text='๐ Tariflar')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_tarif)
@dp.message_handler(text='๐ Cosmo tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=cosmo_tarif)
@dp.message_handler(text='๐ฒ Special tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=special_tarif)
@dp.message_handler(text='โ Special+ tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=special_plus_tariflar)
@dp.message_handler(text='๐ญ Kayfiyat tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=kayfiyat_tariflar)
@dp.message_handler(text='๐ Tantana tariflari')
async def bot_start(message: types.Message):
    await message.answer(text="Tanlang",reply_markup=tantana_tarif)
@dp.message_handler(text='๐จ Marhamat tarifi')
async def bot_start(message: types.Message):
    await message.answer(text="""๐จ Marhamat tarifi:

Qoโngโiroqlar - 30 daqiqa ๐
Internet - 30 MB ๐

Limitdan tashqari:
Qoโngโiroqlar 1 daqiqasi  - 10 soโm
Internet 1 mb - 10 soโm
SMS  - 10 soโm
   
Abonent to`lovi oyiga 10 000 so`m ๐ฐ 
Tarif faqat yangi ulanuvchilar uchun amal qiladi
๐ @aloqa_operatorlar_bot    
""")


@dp.message_handler(text='๐ Yengil hafta')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Yengil hafta tarifi:

Qoโngโiroqlar - 200 daqiqa ๐
Internet -  200 MB ๐
SMS - 200 ta โ๏ธ
Abonent to`lovi haftasiga 5000 so`m ๐ฐ
     
Qoldiqlarni tekshirish: *103#     
Tarifga o`tish  *120#
๐ @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='๐ผ๏ธ Oddiy')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ผ๏ธ Oddiy:

Qoโngโiroqlar ๐ : 
    Tarmoq ichida 1 daqiqasi - 95 soโm
    Oโzbekiston boโyicha 1 daqiqasi- 120 soโm
SMS โ๏ธ: 
    Oโzbekiston boโyicha - 80 soโm
    Xalqaro chiqvchi sms - 1000 soโm
Internet ๐ :
 1 mb  - 450 soโm 

Abonent to`lovi kuniga - 380 so`m ๐ฐ    
Tarifga o`tish: *120#
๐ @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='๐ Student')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Student tarifi:

Qoโngโiroqlar - 700 daqiqa ๐
Internet -  3500 MB ๐
SMS - 200 ta โ๏ธ
Abonent to`lovi oyiga 10 000 so`m ๐ฐ

Qoldiqlarni tekshirish: 
    *103# - internet
    *102# - daqiqa va sms

Tarif faqat yangi ulanuvchilar uchun amal qiladi.
๐ @aloqa_operatorlar_bot    
""")
@dp.message_handler(text='โ๏ธ Uchar internet')
async def bot_start(message: types.Message):
    await message.answer(text="""โ๏ธ Uchar internet tarifi:

Internet trafigi cheksiz ๐ :
3000 mb tugagach keyingi abonent toโlovi yechilgunga qadar tezlik 64 kbit/s gacha qilib belgilanadi.  
 
Abonent to`lovi oyiga - 22 000 so`m ๐ฐ 
Tarifga o`tish: *120#
๐ @aloqa_operatorlar_bot    
""")


@dp.message_handler(text='<<Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_asosiy)
@dp.message_handler(text='<<<Orqaga')
async def bot_start(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=usel_tarif)
@dp.message_handler(text='๐ฐ Cosmo 16')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ COSMO 16 tarifi:

Qoโngโiroqlar - 1000 daqiqa ๐
Internet - 2000 MB ๐
SMS - 200 ta โ๏ธ
Abonent to`lovi oyiga - 16 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ฐ Cosmo 23')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ COSMO 23 tarifi:

Qoโngโiroqlar - 1500 daqiqa ๐
Internet - 3000 MB ๐
SMS - 300 ta โ๏ธ 
Abonent to`lovi oyiga - 23 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ฐ Cosmo 28')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ COSMO 28 tarifi:

Qoโngโiroqlar - 2000 daqiqa ๐
Internet - 5000 MB ๐
SMS - 500 ta โ๏ธ
Abonent to`lovi oyiga 28 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 35')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 35 tarifi:

Qoโngโiroqlar - 2500 daqiqa ๐
Internet - 7000 MB ๐
SMS - 1000 ta โ๏ธ
Abonent to`lovi oyiga - 35 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 45')
async def bot_start(message: types.Message):
    await message.answer(text="""๐  SPECIAL 45:

Qoโngโiroqlar - 3000 daqiqa ๐
Internet - 9000 MB ๐
SMS - 2000 ta โ๏ธ
Abonent to`lovi oyiga - 45 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#

๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 45')
async def bot_start(message: types.Message):
    await message.answer(text="""๐  SPECIAL 45:

Qoโngโiroqlar - 3000 daqiqa ๐
Internet - 9000 MB ๐
SMS - 2000 ta โ๏ธ
Abonent to`lovi oyiga - 45 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#

๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special 55')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 55 tarifi:

Qoโngโiroqlar - 4000 daqiqa ๐
Internet - 12 000 MB ๐
SMS - 3000 ta โ๏ธ  
Abonent to`lovi oyiga 55 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 70')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 70 tarifi:

Qoโngโiroqlar -  Cheksiz ๐
Internet - 16 000 MB ๐
SMS - 4 000 ta โ๏ธ
Abonent to`lovi oyiga - 70 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 70')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 70 tarifi:

Qoโngโiroqlar -  Cheksiz ๐
Internet - 16 000 MB ๐
SMS - 4 000 ta โ๏ธ
Abonent to`lovi oyiga - 70 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special 80')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 80 tarifi:

Qoโngโiroqlar -  Cheksiz daqiqa ๐
Internet - 18000 MB ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga - 80 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#

๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 100')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 100 :

Qoโngโiroqlar - Cheksiz ๐
Internet - 25 000 MB ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga 100 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120# :

Qoโngโiroqlar - Cheksiz ๐
Internet - 25 000 MB ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga 100 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special Unlim')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special Unlim :

Qoโngโiroqlar - Cheksiz ๐
Internet - Cheksiz ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga 139 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special Unlim')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special Unlim :

Qoโngโiroqlar - Cheksiz ๐
Internet - Cheksiz ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga 139 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special Unlim TURBO')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special Unlim TURBO :

Qoโngโiroqlar - Cheksiz ๐
Internet - ๐ Special unlim turbo
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga 150 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *120#

๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special 35โ')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 35โ tarifi:

Qoโngโiroqlar - 2500 daqiqa ๐
Internet - 7000 MB ๐
SMS - 1000 ta โ๏ธ
Abonent to`lovi oyiga - 37 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 55โ')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 55โ tarifi:

Qoโngโiroqlar - 4000 daqiqa ๐
Internet - 12 000 MB ๐
SMS - 3000 ta โ๏ธ 
Abonent to`lovi oyiga 57 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ Special 80โ')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 80โ tarifi:

Qoโngโiroqlar -  Cheksiz ๐
Internet - 18000 MB ๐
SMS - 5000 ta โ๏ธ
Abonent to`lovi oyiga - 82 000 so`m ๐ฐ

Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    

Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text='๐ Special 125โ')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Special 125โ tarifi:

Qoโngโiroqlar - Cheksiz ๐
Internet - 35 000 MB ๐
SMS - 5000 ta โ๏ธ 
Abonent to`lovi oyiga 127 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms
*103# - Megabaytlar    
    
Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text='๐ญ Yaxshi kayfiyat')
async def bot_start(message: types.Message):
    await message.answer(text="""๐ญ Yaxshi kayfiyat tarifi:

Qoโngโiroqlar ๐ : 
    750 daqiqa tarmoq ichida 
    75 daqiqa tarmoqdan tashqari

Internet ๐ :
 300 MB umumiy
 1000 MB messenjerlar uchun   
Abonent to`lovi oyiga - 13 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ญ Zo'r kayfiyat")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ญ Zoโr kayfiyat:

Qoโngโiroqlar ๐ : 
    1000 daqiqa tarmoq ichida 
    150 daqiqa tarmoqdan tashqari

Internet ๐ :
 500 MB umumiy
 1500 MB messenjerlar uchun 
Abonent to`lovi oyiga - 20 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ญ A'lo kayfiyat")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ญ A'lo kayfiyat:

Qoโngโiroqlar ๐ : 
    1200 daqiqa tarmoq ichida 
    200 daqiqa tarmoqdan tashqari

Internet ๐ :
 1200 MB umumiy
 2000 MB messenjerlar uchun  
Abonent to`lovi oyiga - 25 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish - *103#   
Tarifga o`tish uchun *120#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ Tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Tantana:

Qoโngโiroqlar - 1000 daqiqa ๐
SMS - 1000 ta โ๏ธ  
Abonent to`lovi oyiga 15 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms   
Tarifga o`tish: *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ Katta tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Katta tantana:

Qoโngโiroqlar - 1500 daqiqa ๐
SMS - 1500 ta โ๏ธ
Abonent to`lovi oyiga 20 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms 
    
Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ Super tantana")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Super tantana:

Qoโngโiroqlar - 3000 daqiqa ๐
SMS - 3000 ta โ๏ธ   
Abonent to`lovi oyiga 30 000 so`m ๐ฐ
     
Qoldiqlarni tekshirish:
*102# - Daqiqalar va sms 
    
Tarifga o`tish uchun *877#
๐ @aloqa_operatorlar_bot
""")


@dp.message_handler(text="๐ Oylik Internet toโplamlari")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Oylik Internet toโplamlari:

Toโplam 1 GB - 8 900 soโm
kod: *558*555*3*1*21691#

Toโplam 1,5 GB - 13 000 soโm
kod: *558*555*3*2*21691#

Toโplam 2 GB - 15 000 soโm
kod: *558*555*3*3*21691#

Toโplam 4 GB - 25 000 soโm
kod: *558*555*3*4*21691#

Toโplam 7 GB - 35 000 soโm
kod: *558*555*3*5*21691#

Toโplam 10 GB - 45 000 soโm
kod: *558*555*3*6*21691#

Toโplam 13 GB - 55 000 soโm
kod: *558*555*3*7*21691#

Toโplam 20 GB - 65 000 soโm
kod: *558*555*3*8*21691#

Toโplam 30 - 75 000 soโm
kod: *558*555*3*9*21691#

Toโplam 50 - 85 000 soโm
kod: *558*555*3*10*21691#

Toโplam 80 - 115 000 soโm
kod: *558*555*3*11*21691#

Toโplam 90 - 135 000   soโm
kod: *558*555*3*12*21691#

Toโplam 135 - 188 000   soโm
kod: *558*555*3*13*21691#

(koddan nusxa olish uchun ustiga bosing!)

MB amal qilish muddati - 31 kun
Trafik qoldigโini tekshirish: *107#
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ Haftalik Internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Haftalik Internet-toโplamlar:

Tarmoqdagi muloqot kamlik qilyaptimi? Unday boโlsa biz Sizga koโproq Internet taklif qilamiz!

Haftalik 80 toโplami - 8 420 soโm - 80 MB - *555*2*1*1#
Haftalik 160 toโplami - 12 630 soโm - 160 MB - *555*2*2*1#
Haftalik 320 toโplami - 16 840 soโm - 320 MB - *555*2*3*1#
Toโplamni oโchirish: *555*2*10*2*1# 

Xizmatni boshqarish: *๏ธโฃ5๏ธโฃ5๏ธโฃ5๏ธโฃ*๏ธโฃ2๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="โ๏ธ Kunlik Internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""
โ๏ธ Kunlik Internet-toโplamlar:

Toโplam 5 - 390 soโm - 5 MB - *555*1*1*1#

Toโplam 10 - 550 soโm - 10 MB - *555*1*2*1#

Toโplam 20 - 790 soโm - 20 MB - *555*1*3*1#

Toโplam 35 - 1 190 soโm - 35 MB - *555*1*4*1#

Toโplam 55 - 1 890 soโm - 55 MB - *555*1*5*1#

Toโplam 100 - 2 790 soโm - 100 MB - *555*1*6*1#

Toโplam 130 - 3 790 soโm - 130 MB - *555*1*7*1#

Toโplam 160 - 4 490 soโm - 160 MB - *555*1*8*1#

Toโplam 200 - 4 990 soโm - 200 MB - *555*1*9*1#

(koddan nusxa olish uchun ustiga bosing!)
๐ @aloqa_operatorlar_bot
""")

@dp.message_handler(text="โก๏ธInternet-oโtkazma")
async def bot_start(message: types.Message):
    await message.answer(text="""โก๏ธInternet-oโtkazma:

Internet-trafikni doโstingiz bilan baham koโring!
*525*998YYXXXXXXX*internet trafik hajmi(100-300)#
Bitta muvaffaqiyatli oโtkazma narxi 500 soโm
*Mablagโ Internet-trafik joโnatuvchi-abonent hisobidan ushlab qolinadi.

Xizmatni boshqarish: *๏ธโฃ5๏ธโฃ2๏ธโฃ5๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ Aksiya: 1gb, 2gb, va 3gb")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Aksiya: 1gb, 2gb, va 3gb:

Qoโshimcha hamyonbop internet-toโplamlar

Tarif rejasi boโyicha internet-trafigingiz yetmay qoldimi?

Yangi internet-toโplamlarni kutib oling:

  300 MB atigi 5 000 soโmga โ ยซCOSMOยป tariflar tizimi uchun

  1 GB atigi 8 000 soโmga โ ยซAโlo kayifyatยป tarifi va ยซCOSMOยป tariflar tizimi uchun

  1.5 GB atigi 15 000 soโmga โ ยซCOSMOยป tariflar tizimi uchun

  2 GB atigi 10 000 soโmga โ ยซActiveยป va ยซSpecialยป tariflar tizimlari uchun

  3 GB atigi 15 000 soโmga โ ยซActiveยป va ยซSpecialยป tariflar tizimlari uchun

  4 GB atigi 27 000 soโmga โ ยซActiveยป va ยซSpecialยป tariflar tizimlari uchun

  5 GB atigi 33 000 soโmga โ ยซActiveยป va ยซSpecialยป tariflar tizimlari uchun

Xizmatni boshqarish: *๏ธโฃ2๏ธโฃ5๏ธโฃ5๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="โณ Soatbay internet")
async def bot_start(message: types.Message):
    await message.answer(text="""โณ Soatbay internet:

Yirik fayllarni koโchirib olish uchun koโp trafik kerakmi?
ยซSoatbay internetยป xizmatidan foydalaning va 1 soatga 5 GB internet oling.
Faollashtirish va boshqarish:*๏ธโฃ6๏ธโฃ1๏ธโฃ6๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ Tungi internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Tungi internet-toโplamlar:

Tungi internet-toโplamlar โ bu tungi vaqtda qulay foydalanish uchun hamyonbop narxda koโp internet-trafik.
Toโplam 5 GB โ 20 000 soโm
Toโplam 20 GB โ 45 000 soโm

Xizmatdan foydalanish davri: 01:00-09:00
Xizmatning amal qilish muddati: 30 kun

Faollashtirish va boshqarish:*๏ธโฃ6๏ธโฃ1๏ธโฃ6๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="โพ Cheksiz Internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""โพ Cheksiz Internet-toโplamlar:

Ucelldan yuqori tezlikdagi 4G bilan yangi imkoniyatlar eshigini oching!
Faolashtirish: *๏ธโฃ5๏ธโฃ5๏ธโฃ5๏ธโฃ*๏ธโฃ4๏ธโฃ#๏ธโฃ
Xizmatni bekor qilish: *555*4*10*2#
Berilgan trafik limiti tugagandan soโng, Internet tezligi 64 Kb/soniyaga teng boโladi.

Xizmatni boshqarish: 
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="โ๏ธ Oylik 4G Internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""โ๏ธ Oylik 4G Internet-toโplamlar:

Ucell yangi Oylik Internet toโplamlarini taqdim qilmoqda. Toโplamlardan biriga bir marta ulaning va har 30 kunda yangi toโplamga ega boโling. Toโplamlar avtomatik tarzda belgilanadi.
Toโplamlarni faollashtirish/boshqarish: *๏ธโฃ5๏ธโฃ5๏ธโฃ5๏ธโฃ*๏ธโฃ5๏ธโฃ#๏ธโฃ
Foydalanilgan trafikni tekshirish: *555*5*10*1#
Xizmatni bekor qilish: *555*5*10*2#
Xizmat bekor qilingan holda sarflanmagan Internet-trafik qoldig'i bekor qilinadi.
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ก TAS-IX uchun internet-toโplamlar")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ก TAS-IX uchun internet-toโplamlar:

TAS-IX 8000 8000 10 000 30 kun
TAS-IX 14 000 14 000 15 000 30 kun
TAS-IX 20 000 20 000 20 000 30 kun

Xizmatni boshqarish: *๏ธโฃ6๏ธโฃ1๏ธโฃ6๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ Internet-sovgโa")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ Internet-sovgโa:

Yaqinlaringizga quvonch ulashing
Yangi yil ortda qolgan boโlsada, kayfiyat bayramona boโlib qolaveradi!
Ucellning yangi โInternet-sovgโaโ xizmati bilan hamyonbop narxda yaqinlaringizga internet-toโplam sovgโa qilib, ularni xursand etishda davom eting.

Xizmatni boshqarish: *๏ธโฃ9๏ธโฃ7๏ธโฃ9๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ฅ Mega BOOM")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ฅ Mega BOOM:

Internet foydalanuvchilari uchun ajoyib yangilik!

1 MB atigi 4,21 soโm.
Xizmatni ulash narxi: 421 soโm
Abonent toโlovi: 421 soโm kuniga
Xizmatni yoqish: *๏ธโฃ9๏ธโฃ0๏ธโฃ9๏ธโฃ#๏ธโฃ
Xizmatni oโchirish: *๏ธโฃ9๏ธโฃ0๏ธโฃ9๏ธโฃ*๏ธโฃ2๏ธโฃ#๏ธโฃ
๐ @aloqa_operatorlar_bot
""")
@dp.message_handler(text="๐ต Internet-avans")
async def bot_start(message: types.Message):
    await message.answer(text="""๐ต Internet-avans:

Internet-toโplam xarid qilish imkoniyati yoโqmi?
"Internet-avans" xizmatidan foydalaning โ 30 kun muddatga 50 MB Internet-trafik oling.
"Internet-avans" xizmatidan foydalanganlik uchun toโlov  - 1 052,5 soโm (hisobni birinchi toโldirishda 50 MB Internet-trafik qiymati bilan birga yechib olinadi).

Xizmatni boshqarish  *๏ธโฃ5๏ธโฃ1๏ธโฃ5๏ธโฃ#๏ธโฃyoki *๏ธโฃ9๏ธโฃ1๏ธโฃ1๏ธโฃ#๏ธโฃ USSD-buyrugโi orqali amalga oshiriladi.
๐ @aloqa_operatorlar_bot
""")