# we need to import this voice recognition packages bascially the python libraries ......:) 
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
r.energy_threshold=400
while True:
    with sr.Microphone() as source:
        print("Speak Anything:")
        r.adjust_for_ambient_noise(source, duration=5)
        r.dynamic_energy_threshold = True 
        audio = r.listen(source)
        #dv=r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            if(text == "hello"):
                print(" ==> Welcome to python")
            elif(text == "hello i am misal"):
                print("Invalid input ")
            else:
                print("Try again")
        except:
            print("Sorry could not recognize your voice")
            break
