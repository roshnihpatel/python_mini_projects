from gtts import gTTS
import os

def text_to_speech():
    '''Converts input text to speech and saves audio in a user named .mp3 file'''

    title = input("Please provide name for mp3 file: ")
    text= input("Enter text to convert to speech: ")
    tts = gTTS(text)
    tts.save(f"{title}.mp3")
    os.system(f"start {title}.mp3")


while True:
    decision = input("Do you want to convert text to speech? y/n: ")

    if decision.lower() == "y":
        text_to_speech()
    elif decision.lower() == "n":
        print("goodbye\n")
        break
    else:
        print("Not valid option, please try again\n")
        continue


