import speech_recognition as spr
import pyttsx3
from googletrans import Translator
from gtts import gTTS 
import os

recog1 = spr.Recognizer()
recog2 = spr.Recognizer()
#print(spr.Microphone.list_microphone_names())
engine = pyttsx3.init()

mic = spr.Microphone(device_index=0)

with mic as source:
    print("Say HELLO to initiate Translator")
    print("----------------------------------")
    audio = recog1.listen(source)

    if 'hello' in recog1.recognize_google(audio):
        recog1 = spr.Recognizer()
        translator = Translator()
        from_lang = 'en'
        to_lang = 'hi'
        print("Speak your sentence now...")
        audio = recog2.listen(source)
        get_sentence = recog2.recognize_google(audio)

        try:
             get_sentence = recog2.recognize_google(audio)
             print("Sentence to be translated:" + get_sentence)
             text2trans = translator.translate(get_sentence, src=from_lang,dest=to_lang)
             text = text2trans.text
             speak = gTTS(text=text, lang=to_lang,slow=False)
             speak.save("voice.mp3")
             os.system("start voice.mp3")
            #  engine.say(speak)
            #  engine.runAndWait()
             
        except spr.UnknownValueError:
             print("Unable to understand")
        except spr.RequestError as e:
            print("Unable to get required output".format(e))    