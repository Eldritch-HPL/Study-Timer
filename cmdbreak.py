# import required modules
from playsound import playsound
import time
import os
import secrets

songs = ["bell_boy.wav", "black.wav", "dance.wav", 
    "sedan.wav", "sunglasses.wav", "why.wav"]    

#main sleep/print function
def study_time():
    print("Start study or project 20 minutes\n\n")
    print("20 minutes remaining")
    time.sleep(300)
    print("15 minutes remaining")
    time.sleep(300)
    print("10 minutes remaining")
    time.sleep(300)
    print("5 minutes remaining")
    time.sleep(300)
    print("PLAY TIME!!!")
    
    # for playing random music wav file
    playme = secrets.choice(songs)
    audio_file = os.path.dirname(__file__) + '/tunes/'+ playme
    playsound(audio_file)

while True:
    more = input("Study now? Y/n:  ") or "Y"
    if more == str.upper("Y"):
        study_time()
    else:
        print("Bye!")
        break
