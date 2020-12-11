import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wished():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")
    speak("My name is Hazel,I am Aman's personal assistant. please tell me how may i help you")


def tacoma():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'your password')
    server.sendmail('your email', to, content)
    server.close()




if __name__ == '__main__':
    wished()
    if 1:
        query = tacoma().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "E:\\CHPPP\\musc"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("sir the time is :", strTime)
            print(strTime)

        elif 'opec android studio' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio"
            os.startfile(path)

        elif 'calculation' in query:
            question = query
            app_id = 'LTHYV6-HKR9WV3HEG'
            client = wolframalpha.Client(app_id)
            res = client.query(question) 
            answer = next(res.results).text 
            print(answer)
            speak(answer)

        elif 'email to saksham' in query:
            try:
                speak("what should i say")
                content = tacoma()
                to = "to whom sent"
                sendEmail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email")
