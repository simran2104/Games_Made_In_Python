import speech_recognition as sr
Audio_file=("Speech.wav")
r=sr.Recognizer()

with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)

try:
    print("audio files contains:   \n"+ r.recognize_google(audio))
except:
    print("Failed")
    
'''except sr.UnkownValueError:
    print("Google Speech Recognition could not inderstand audio")
except sr.RequestError:
    print("Couldn't get the results from google speech recognition")'''


