import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robo Speaker")

while True:
    x = input("Enter what you want me to speak: ")
    if x == "q":
        break
    engine.say(x)
    engine.runAndWait()
