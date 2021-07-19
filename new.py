import speech_recognition as sr
def recogonise():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("speak")
    input = r.listen(source)
    try:
        processed_text = r.recognize_google(input)
        print(processed_text)
        return processed_text
    except sr.UnknownValueError:
        return "Raven cannot recognise your voice"
print("Hi")
x=recogonise()
