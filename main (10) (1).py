import json
import math
import datetime
from datetime import datetime
import os
from colorama import init, Fore, Back, Style
from collections import Counter
import random
class Singleton:
    def print_s(self, text):
        self.log += "Бот : " + str(text) + '\n'
        print(Fore.YELLOW + str(text) + Style.RESET_ALL)

    def bark(self):
        t = random.random()
        if 0.05 <= t and t <= 0.10:
            self.print_s("Чудовий вибір!")
        elif 0.35 < t and t <= 0.40:
            self.print_s("Ех, знов те саме")
        elif 0.65 < t and t <= 0.70:
            self.print_s("Що ж, давайте порахуємо!")
    
    def input_s(self, prompt, menu):
        self.log += "Користувач : "
        print(prompt)
        ans = input(Fore.GREEN + "")
        self.log += ans + '\n'
        if ans.lower() == "вихід":
            path_ = self.config["Путь"]
            if os.path.exists(path_):
                with open(path_, "a") as file:
                    file.writelines(self.log)
                f.close()
            else:
                with open(path_, "w") as file:
                    file.writelines(self.log)
                f.close()
            path_ = "dialog - " + str(datetime.now())
            with open(path_, "w") as file:
                file.writelines(self.log)
            f.close()
            quit()
        elif ans.lower() == "назад":
            if menu == "main":
                self.main_menu()
            else:
                self.sub_menu(menu)
        elif ans.lower() == "допомога":
            self.print_s("Щоб вийти з програми, введіть \"вихід\". Щоб повернутися у попереднє меню, введіть \"назад\"")
        else:            
            return ans

    def sub_menu(self, theme):
        self.print_s(f'Я можу допомогти з наступними питаннями у темі {theme}: ')
        while True:
            fl = 0
            for item in self.config['Теми'][theme]:
                self.print_s(item['Назва'])                
            ans = self.input_s(Fore.GREEN + "", "main")
            if ans in self.config['Список тем']:
                self.sub_menu(ans)
            data = self.config['Теми'][theme]
            for items in data:
                if ans in items['Назва']:
                    fl = 1
                    self.print_s(f'Ви обрали тему {ans}')
                    self.bark()
                    getattr(globals()['Singleton'], items['Функція'])(self, theme)
            if fl == 0:
                self.print_s("Нажаль, я не знаю цієї теми або підтеми. Натомість, я можу домогти на такі основні теми:")
                for items in self.config['Список тем']:
                    self.print_s(items)
            
            
    def validate_float(self, theme, value, positive=None):
        f = 0
        ans = 0
        self.print_s(f'Введіть значення для {value}')
        while f != 1:
            ans = self.input_s("", theme)
            try:
                ans = float(ans)
                f = 1
                if positive is not None and f < 0:
                    self.print_s("Введіть значення більше 0!")
                    f = 0
                
            except ValueError: 
                self.print_s("Введіть корректне значення!")
        return ans
    def main_menu(self):
        ans = ""
        self.print_s("Оберіть тему: ")
        while True:
            for item in self.config['Список тем']:
                self.print_s (item)
            ans = self.input_s("", "main")
            if ans not in self.config['Список тем']:
                self.print_s("Будь ласка, перевірте правильність вводу!")
                continue
            self.print_s("Ви обрали тему \"" + ans + "\"")
            self.bark()
            self.sub_menu(ans)

    def __init__(self, config, log):
        self.log = log
        self.config = config
    
    def lec(self, theme):
        self.print_s("Який тип енергїї ви хочете знайти?")
        self.print_s("1. Кінетична")
        self.print_s("2. Потенціальна")
        self.print_s("3. Внутрішня")
        Ek = 0
        Ep = 0
        Ei = 0
        const = 0
        ans = self.validate_float(theme, "тип енергії")
        while ans > 4 or ans < 0:
            ans = self.validate_float(theme, "Оберіть тип енергії (від 1 до 3)")
        if ans == 1:
            Ep = self.validate_float(theme, "Ep")
            Ei = self.validate_float(theme, "Ei")
            const = self.validate_float(theme, "const")
            self.print_s(f'Відповідь - {const - Ep - Ei}')
        elif ans == 2:
            Ek = self.validate_float(theme, "Ek")
            Ei = self.validate_float(theme, "Ei")
            const = self.validate_float(theme, "const")
            self.print_s(f'Відповідь - {const - Ek - Ei}')
        else:
            Ek = self.validate_float(theme, "Ek")
            Ep = self.validate_float(theme, "Ep")
            const = self.validate_float(theme, "const")
            self.print_s(f'Відповідь - {const - Ek - Ep}')

    def coulon(self, theme):
        k =  self.validate_float(theme, "f")
        q1 = self.validate_float(theme, "q1")
        q2 = self.validate_float(theme, "q2")
        r =  self.validate_float(theme, "r")
        F = k * (q1* q2) / (r**2) 
        self.print_s(f'Відповідь F = {F}')
    
    def stef_bol(self, theme):
        sigma = self.validate_float(theme, "sigma")
        A = self.validate_float(theme, "A")
        T = self.validate_float(theme, "T")
        P = sigma * A * T**4
        self.print_s(f'Відповідь P = {P}')

    def grav_const(self, theme):
        self.print_s("Відповідь 6.67384(80)e-11")

    def length(self, theme):
        x1 = self.validate_float(theme, "x1")
        y1 = self.validate_float(theme, "y1")
        x2 = self.validate_float(theme, "x2")
        y2 = self.validate_float(theme, "x2")
        ans = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        self.print_s(f'Відповідь AB = {ans}')

    def s_triangle(self, theme):
        b = self.validate_float(theme, "b", positive=True)
        h = self.validate_float(theme, "h", positive=True)
        S = 0.5 * b * h
        self.print_s(f'Відповідь S = {S}')

    def s_trapezoid(self, theme):
        a = self.validate_float(theme, "a", positive=True)
        b = self.validate_float(theme, "b", positive=True)
        h = self.validate_float(theme, "h", positive=True)
        S = 0.5 * (a + b) * h
        self.print_s(f'Відповідь S = {S}')

    def pi(self, theme):
        self.print_s(math.pi)

    def bgst_pop(self, theme):
        self.print_s("Шанхай")
    
    def count_longest(self, theme):
        i, o = self.io_path(theme)
        with open(i, 'r') as file:
            content = file.read()
            file.close()
            words = content.split()
            words.sort(key=lambda x: len(x), reverse=True)
            longest_words = words[:10]
        with open(o, "w") as file:
            for word in longest_words:
                file.write(word + "\n")
            file.close()

    def palindrom(self, theme):
        i, o = self.io_path(theme)
        with open(i, "r", encoding="utf-8") as file:
            content = file.read()
            words = content.split()
            palindrome_words = [word for word in words if word.lower() == word.lower()[::-1]]
        with open(o, "w") as file:
                for word in palindrome_words:
                    file.write(word + '\n')
        file.close()

    def count_most_used(self, theme):
        i, o = self.io_path(theme)
        with open(i, "r", encoding="utf-8") as file:
            content = file.read()
        text = content.replace(" ", "").lower()
        letter_counts = {}
        for letter in text:
            if letter.isalpha():
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
        most_used_letter = max(letter_counts, key=letter_counts.get)
        count = letter_counts[most_used_letter]
        with open(o, "w") as file:
            file.write(f'{most_used_letter} : {count}')

    def count_no_vowels(self, theme):
        i, o = self.io_path(theme)
        with open(i, "r", encoding="utf-8") as file:
            content = file.read()
        words = content.split()
        def has_vowels(word):
            vowels = "aeiou"
            return any(vowel in word.lower() for vowel in vowels)
        filtered_words = [word for word in words if len(word) > 0 and not has_vowels(word)]
        longest_words = [word for word in filtered_words if len(word) == len(max(filtered_words, key=len))]
        with open(o, "w") as file:
            for word in longest_words:
                file.write(word + '\n')

    def io_path(self, theme):
        in_ = self.input_s("Введіть шлях до файлу вводу:", theme)
        out_ = self.input_s("Введіть шлях до файлу виводу", theme)
        return in_, out_

    def count_uniq(self, theme):
        i, o = self.io_path(theme)
        with open(i, "r", encoding="utf-8") as file:
            content = file.read()
        words = content.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        unique_words = [word for word, count in word_counts.items() if count == 1]
        f = open(o, "w")
        for word in unique_words:
            f.write(word + " ")
        file.close()
        f.close()

    def year(self, theme):
        self.print_s(f'Зараз {datetime.datetime.now().year} рік')

    def portugal(self, theme):
        self.print_s("Столиця Португілії - Лісабон")

    def titanic(self, theme):
        self.print_s("Тітаник затонув у 1912 році")

    def sheqspir(self, theme):
        self.print_s("Уільям Шекспір народився 26 квітня 1564 року.")
    
    def beetles(self, theme):
        self.print_s("\"Бітлз\" відправилися у США у 1964 році.")

    def can(self, theme):
        self.print_s("Консервну банку було винайдено у 1810 році.")

    def argentum(self, theme):
        self.print_s("Хімічний символ для срібла - Ag.")

    def days_until_new_year(self, theme):
        now = datetime.datetime.now()
        current_year = now.year
        new_year = datetime.datetime(current_year + 1, 1, 1)
        time_difference = new_year - now
        self.print_s(f'До нового року {time_difference} днів')

    def text(self, theme):
        who = "Хто?"
        where = "Де?"
        when = "Коли?"
        why = "Нащо?"
        what = "Що?"
        text1 = f'{when} у {where} відбулась зустріч з {who}, який зробив {what} для того щоб {why}'
        text2 = f'{who} зробив {what} і {why} це було зроблено, і {where} та це сталося {when}'
        text3 = f'{when} і {where} відбудеться подія, на яку {who} запрошений зробити {what} для {why}'
        text4 = f'В {where} {who} займається {what}, щоб {why} і це зазвичай відбувається {when}'
        text5 = f'{when} і {where} відбувається подія, на який {who} має зробити {what} задля {why}'
        self.print_s("1  " + text1)
        self.print_s("2  " + text2)
        self.print_s("3  " + text3)
        self.print_s("4  " + text4)
        self.print_s("5  " + text5)
        ans = self.validate_float(theme, "номеру тексту")
        while ans >= 6 or ans <= 0:
            ans = self.validate_float(theme, "Оберіть номер тексту (від 1 до 5)")
        who = self.input_s("Хто?", theme)
        where = self.input_s("Де?", theme)
        when = self.input_s("Коли?", theme)
        why = self.input_s("Нащо?", theme)
        what = self.input_s("Що?", theme)
        text1 = f'{when} у {where} відбулась зустріч з {who}, який зробив {what} для того щоб {why}'
        text2 = f'{who} зробив {what} і {why} це було зроблено, і {where} та це сталося {when}'
        text3 = f'{when} і {where} відбудеться подія, на яку {who} запрошений зробити {what} для {why}'
        text4 = f'В {where} {who} займається {what}, щоб {why} і це зазвичай відбувається {when}'
        text5 = f'{when} і {where} відбувається подія, на який {who} має зробити {what} задля {why}'

        choise = random.random()
        if ans == 1:
            self.print_s(text1)
        elif ans == 2:
            self.print_s(2)
        elif ans == 3:
            self.print_s(3)
        elif ans == 4:
            self.print_s(4)
        else:
            self.print_s(5)


f = open("conf.json")    
bot = Singleton(json.load(f), "")
bot.main_menu()
f.close()


