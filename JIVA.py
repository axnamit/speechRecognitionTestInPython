import speech_recognition as sr #pip install speechRecognition
import time
from gtts import gTTS 
import os 
from playsound import playsound
   
class MainClass:
    def chekVoice(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("hello sir..")
            time.sleep(3)
            print("please wait i,m callibrating ....")
            r.adjust_for_ambient_noise(source,duration=5)
            print("listning....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:   
            text = r.recognize_google(audio)
            if(format(text)=="hello Jarvis"):
                print("hello sir ")
                return "Hello sir"
            else:
                print('you said :{}'.format(text))
                return text
        except:
            print("sorry")
            return "sorry"
    
    def speakFun(self,textFromspeek):
        myText= "hello sir "
        laungage = 'en'
        myobj = gTTS(text=textFromspeek,lang=laungage,slow=False)
        myobj.save("hello.mp3")
        try:
            os.system("mpg321 ~/jarvis/hello.mp3")  
        except NameError:
            print(NameError)
        #os.system("~/jarvis/hello.mp3")

        


obj = MainClass()
obj.speakFun("Hello sir!  please wait ....")
test=obj.chekVoice()
if "how are you" in test:
    obj.speakFun("i am fine ")
elif "hello " in test:
    obj.speakFun("hello sir ! what can i do for you")
else:
    obj.speakFun(test)
#obj.chekVoice()
