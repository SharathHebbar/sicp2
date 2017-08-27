# importing python module
from gtts import gTTS
import os

# Create an instance

tts = gTTS(text = "INSERT MESSAGE WHAT COMPUTER TO SPEAK", lang= 'en')

  ## Supported Languages (lang = 'Your language')
""" 
    *  af' : 'Afrikaans'
    * 'sq' : 'Albanian'
    * 'ar' : 'Arabic'
    * 'hy' : 'Armenian'
    * 'bn' : 'Bengali'
    * 'ca' : 'Catalan'
    * 'zh' : 'Chinese'
    * 'zh-cn' : 'Chinese (Mandarin/China)'
    * 'zh-tw' : 'Chinese (Mandarin/Taiwan)'
    * 'zh-yue' : 'Chinese (Cantonese)'
    * 'hr' : 'Croatian'
    * 'cs' : 'Czech'
    * 'da' : 'Danish'
    * 'nl' : 'Dutch'
    * 'en' : 'English'
    * 'en-au' : 'English (Australia)'
    * 'en-uk' : 'English (United Kingdom)'
    * 'en-us' : 'English (United States)'
    * 'eo' : 'Esperanto'
    * 'fi' : 'Finnish'
    * 'fr' : 'French'
    * 'de' : 'German'
    * 'el' : 'Greek'
    * 'hi' : 'Hindi'
    * 'hu' : 'Hungarian'
    * 'is' : 'Icelandic'
    * 'id' : 'Indonesian'
    * 'it' : 'Italian'
    * 'ja' : 'Japanese'
    * 'km' : 'Khmer (Cambodian)'
    * 'ko' : 'Korean'
    * 'la' : 'Latin'
    * 'lv' : 'Latvian'
    * 'mk' : 'Macedonian'
    * 'no' : 'Norwegian'
    * 'pl' : 'Polish'
    * 'pt' : 'Portuguese'
    * 'ro' : 'Romanian'
    * 'ru' : 'Russian'
    * 'sr' : 'Serbian'
    * 'si' : 'Sinhala'
    * 'sk' : 'Slovak'
    * 'es' : 'Spanish'
    * 'es-es' : 'Spanish (Spain)'
    * 'es-us' : 'Spanish (United States)'
    * 'sw' : 'Swahili'
    * 'sv' : 'Swedish'
    * 'ta' : 'Tamil'
    * 'th' : 'Thai'
    * 'tr' : 'Turkish'
    * 'uk' : 'Ukrainian'
    * 'vi' : 'Vietnamese'
    * 'cy' : 'Welsh'
"""

# Saving mp3 file

tts.save("YourFileName.mpg")

# Activating text to speech 
# IF YOU DO NOT HAVE  mp321 command in your raspbian, enter following code bellow
# sudo apt-get install mpg321

os.system("mpg321 YourFileName.mpg")
