import speech_recognition as  sr 


r = sr.Recognizer()
r.energy_threshold


with sr.Microphone() as source:
    print("please wait calibrating microphone ...")
    r.adjust_for_ambient_noise(source,duration=5)
    print("speak anything")
    audio = r.listen(source)
    #print(audio)

    try:   
        text = r.recognize_google(audio)
        print('you said :{}'.format(text))
    except:
        print("sorry")