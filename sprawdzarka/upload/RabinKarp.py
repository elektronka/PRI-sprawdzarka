def get_file(l):
    files_and_enlargement = {}
    for file in l:
        enlargement = ""
        i = len(file) - 1
        while(i >= 0):
            if file[i] == '.':
                enlargement += file[i]
                break
            enlargement += file[i]
            i = i - 1
        enlargement = list(enlargement)
        enlargement.reverse()
        enlargement = "".join([str(i) for i in enlargement])
        if enlargement == '.txt' or enlargement == '.xml':
            files_and_enlargement[file] = enlargement
    return files_and_enlargement

def ReadMetric(report):
        i = 0
        name_surname = ""
        nr_index = ""
        count_pkt = ""
        for line in report:
            if i <= 2:
                i = i + 1
                continue
            elif i >= 3 and i <= 5:
                j = 0
                was = False
                while line != "" and j < len(line):
                    if was == True:
                        break
                    if line[j] == '>':
                        j = j + 1
                        if line[j] == '<':
                            if i == 3:
                                name_surname += '-'
                            elif i == 4:
                                nr_index += '-'
                            elif i == 5:
                                count_pkt += '-'
                            break
                        was = True
                        while True:
                            if i == 3:
                                name_surname += line[j]
                            elif i == 4:
                                nr_index += line[j]
                            elif i == 5:
                                count_pkt += line[j]
                            j = j + 1
                            if line[j] == '<':
                                break
                    else:
                        j = j + 1
            elif i > 5:
                break
            i = i + 1
        return name_surname, nr_index, count_pkt

def get_words(file1, file2):
        temp1 = [[word for word in line.split(' ')] for line in file1]
        words1 = []
        for list1 in temp1:
            if list1[0] == '\n' or list1[0] == 'Zadanie':
                continue
            words1.extend(list1)
        clear_words1 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words1:
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword1 = "".join(word)
            clear_words1.append(clearword1)

        temp2 = [[word for word in line.split(' ')] for line in file2]
        words2 = []
        for list2 in temp2:
            if list2[0] == '\n' or list2[0] == 'Zadanie':
                continue
            words2.extend(list2)
        clear_words2 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words2:
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword2 = "".join(word)
            clear_words2.append(clearword2)
        return clear_words1, clear_words2

def get_textlist( list_of_file1, list_of_file2):
    text_list1 = []
    text_list2 = []
    appeared1 = False
    appeared2 = False
    for word1 in list_of_file1:
        if word1 == '</sprawozdanie>':
            appeared1 = True
            continue
        if appeared1 == True and word1 != '':
            text_list1.append(word1)
    for word2 in list_of_file2:
        if word2 == '</sprawozdanie>':
            appeared2 = True
            continue
        if appeared2 == True and word2 != '':
            text_list2.append(word2)
    del(list_of_file1)
    del(list_of_file2)
    return text_list1, text_list2

def remove_repeat( text1, text2):
        not_repeat1 = []
        not_repeat2 = []
        for word1 in text1:
            if word1 not in not_repeat1:
                not_repeat1.append(word1)
            else:
                continue
        for word2 in text2:
            if word2 not in not_repeat2:
                not_repeat2.append(word2)
            else:
                continue
        return not_repeat1, not_repeat2

