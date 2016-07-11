import speech_recognition as sr
import time
import serial
import pyttsx
engine = pyttsx.init()
r = sr.Recognizer()
m = sr.Microphone()
ser = serial.Serial("COM9",9600)
ser.isOpen();
#ser.open();
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.record(source,2);
        print("Got it! Now to recognize it...")
        try:
            value1 = r.recognize_google(audio)
            if str is bytes:
               print(u"You said bytes -  {}".format(value1).encode("utf-8"))
            else:
                print("You said google {}".format(value1))
            if value1 == 'left':
            	value1 = '4'
            elif value1 == 'right':
            	value1 = '6'
            elif value1 == 'forward':
            	value1 = '8'
            elif value1 == 'backward':
            	value1 = '2'
            elif value1 == 'stop':
            	value1 = '5'
            elif value1 == 'buzzer on':
            	value1 = '7'
            elif value1 == 'buzzer off':
            	value1 = '9'
            elif value1 == 'hi' or value1 == 'hello':
            	engine.say('Hello User! How you doin?')
            	engine.runAndWait()
            	value1 = '5'
            elif value1 == 'peace' or value1 == 'enjoy':
            	engine.say('rest in pieces')
            	engine.runAndWait()
            	value1 = '5'
            elif value1 == 'war' or value1 == 'love':
            	engine.say('everything is fair in love and war... ')
            	engine.runAndWait()
            	value1 = '5'
            elif value1 == 'exit':
            	break
            else:
            	engine.say('Give proper inputs please!')
            	engine.runAndWait()
            	value1 = '5'
            print(value1)
            ser.write(value1)
            time.sleep(1)
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
ser.close();
