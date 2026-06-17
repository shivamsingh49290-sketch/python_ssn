from gtts import *
from playsound import *

text=gTTS(input("enter text"))
text.save("a.mp3")
playsound("a.mp3")
