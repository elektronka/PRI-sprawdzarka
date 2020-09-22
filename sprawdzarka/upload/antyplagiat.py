
class Report:
    def __init__(self, name_surname, nr_index, count_pkt):
        self.name_surname = name_surname
        self.nr_index = nr_index
        self.count_pkt = count_pkt

    def ReadReport(self, solution):
        i = 0
        name_surname = ""
        nr_index = ""
        count_pkt = ""
        for line in solution:
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


class ProgramFile(Report):

    def get_file(self,plik1, plik2):
        file1 = open(plik1, 'r', encoding='utf8')
        file2 = open(plik2, 'r', encoding='utf8')
        return file1, file2

    def get_textlist(self, list_of_file1, list_of_file2):
        text_list1 = []
        text_list2 = []
        appeared1 = False
        appeared2 = False
        for word1 in list_of_file1:
            if word1 == '</sprawozdanie>':
                appeared1 = True
                continue
            if appeared1 == True:
                text_list1.append(word1)

        for word2 in list_of_file2:
            if word2 == '</sprawozdanie>':
                appeared2 = True
                continue
            if appeared2 == True:
                text_list2.append(word2)
        del(list_of_file1)
        del(list_of_file2)

        return text_list1, text_list2



    def get_words(self, file1, file2):
        temp1 = [[word for word in line.split(' ')] for line in file1]
        words1 = []
        for list1 in temp1:
            words1.extend(list1)
        clear_words1 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words1:
            #words1.remove(word)
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword1 = "".join(word)
            clear_words1.append(clearword1)

        temp2 = [[word for word in line.split(' ')] for line in file2]
        words2 = []
        for list2 in temp2:
            words2.extend(list2)
        clear_words2 = []
        chars = ['?', '!', ':', ';', '.', '(', ')', '\n', ',', '\t', '?\n', '!\n', '.\n', ',\n', ':\n', ';\n', '(\n', ')\n']
        for word in words2:
            #words2.remove(word)
            word = list(word)
            for i in range(len(word)):
                if word[i] in chars:
                    word[i] = ""
            clearword2 = "".join(word)
            clear_words2.append(clearword2)
        return clear_words1, clear_words2


    def check_words(self, words_list1, words_list2):
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
            #print(the_same)
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
        #print(words_list1)
        #print(words_list2)
        return words_to_check, count_of_the_same

# ustalić pokrywające się litery
    def check_the_similar_words(self, checked, list_of_words):

        positive = 0
        for word in list_of_words:
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
            #print(checked, end=' ')
            #print(word, end=' ')
            #print(first, end=' ')
            #print(this_is_not_similar, end=' ')
            #print(negative, end=' ')
            #print(positive)
        #print(positive)
        return positive



if __name__ == '__main__':

    plagiarism = ProgramFile("Bartłomiej Nowak", "434162", "15")
    file1, file2 = plagiarism.get_file()
    name_surname1, nr_index1, count_pkt1 = plagiarism.ReadReport(file1)
    name_surname2, nr_index2, count_pkt2 = plagiarism.ReadReport(file2)
    first_list, second_list = plagiarism.get_words(file1, file2)
    text_list1, text_list2 = plagiarism.get_textlist(first_list, second_list)
    if len(text_list1) != 0 and len(text_list2) != 0:
        to_check, count_of_the_same_or_similar = plagiarism.check_words(text_list1, text_list2)
        if len(text_list1) >= len(text_list2):
            for checked in to_check:
                result = plagiarism.check_the_similar_words(checked, text_list1)
                count_of_the_same_or_similar += result
            total = len(text_list1)
            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)

        else:
            for checked in to_check:
                result = plagiarism.check_the_similar_words(checked, text_list2)
                count_of_the_same_or_similar += result
            total = len(text_list2)
            plagiarism_coefficient = round(count_of_the_same_or_similar * 100 / total, 2)
        if plagiarism_coefficient >= 30:
            print("Oba teksty mają ", plagiarism_coefficient, " procent podobnych słów")
            print("Prace są podobne! Podejrzewam plagiat!!")
            print("Osoby które dopuściły się plagiatu to:")
            print(name_surname1, " o numerze indeksu ", nr_index1)
            print(name_surname2, " o numerze indeksu ", nr_index2)
        else:
            print("Oba teksty mają ", plagiarism_coefficient, " procent podobnych słów")
            print("Prace są różne! Nie stwierdzam plagiatu!!")
    else:
        print("Nie można sprawdzić plagiatu dla pustych plików")

    #xml = Report(name_surname="Bartłomiej Nowak", nr_index=434126, count_pkt=15)
    #name_surname, nr_index, count_pkt = xml.ReadReport()
    #print(name_surname, end=';')
    #print(nr_index, end=';')
    #print(count_pkt)



