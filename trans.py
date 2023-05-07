import googletrans
import playsound
import time
translator = googletrans.Translator()
word = input("Enter Word: ")
print(googletrans.LANGUAGES)
lang = input('Choose Langugue Use That: ')
translated = translator.translate(word,dest=lang)
final = print(translated.text)
time.sleep(10)