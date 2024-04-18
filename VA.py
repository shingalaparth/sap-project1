import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pyjokes
import os



engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")

  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")

  else:
    speak("Good Evening!")

  speak("I am lalu Sir. Please tell me how may I help you")


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
        
        try:
          print("Recognizing...")
          query = sr.recognize_google(audio, language='en-in')
          print(f"User said: {query}\n")
    
        except Exception as e:
          print(e)
          print("Say that again please...")
          return "None"
        return query

def speechtext(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[10].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    
        if "lalu" in sptext().lower():
            wishMe()
            while True:
                data1 = sptext().lower()

                if "your name" in data1:
                 name = "my name is lalu"
                 speechtext(name)

                elif 'open stackoverflow' in data1:
                 webbrowser.open("stackoverflow.com")
                                
                elif 'wikipedia' in data1:
                    speak('Searching Wikipedia...')
                    data1 = data1.replace("wikipedia", "").strip()  # Remove "wikipedia" and any leading/trailing whitespace
                    if data1:  # Check if data1 is not empty
                            results = wikipedia.summary(data1, sentences=2)
                            speak("According to Wikipedia")
                            print(results)
                            speak(results)
                    else:
                            speak("Sorry, I didn't catch that. Could you please tell me what you want to search on Wikipedia?")

                elif "old are you" in data1:
                 age = "i am two year old"
                 speechtext(age)


                elif " your favorite color" in data1:
                 response = "As an AI, I don't have personal experiences or preferences, but I can tell you that blue is often associated with calm and stability."
                 speechtext(response)

                elif "who is your creator" in data1:
                  response = "I was created by Parth shingala"
                  speechtext(response)

                elif "time" in data1:
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtext(time)

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")
                
                elif 'google' in data1:
                    webbrowser.open("https://www.google.com/")
                
                elif 'whatsapp' in data1:
                    webbrowser.open("https://web.whatsapp.com/")
                
                elif 'google drive' in data1:
                    webbrowser.open("https://drive.google.com/")
                
                elif 'e-mail' in data1:
                    webbrowser.open("https://mail.google.com/")

                elif 'instagram' in data1:
                    webbrowser.open("https://www.instagram.com/")

                elif 'replit' in data1:
                    webbrowser.open("https://replit.com/~")

                elif 'copilot' in data1:
                    webbrowser.open("https://copilot.microsoft.com/")

                elif 'netflix' in data1:
                    webbrowser.open("https://www.netflix.com/in/")

                elif 'discord' in data1:
                    webbrowser.open("https://discord.com/")

                elif 'spotify' in data1:
                    webbrowser.open("https://open.spotify.com/")

                elif 'w3school' in data1:
                    webbrowser.open("https://www.w3schools.com/")

                elif 'amazon' in data1:
                    webbrowser.open("https://www.amazon.in/")

                elif 'gemini' in data1:
                    webbrowser.open("https://gemini.google.com/app")

                elif "joke" in data1:
                    joke_1 = pyjokes.get_joke(language="en",category="natural") 
                    print(joke_1)
                    speechtext(joke_1)

                elif "exit" in data1:
                    speechtext("thank you")
                    break


        else:
            print("thanks")






