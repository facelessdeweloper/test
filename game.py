from speakAI import *
import random
levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}
count = 0
lvl = input('Выберите уровень \n')
if lvl == 'easy':
    for i in range(3):
        random_word = random.choice(levels["easy"])
        print('Скажите', random_word)
        text = speak_eng()
        text = str(text)
        if random_word == text.lower():
            print('Правильно')
            count += 1
        else:
            print('Неправильно')
if lvl == 'medium':
    for i in range(3):
        random_word = random.choice(levels["medium"])
        print('Скажите', random_word)
        text = speak_eng()
        text = str(text)
        if random_word == text.lower():
            print('Правильно')
            count += 1
        else:
            print('Неправильно')
if lvl == 'hard':
    for i in range(3):
        random_word = random.choice(levels["hard"])
        print('Скажите', random_word)
        text = speak_eng()
        text = str(text)
        if random_word == text.lower():
            print('Правильно')
            count += 1
        else:
            print('Неправильно')
            


