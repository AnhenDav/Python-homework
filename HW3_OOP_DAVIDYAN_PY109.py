class Analyser:

    def __init__(self):
        self.phrase = input('Введите значение:')

    def len_phrase(self):
        return len(self.phrase)

    def analysis(self):
        vowels = 0
        vowels_str = ''
        consonants = 0
        consonants_str = ''
        all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        even = 0
        odd = 0
        num_list = []


        list_phrase = self.phrase.split()
        for i in list_phrase:
            if i.isdigit():
                i = int(i)
                while i > 0:
                    num_list.append(i % 10)
                    i = i // 10
                for num in num_list:
                    if num % 2 == 0:
                        even += num
                    else:
                        odd += num
                print('Результат по числу (произведение чётных на длину строки):', even * self.len_phrase())

            elif i.isalpha():
                i = str(i)
                for letter in i:
                    letter = letter.lower()
                    if letter in all_vowels:
                        vowels += 1
                        vowels_str += letter + ' '
                    else:
                        consonants += 1
                        consonants_str += letter + ' '
        if vowels * consonants <= self.len_phrase():
            print('Результат по строке (все гласные буквы в предложении):', vowels_str)
        else:
            print('Результат по строке (все негласные буквы в предложении):', consonants_str)




v = Analyser()
v.analysis()
