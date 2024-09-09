# Run these commands in new terminal
# pip install pyttsx3
# pip install wikipedia

import pyttsx3 
import wikipedia

voice=pyttsx3.init()
In=input("Searching wikipedia/google: ")
result=wikipedia.summary(In,sentences=0)
print(result)
voice.say(result)
voice.runAndWait()