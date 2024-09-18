from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_word():
    url = "http://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find_all("div", id="random_word")
        word_definition = soup.find_all("div", id="random_word_definition")

        return {
            "english_word": english_word[0].text,
            "word_definition": word_definition[0].text
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def word_game():
    translator = Translator()
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_word()
        if word_dict is None:
            continue

        # Переводим слово и его определение на русский язык
        english_word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        translated_word = translator.translate(english_word, dest='ru').text
        translated_definition = translator.translate(word_definition, dest='ru').text

        print(f"Значение слова: {translated_definition}")
        user = input("Что за слово? ")

        if user.lower() == translated_word.lower():
            print("Правильно")
        else:
            print(f"Неправильно, было загадано слово: {translated_word}")

        play_again = input("Хотите сыграть еще? (*/нет): ")
        if play_again.lower() == "нет":
            print("Спасибо за игру")
            break

word_game()
