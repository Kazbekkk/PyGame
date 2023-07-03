# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12

one_points = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_points = ['Д', 'К', 'Л', 'М', 'П', 'У']
three_points = ['Б', 'Г', 'Ё', 'Ь', 'Я']
four_poinrs = ['Й', 'Ы']
five_points = ['Ж', 'З', 'Х', 'Ц', 'Ч']
eight_points = ['Ш', 'Э', 'Ю']
ten_points = ['Ф', 'Щ', 'Ъ']
word = input("Введите слово: ")
text_upper = word.upper()
count = 0
w = 0
for i in text_upper:
    i.upper
    w = count # старое значение 0
    for a in one_points:
        if a == i:
            count += 1 # новое
            break
    if count != w:
        continue
    else:
        for a in two_points:
            if a == i:
                count += 2
                break
        if count != w:
            continue
        else:
            for a in three_points:
                if a == i:
                    count += 3
                    break
            if count != w:
                continue
            else:
                for a in four_poinrs:
                    if a == i:
                        count += 4
                        break
                if count != w:
                    continue
                else:
                    for a in five_points:
                        if a == i:
                            count += 5
                            break
                    if count != w:
                        continue
                    else:
                        for a in eight_points:
                            if a == i:
                                count += 8
                                break
                        if count != w:
                            continue
                        else:
                            for a in ten_points:
                                if a == i:
                                    count += 10
                                    break

print(f"Стоимость введеннго слова '{word}' = {count}")