def check_words( words_list1, words_list2):
        if len(words_list1) >= len(words_list2):
            the_same = []
            words_to_check = []
            for w in words_list2:
                checked = w
                if checked in words_list1:
                    the_same.append(checked)
                else:
                    i = 0
                    while i < len(words_list1):
                        if abs(len(checked) - len(words_list1[i])) > 0 and abs(len(checked) - len(words_list1[i])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            i = i + 1
        else:
            the_same = []
            words_to_check = []
            for w in words_list1:
                checked = w
                if checked in words_list2:
                    the_same.append(checked)
                else:
                    j = 0
                    while j < len(words_list2):
                        if abs(len(checked) - len(words_list2[j])) > 0 and abs(len(checked) - len(words_list2[j])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            j = j + 1
        count_of_the_same = len(the_same)
        return words_to_check, count_of_the_same

def check_words( words_list1, words_list2):
        if len(words_list1) >= len(words_list2):
            the_same = []
            words_to_check = []
            for w in words_list2:
                checked = w
                if checked in words_list1:
                    the_same.append(checked)
                else:
                    i = 0
                    while i < len(words_list1):
                        if abs(len(checked) - len(words_list1[i])) > 0 and abs(len(checked) - len(words_list1[i])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            i = i + 1
        else:
            the_same = []
            words_to_check = []
            for w in words_list1:
                checked = w
                if checked in words_list2:
                    the_same.append(checked)
                else:
                    j = 0
                    while j < len(words_list2):
                        if abs(len(checked) - len(words_list2[j])) > 0 and abs(len(checked) - len(words_list2[j])) <= 3:
                            words_to_check.append(checked)
                            break
                        else:
                            j = j + 1
        count_of_the_same = len(the_same)
        return words_to_check, count_of_the_same

def check_the_similar_words( checked, list_of_words):
        positive = 0
        if checked.isdigit() == False: #nie porównuj podobieństwa liczb pomiędzy sobą
            for word in list_of_words:
                if word.isdigit() == True:
                    continue
                if len(checked) <= len(word):
                    length = len(checked)
                elif len(checked) > len(word):
                    length = len(word)
                i = 0
                negative = 0
                first = False
                is_already_negative = False
                this_is_not_similar = False
                while i < length:
                    if i == 0 and checked[0].lower() == word[0].lower():
                        first = True
                        i = i + 1
                        continue
                    if checked[i] == word[i] and negative <= 3:
                        if not is_already_negative == True:
                            i = i + 1
                        else:
                            this_is_not_similar = True
                            break
                    elif checked[i] == word[i] and negative > 3:
                        this_is_not_similar = True
                        break
                    elif checked[i] != word[i] and negative <= 3:
                        is_already_negative = True
                        negative += 1
                        i = i + 1
                    elif checked[i] != word[i] and negative > 3:
                        this_is_not_similar = True
                        negative += 1
                        break
                negative += abs(len(checked) - len(word))
                if negative <= 3 and first == True and this_is_not_similar == False:
                    positive = positive + 1
            return positive
        else:
            return positive

def Rabin_Karp_algorithm(pat, txt, q):
        if (type(pat) is str) and (type(txt) is str) and (type(q) is int):
            M = len(pat)
            N = len(txt)
            i = 0
            j = 0
            p = 0  # wartość hasha dla wzoru
            t = 0  # wartość hasha dla tekstu
            h = 1
            d = 256
            similars = []

            # Wartość h powinna mieć wartość 'pow(d, M-1) % q'
            for i in range(M - 1):
                h = (h * d) % q

            # Przelicz wartość hasha wzoru i hasha pierwszego podciągu tekstu
            for i in range(M):
                p = (d * p + ord(pat[i])) % q
                t = (d * t + ord(txt[i])) % q

            # Przeglądaj wzór w tekście jeden po drugim
            for i in range(N - M + 1):  # Sprawdź wartości hash dla obecnego tekstu i wzoru
                if p == t:  # jeśli wartość hasha pasuje wtedy tylko sprawdź dla każdego znaku z osobna
                    for j in range(M):  # Sprawdź znak po znaku
                        if txt[i + j] != pat[j]:
                            break
                    j += 1
                    if j == M:
                        similars.append(i)
                if i < N - M:  # Przelicz wartość hasha dla kolejnego tekstu
                    t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                    if t < 0:  # Możemy mieć wartość ujemną t. Konwertujemy na dodatnią
                        t = t + q
            return similars
        else:
            raise Exception("Co najmniej jeden parametr jest niepoprawny")

