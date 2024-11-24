import speech_recognition as sr
def speak_ru():
    # Создаем распознаватель
    recognizer = sr.Recognizer()

    # Используем микрофон в качестве источника аудио
    with sr.Microphone() as source:
        # Слушаем аудио
        audio = recognizer.listen(source)
        try:
            # Распознаем речь с определенным языком (например, 'ru-RU' для русского)
            text = recognizer.recognize_google(audio, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return
        except sr.RequestError as e:
            return
def speak_eng():
        # Создаем распознаватель
    recognizer = sr.Recognizer()

    # Используем микрофон в качестве источника аудио
    with sr.Microphone() as source:
        # Слушаем аудио
        audio = recognizer.listen(source)
        try:
            # Распознаем речь с определенным языком
            text = recognizer.recognize_google(audio, language='en-EN')
            return text
        except sr.UnknownValueError:
            return
        except sr.RequestError as e:
            return