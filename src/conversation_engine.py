
import gtts
import speech_recognition as sr
import os 
from gtts import gTTS
from translate import Translator
from playsound import playsound

class ConversationEngine:
    def __init__(self, lang="nl", translate_lang="es"):
        self.rec_lang = lang
        self.from_lang = lang
        self.to_lang = translate_lang
        self.translator= Translator(from_lang=lang, to_lang=translate_lang)
        self.r = sr.Recognizer()
        
    def tranlate_speech(self):
        with sr.Microphone() as source:
            self.r.energy_threshold = 4000
            self.r.adjust_for_ambient_noise(source)
            print('Speak:')
            audio = self.r.listen(source)
            
            try:
                recognize_lang = ""
                if self.rec_lang == "nl":
                    recognize_lang = "nl-NL"
                elif self.rec_lang == "es":
                    recognize_lang = "es-MX"
                else:
                    print('Invalid language: {}'.format(recognize_lang))
                    return
                 
                print('Selected language {}'.format(recognize_lang))
                text = self.r.recognize_google(audio, language=recognize_lang)
                print('You said : {}'.format(text))
                mytext = self.translator.translate(text)
                print('Translate : {}'.format(mytext))
                # Language in which you want to convert 
                # Passing the text and language to the engine,  
                # here we have marked slow=False. Which tells  
                # the module that the converted audio should  
                # have a high speed 
                myobj = gTTS(text=mytext, lang=self.to_lang, slow=False) 
                  
                # Saving the converted audio in a mp3 file named 
                myobj.save("temp.mp3") 
                # # Playing the converted file 
                playsound("temp.mp3")
                # delete temporary file
                os.remove("temp.mp3")
            except Exception as e:
                print('Sorry couldnt recognize your voice:' + str(e))
                
    def speak(self, text):
        myobj = gTTS(text=text, lang=self.rec_lang, slow=False) 

        # Saving the converted audio in a mp3 file named 
        myobj.save("temp.mp3") 
        # # Playing the converted file 
        playsound("temp.mp3")
        # delete temporary file
        os.remove("temp.mp3")
        
    def listen(self):
        with sr.Microphone() as source:
            self.r.energy_threshold = 4000
            self.r.adjust_for_ambient_noise(source)
            print('Speak:')
            audio = self.r.listen(source)
            
            try:
                recognize_lang = ""
                if self.rec_lang == "nl":
                    recognize_lang = "nl-NL"
                elif self.rec_lang == "es":
                    recognize_lang = "es-MX"
                else:
                    print('Invalid language: {}'.format(recognize_lang))
                    return
                 
                print('Selected language {}'.format(recognize_lang))
                text = self.r.recognize_google(audio, language=recognize_lang)
                print('You said : {}'.format(text))
                mytext = self.translator.translate(text)
                print('Translate : {}'.format(mytext))
            except Exception as e:
                print('Sorry couldnt recognize your voice:' + str(e))

