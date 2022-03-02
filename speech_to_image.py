import speech_recognition as sr
import pyttsx3
from pathlib import Path
from PIL import Image

r = sr.Recognizer()

def SpeakText(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.1)
			audio2 = r.listen(source2)
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say "+MyText)
			SpeakText(MyText)
            
my_file = Path(f"/home/solicitous/Downloads/python/images/{MyText}.jpeg")
if my_file.is_file():
    im = Image.open(f"/home/solicitous/Downloads/python/images/{MyText}.jpeg")
    im.show()
else:
    print('file not found')            
        