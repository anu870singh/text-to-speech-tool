import pyttsx3

engine = pyttsx3.init()
text = input("Kuch likhiye jo bulwana chahte hain: ")
engine.say(text)
engine.runAndWait()
