import speech_recognition as sr
import time
import serial
import pyttsx
from library import library
import random
engine = pyttsx.init()
r = sr.Recognizer()
m = sr.Microphone()
#ser = serial.Serial("COM9",9600)
#ser.isOpen()
mode_value = {"interactive":3 , "command":1.7}
mode = "none"

def interactive():
	global r,m,engine,mode,mode_value,library
	ran = random.randint(0,100);
	engine.say("Interactive Mode. On")
	engine.say(library[mode][ran % len(library[mode])])
	engine.runAndWait()
	print("\n------IN INTERACTIVE MODE------\n")
	while mode == "interactive":
		ran = random.randint(0,100)
		print("Talk To Me...")
		with m as source: audio = r.record(source,mode_value[mode])
		try:
			value =  r.recognize_google(audio)
			if((value == "hi") or ("hello" in value) or ("greeting" in value) or (("what" in value) and ("up" in value)) or ("sup" in value) or ("hey" in value)):
				engine.say(library["greeting"][ran % len(library["greeting"])])
				engine.runAndWait();
			elif((value == "exit") or (value == "quit") or ((("exit" in value and "mode" in value) or ("quit" in value and "mode" in value)))):
				mode = "none"
			elif("command" in value):
				mode = "command"
			else:
				engine.say("Did You say, '"+ value + "'")
				engine.say(library['errorIn'][ran % len(library['errorIn'])])
				engine.runAndWait()
		except sr.UnknownValueError:
			print("Oops! Didn't catch that")
		except sr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e)) 
	if(mode == "command"):
		command()
def command():
	global r,m,engine,mode,mode_value,library
	ran = random.randint(0,100);
	engine.say("Command Mode. On")
	engine.say(library[mode][ran % len(library[mode])])
	engine.runAndWait()
	print("\n-----WILL FOLLOW YOUR COMMAND-----\n")
	while mode == "command":
		ran = random.randint(0,100);
		print("Tell me The Command...")
		with m as source: audio = r.record(source,mode_value[mode])
		try:
			value =  r.recognize_google(audio)
			if(value == "exit" or value == "quit" or (("exit" or "quit") and "mode" in value)):
				mode = "none"
			elif("interact" in value):
				mode = "interactive"
			else:
				engine.say("'" + value +"', is a false command")
				engine.runAndWait()
		except sr.UnknownValueError:
			pass
		except sr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
	if(mode == "interactive"):
		interactive()
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Please Choose The mode :\n1)Interactive Mode\n2)Command Mode\nSay 'exit' to exit the program");
    while True:
        print("Say something!")
        with m as source: audio = r.record(source,3)
        print("Got it! Now to recognize it...")
        try:
        	value =  r.recognize_google(audio)
        	ran = random.randint(0,100);
        	if((value == "hi") or ("hello" in value) or ("greeting" in value) or (("what" in value) and ("up" in value)) or ("sup" in value) or ("hey" in value)):
        		engine.say(library["greeting"][ran % len(library["greeting"])])
        		engine.runAndWait()
        	elif(("mode" in value) or ("interact" in value) or ("command" in value)):
        		value = value.split(" ");
        		for v in value:
        			if("interact" in v):
        				mode = "interactive"
        				interactive()
        				break
        			if("command" in v):
        				mode = "command"
        				command()	
        				break
        	elif(value == "exit"):
        		break
        	else:
        		engine.say("The Command, '"+value+ "', is not recognised!")
        		engine.say("Please Try Again!")
        		engine.runAndWait();
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass
#ser.close();
