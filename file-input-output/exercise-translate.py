from translate import Translator

translate = Translator(to_lang="ja")

try:
    with open("translate.txt", mode="r") as translate_file:
        text = translate_file.read()
        print(translate.translate(text))
except FileNotFoundError as err:
    print('File not exist!')
    raise err

