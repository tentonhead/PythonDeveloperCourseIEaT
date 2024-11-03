# TODO  Напишите функцию count_letters
def calculate_letters(source):
    letters = {}
    for i in range(len(source)):
        c = source[i].lower()
        if c.isalpha():
            if letters.get(c) != None:
                letters[c] += 1
            else:
                letters[c.lower()] = 1
    return letters

# TODO Напишите функцию calculate_frequency
def calculate_frequency(occurences):
    n = sum(occurences.values())
    frequencies = occurences.copy()

    for k in frequencies.keys():
        frequencies[k] = occurences[k] / n
    return frequencies

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
counts = calculate_letters(main_str)
frequency = calculate_frequency(counts)
for k in counts:
    print(f"{k}:",  "%.2f" % round(frequency[k], 2))