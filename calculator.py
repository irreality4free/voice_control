import speech_recognition as sr
import os
import re
from pygame import mixer
import datetime
import time
from gtts import gTTS
import sympy


def ListenMe():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-нибудь")
        audio = r.listen(source)

    try:
         print(r.recognize_google(audio, language="ru-RU"))
         return r.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        print("Робот не расслышал фразу")
        return "Я не понимаю, я тупое"
    except sr.RequestError as e:
        print("Ошибка сервиса; {0}".format(e))
        return "Ошибка сервиса"



def Speak(some_text):
    # Для того чтобы не возникало коллизий при удалении mp3 файлов
    # заведем переменную mp3_nameold в которой будем хранить имя предыдущего mp3 файла
    mp3_nameold = '111'
    mp3_name = "1.mp3"

    # Инициализируем звуковое устройство
    mixer.init()

    # Открываем файл с текстом и по очереди читаем с него строки в ss

    ss = some_text

    # Делим прочитанные строки на отдельные предложения
    split_regex = re.compile(r'[.|!|?|…]')
    sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(ss)])

    # Перебираем массив с предложениями
    for x in sentences:
        if (x != ""):
            print(x)
            # Эта строка отправляет предложение которое нужно озвучить гуглу
            tts = gTTS(text=x, lang='ru')
            # Получаем от гугла озвученное предложение в виде mp3 файла
            tts.save(mp3_name)
            # Проигрываем полученный mp3 файл
            mixer.music.load(mp3_name)
            mixer.music.play()
            while mixer.music.get_busy():
                time.sleep(0.1)
            # Если предыдущий mp3 файл существует удаляем его
            # чтобы не захламлять папку с приложением кучей mp3 файлов
            if (os.path.exists(mp3_nameold) and (mp3_nameold != "1.mp3")):
                os.remove(mp3_nameold)
            mp3_nameold = mp3_name
            # Формируем имя mp3 файла куда будет сохраняться озвученный текст текущего предложения
            # В качестве имени файла используем текущие дату и время
            now_time = datetime.datetime.now()
            mp3_name = now_time.strftime("%d%m%Y%I%M%S") + ".mp3"

        # Читаем следующую порцию текста из файла


    # Закрываем файл


    # Устанвливаем текущим файлом 1.mp3 и закрываем звуковое устройство
    # Это нужно чтобы мы могли удалить предыдущий mp3 файл без колизий
    mixer.music.load('1.mp3')
    mixer.stop
    mixer.quit

    # Удаляем последний предыдущий mp3 файл
    if (os.path.exists(mp3_nameold)):
        os.remove(mp3_nameold)


def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
        "девять", "десять", "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
        "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать",
      ]

      tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдеся", "семьдесят", "восемьдесят", "девяносто"]
      thondreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

      scales = [ "тысяча", "миллион", "миллиард", "триллион"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(thondreds):     numwords[word] = (1, idx * 100)
      for idx, word in enumerate(scales):   numwords[word] = (10*10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def calc():
    phraze = ListenMe()
    phraze =phraze.replace("плюс", "+")
    phraze =phraze.replace("x", "*")
    phraze =phraze.replace("х", "*")
    phraze =phraze.replace("X", "*")
    phraze =phraze.replace("минус", "-")
    phraze =phraze.replace("разделить", "/")
    phraze =phraze.replace("умножить", "*")
    phraze =phraze.replace("две", "2")
    phraze =phraze.replace("одна тысяча", "1")
    phraze =phraze.replace("один миллион", "1")
    phraze =phraze.replace("один million", "1")
    phraze =phraze.replace("одна", "")
    phraze =phraze.replace("тысяча", "1")
    phraze =phraze.replace("миллион", "1")
    phraze =phraze.replace("million", "1")
    phraze =phraze.replace("тысяч", "")
    phraze =phraze.replace("тысячи", "")
    phraze =phraze.replace("миллиона", "")
    phraze =phraze.replace("миллионов", "")
    phraze =phraze.replace('на','')
    phraze =phraze.replace('один','1')
    phraze =phraze.replace('два','2')
    phraze =phraze.replace('три','3')
    phraze =phraze.replace('четыре','4')
    phraze =phraze.replace('пять','5')
    phraze =phraze.replace('шесть','6')
    phraze =phraze.replace('семь','7')
    phraze =phraze.replace('восемь','8')
    phraze =phraze.replace('девять','9')
    phraze =phraze.replace('десять','10')
    phraze =phraze.replace('десять','11')
    phraze =phraze.replace('двенадцать','12')
    phraze =phraze.replace('тринадцать','13')
    phraze =phraze.replace('четырнадцать','14')
    phraze =phraze.replace('пятнадцать','15')
    phraze =phraze.replace('шестнадцать','16')
    phraze =phraze.replace('семнадцать','17')
    phraze =phraze.replace('восемнадцать','18')
    phraze =phraze.replace('девятнадцать','19')
    phraze =phraze.replace('двадцать','2')
    phraze =phraze.replace('тридцать','3')
    phraze =phraze.replace('сорок','4')
    phraze =phraze.replace('пятьдесят','5')
    phraze =phraze.replace('шестьдесят','6')
    phraze =phraze.replace('семьдесят','7')
    phraze =phraze.replace('восемьдесят','8')
    phraze =phraze.replace('девяносто','9')
    phraze =phraze.replace('сто','1')
    phraze =phraze.replace('двести','2')
    phraze =phraze.replace('триста','3')
    phraze =phraze.replace('четыреста','4')
    phraze =phraze.replace('пятьсот','5')
    phraze =phraze.replace('шестьсот','6')
    phraze =phraze.replace('семьсот','7')
    phraze =phraze.replace('восемьсот','8')
    phraze =phraze.replace('девятьсот','9')
    phraze =phraze.replace("1million", "1")
    phraze =phraze.replace(" ", "")
    print (phraze)
    Speak (str(eval(str(phraze))).replace('.', '. точка'))

calc()
