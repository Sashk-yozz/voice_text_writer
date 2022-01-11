import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

engine = pyttsx3.init()

def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()

sayToMe("Привет всем! У нас все работает отлично")
sayToMe("Скажите хоть что-то")

record = sr.Recognizer()
while True:
    try:
        with sr.Microphone(device_index=1) as source:
            print("Говори..")
            audio = record. listen(source)

            result = record.recognize_google(audio, language="en-EN")
            result = result.lower()

            print(result.lower())

            if result == "скажи время":
                now = datetime.datetime.now()
                str_date = "Сейчас {}:{}".format(str(now.hour), str(now.minute))
                print(str_date)
                sayToMe(str_date)
            elif result == "открой веб-сайт":
                webbrowser.open("https://itproger.com")
            elif result == "write file":
                file = open('text.txt', 'w')
                print("Что записать в файл?")
                say_text = record.listen(source)
                result_text = record.recognize_google(say_text, language="ru-RU")
                file.write(str(result_text))
                print(result_text)
                file.close()
            elif result == "read file":
                file = open('text.txt', 'r')
                file_read = file.read()
                print(file_read)
                sayToMe(file_read)
    except sr.UnknownValueError:
        print("Голос был не распознан")
    except sr.RequestError:
        print("Что-то пошло не так")

    if result == "exit":
        break



