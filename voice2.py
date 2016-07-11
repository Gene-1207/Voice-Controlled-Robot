import speech_recognition as sr
import time
import serial
r = sr.Recognizer()
m = sr.Microphone()
def kkskaks(self, audio):
    print(u"You said {}".format(r.recognize_google(audio)).encode("utf-8"))
#ser.open();

while True:
    print("Say something!")
    with m as source: lmnas = r.listen_in_background(source,kkskaks)

