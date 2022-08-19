from gtts import gTTS
import os

text_language = input("Text_Language(ing/tr?): ")

text = input("Text: ")

if text_language.lower() == "ing" :
    tts = gTTS(text=text, lang="en")
    tts.save("voice_ing_text.mp3")
    os.system("voice_ing_text.mp3")
else:
    tts = gTTS(text=text, lang= "tr")
    tts.save("voice_tr_text.mp3")
    os.system("voice_tr_text.mp3")