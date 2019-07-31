import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    audio = r.listen(source)
    r.listen(source, 3)

    text=r.recognize_google(audio)
    print("wat u spoke is: {}". format(text))
