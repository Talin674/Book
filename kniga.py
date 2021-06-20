import os
import random
# интвентарь
class Bag(object):
    def __init__(self, max_items=7):
        self.tbag = []
        self.max_items = max_items
    # добавление в инвентарь
    def add(self, item):
        if len(self.tbag) < self.max_items:
            self.tbag.append(item)
        else:
            print('Больше нет места!')

    # удаление из инвенторя
    def delete(self, index_item):
        del self.tbag[index_item]

    def show(self):
        ret = ""
        index_item = 0
        for i in self.tbag:
            ret = ret + str(index_item) + "\t" + i
            index_item += 1
        return ret
    def print_bag(self):
        print(self.tbag)
# заметки
class Notes(object):
    def __init__(self):
        self.notes = []
# игрок
class Player(object):
    def __init__(self, skill=random.randint(1, 6) + 6, stamina=random.randint(1, 12) + 12,
                 luck=random.randint(1, 6) + 6, money=15):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
        self.money = money
        self.bag = Bag()
        self.notes = Notes()

    # выводин на экран инвентарь игрока
    def __str__(self):
        statistic = {"Мастерство=":self.skill, "Выносливость=":self.stamina, "Удача=":self.luck, "Деньги=":self.money}
        return statistic.items()

    # запись в заметки
    def record(self, rec):
        self.notes.notes.append(rec)

    # удаление записи из заметок
    def delete_notes(self, index_rec):
        del self.notes.notes[index_rec]

    # вывод на экран заметок
    def print_notes(self):
        print(self.notes.notes)
    @property
    def add_money(self):
        return self.money
    @add_money.setter
    # добавление денег
    def add_money(self, money):
        self.money += money

# проверка удачи
class Lacky(Player):
    def lacky(self):
        lack = cube() + cube()
        if lack <= self.luck:
            print(lack, "lack")
            return True
        else:
            return False

# бой
class Fight(Player):
    # поиск характерисик
    def poisk_harakteristik(self, spisok, spisok_korney, parametr, spisok_pervih_slov_dobavlenie):
        # передаём spisok - в нём находятся фразы "Потеряйте 1 МАСТЕРСТВО и 3 ВЫНОСЛИВОСТИ", "прибавлять 1 к СИЛЕ своего УДАРА"
        # spisok_korney - список корней "УДАЧ", "МАСТЕРСТВ"
        # parametr - число которое нужно прибавить, либо отнять
        # spisok_pervih_slov_dobavlenie - в этом списке будут слова, которые идут в начале, и будут говорить программе, какую опирацию нужно сделать (прибавить или отнять)

        # harakteristics - содержит фразы из spisok
        # statistic - ищёт фразу в главе
        # korni - содержит корни из spisok_korney

        # этот цикл ищет фразы из spisok в главе
        for harakteristics in spisok:
            statistic = textGL.find(harakteristics)
            if statistic == -1:
                return None
            else:
                # если фраза находится, перебираются все возможные корни для определения, с какой характеристикой персонажа взаимодействовать
                for korni in spisok_korney:
                    harakteristics = str(harakteristics)
                    statistic = harakteristics.find(korni)
                    if statistic != -1:
                        # если первое слово фразы "Дабавьте", "Восстановить", то будет сложение, иначе - вычитание
                        for spiski in spisok_pervih_slov_dobavlenie:
                            if harakteristics.startswith(spiski):
                                if korni == "УДАЧ":
                                    self.luck += parametr
                                if korni == "МАСТЕРСТВ":
                                    self.skill += parametr
                                if korni == "ВЫНОСЛИВО":
                                    self.stamina += parametr
                                if korni == "УДАР":
                                    self.player += 1
                            else:
                                if korni == "УДАЧ":
                                    self.luck -= parametr
                                if korni == "МАСТЕРСТВ":
                                    self.skill -= parametr
                                if korni == "ВЫНОСЛИВО":
                                    self.stamina -= parametr
                                if korni == "УДАР":
                                    self.player -= parametr

    def fight_enemy(self):
        for i in enemys:
            print("НОВЫЙ ВРАГ")
            statistic = []
            m = 0
            for b in i:
                m += 1
                if m != 1:
                    statistic.append(b)
            dd = int(i[2])
            while dd > 0:
                l = len(enemys)
                if l > 1:
                    x = 0
                    for a in enemys:
                        self.enemy = cube() + cube() + int(a[1])
                        print("------БОЙ НАЧАЛСЯ------")
                        print("\t(" + a[0] + ")")
                        print("На кубиках выпало: ", self.enemy - int(a[1]))
                        print("Его сила удара: ", self.enemy)
                        self.player = cube() + cube() + self.skill
                        if textGL.find("паук затягивает вас на дерево"):
                            self.player = self.player - 1
                        print("\t\tВЫ")
                        print("На кубиках выпало: ", self.player - self.skill)
                        print("Ваша сила удара: ", self.player)
                        if self.enemy > self.player:
                            self.stamina -= 2
                            print("Ваша удар оказался слабее! Вы потеряли 2 выносливости, у вас осталось", self.stamina)
                        if self.player > self.enemy:
                            print("Вы сильнее вашего врага!")
                        if x == 0 and self.player > self.enemy:
                            dd -= 2
                            statistic.insert(1, dd)
                            del statistic[2]
                            print("DD", dd)
                            print(i[0], "потерял 2 выносливости, теперь у него", statistic[1])
                        elif self.stamina <= 0:
                            self.stamina = 0
                            print("Вы проиграли, у вас закончилась выносливость")
                            return False
                        if self.player == self.enemy:
                            print("Ваши силы равны!")
                        x += 1
                self.enemy = cube() + cube() + int(i[1])
                print("------БОЙ НАЧАЛСЯ------")
                print("\t(" + i[0] + ")")
                print("На кубиках выпало: ", self.enemy - int(i[1]))
                print("Его сила удара: ", self.enemy)
                self.player = cube() + cube() + self.skill
                if textGL.find("паук затягивает вас на дерево"):
                    self.player -= 1
                print("\t\tВЫ")
                print("На кубиках выпало: ", self.player - self.skill)
                print("Ваша сила удара: ", self.player)
                if self.player > self.enemy:
                    dd -= 2
                    statistic.insert(1, dd)
                    del statistic[2]
                    print("DD", dd)
                    print(i[0], "потерял 2 выносливости, теперь у него", statistic[1])
                elif self.player < self.enemy:
                    self.stamina -= 2
                    print("Ваша удар оказался слабее! Вы потеряли 2 выносливости, у вас осталось", self.stamina)
                elif self.stamina <= 0:
                    self.stamina = 0
                    return False
                if self.player == self.enemy:
                    print("Ваши силы равны!")
            del enemys[0]
        print("Ура! Все враги поверженны, вы одержали победу!")
        return True


# f = os.path.join("D:\Python/Book", "Braslavskiy_Podzemelya-Chernogo-zamka_lU7lVg_178246.txt")
f = "Braslavskiy_Podzemelya-Chernogo-zamka_lU7lVg_178246.txt"

q = open(f, 'r', encoding='utf-8')
for s in range(70):
    print(q.readline())
q.close()
score = 2
slovo1 = "—", "(", "то", "на"
spisok = "уменьшить на ", "надо на ", "уменьшите на ", "увеличив на ", "уменьшив на ", "увеличьте на "

# бросание кубика
def cube():
    dice = random.randint(1, 6) #не верно. кубик у нас 6 гранный и иногда надо кидать все таки 1 кубик, а не два
    return dice

# поиск проверки удачи
def poisk_luck(r):
    luck = r.find("ПРОВЕРЬТЕ СВОЮ УДАЧУ")
    if luck == -1:
        return None
    else:
        return True

d = Lacky()
# провека на удачу
def lack(r):
    if poisk_luck(r):
        if d.lacky():
            return True
        return False
    else:
        return False

# поиск главы
def poisk(number):
    q = open(f, 'r', encoding='utf-8')
    #    povtor.append(number)
    number2 = number + 1
    #    print(povtor)
    ret = ""
    while True:
        i = (q.readline())
        if i[:-1] == str(number):
            while True:
                r = q.readline()
                if r[:-1] == str(number2):
                    break
                # print(r)
                # print ("----")
                ret = ret + r
            return ret

# поиск глав на которые нужно перейти в главе
def findNum(r, s, position):
    x = 2
    position = r.find(s, position + 1)
    if position == -1:
        # print ("Не обнаружен переход!")
        return None
    # print (position)
    if s == "(":
        x = 1
    position += x
    if r[position] == " ":
        position += 1
    spt = ""
    while True:
        if r[position].isdigit():
            spt += r[position]
        else:
            break
        position += 1
    return spt

# характеристики врагов добавляются в список
def enemy_append(name_enemy, lines2):
    enemys = []
    name_enemy2 = len(name_enemy)
    parametr = 1
    parametr2 = 3
    n = 0
    for i in range(name_enemy2):
        enemys.append((name_enemy[n], lines2[parametr], lines2[parametr2]))
        n += 1
        parametr += 4
        parametr2 += 4
    return enemys

# находятся характеристики врагов
def fight_poisk(r):
    global enemys
    lines = []
    lines2 = []
    name_enemy = []
    lines += r.split("\n")
    l = len(lines)
    a = 0
    enemys = None
    for i in range(l):
        c = lines[a]
        if c.startswith("Мастерство"):
            c = lines[a + 1]
            if c.startswith("Выносливость"):
                m = lines[a]
                z = lines[a + 1]
                lines2 += m.split()
                lines2 += z.split()
                name_enemy.append(lines[a - 1])
                enemys = enemy_append(name_enemy, lines2)
        a += 1
    return enemys

# добавляются в список steps найденный главы
def next_steps(r):
    steps = []
    l = len(r)
    position = -1
    while l > position:
        for i in slovo1:
            spt = findNum(r, i, position)
            position += 1
            if spt != None and spt not in steps and spt != "" and spt != "1" and spt != "2":
                steps.append(spt)
            spt = findNum(r, "(", position)
            position += 1
            if spt != None and spt not in steps and spt != "" and spt != "1":
                steps.append(spt)
    return steps

# поиск боя с пауком на дереве
def fight_tree(r, steps, enemys):
    position = r.find("паук затягивает вас на дерево")
    if position == -1:
        return None
    else:
        lacky = lack(r)
        if lacky:
            print("Вам повезло, вы не будете сражаться с монстром! Идите на", steps[1], "главу")
            num = steps[1]
            return num
        else:
            if enemys != None:
                print("Бой начался!")
                print(c.fight_enemy())
                if c.fight_enemy():
                    print("Ваши характеристики", a.__str__())
                    num = steps[2]
                    return num
                else:
                    print("Вы проиграли!")
                    return False

#
def poisk_box(textGL ,x):
    position = textGL.find(x)
    if textGL == -1:
        return None
    if textGL[position] == " ":
        position += 1
    if x == "Внутри ларца лежат":
        position += 19
    spt = ""
    position += 1
    while True:
        spt += textGL[position]
        print("spt:", spt)
        position += 1
        print(position)
        if position == "," or " и " or ".":
            return spt

def add_steps(textGL):
    steps_box = []
    x = "Внутри ларца лежат"
    while True:
        spt = poisk_box(textGL, x)
        steps_box.append(spt)
        x = steps_box[-1]
        print("steps_box:", steps_box)
        if len(steps_box) == 3:
            return steps_box

# разговор с умирающим разбойником
def poisk_two_tree():
    yes_no = ask_yes_no("Вы поверили разбойнику? (yes или no): ")
    if yes_no == "yes":
        a.record("Вы поверили разбойнику")
        print('Вы решили доверится разбойнику! Если увидите две березы на холме, напишите "2 берёзы". У вас появилась новая заметка')
        print(a.print_notes())
        return True
    else:
        print("Вы не прислушались к совету разбойника!")
        return False

# поиск сокровища
def poisk_trove():
    integer = 1
    while True:
        textGL = poisk(integer)
        steps = textGL.find("поднимаетесь на холм к двум березам")
        if steps != -1:
            textGL = poisk(integer)
            steps = next_steps(textGL)
            print(textGL)
            print(steps)
            input("Нажмите Enter для перехода на 47 главу")
        integer += 1



# да или нет
def ask_yes_no(question):
    response = None
    while response not in("yes", "no"):
        response = input(question).lower()
    return response

b = Bag()
n = Notes()
a = Player()

c = Fight()

textGL = poisk(1)
steps = next_steps(textGL)
print(textGL)
print(steps)
yes_no = None
fight_treee = None
lines = None
poisk_two_treee = None
steps_box = []
x = "Внутри ларца лежат"
while True:
    print('Чтобы открыть инвентарь - напишите "инвентарь". Если хотите выпить из фляги - напишите "фляга"')
    print('Чтобы посмотреть статистику вашего персонажа введите - "статистика"')
    num = input('Введите число из представленных в главе: ')
    # бой на дереве
    if fight_treee != None:
        num = fight_treee
        fight_treee = None
    print(num)
    # использование фляги
    if num == "фляга":
        if score > 0:
            score -= 1
            print('Вы использовали флягу (выносливость +2). У вас осталось', score, 'использованеи(ий)')
            a.stamina += 2
        else:
            print('У вас закончилось попытки')
    # сколько осталось использований у фляги
    if num == "состояние фляги":
        print("У вас осталось", score, "попыток")
    # удаление заметки
    elif num.startswith("удалить заметку"):
        del_notes = int(input("Введите номер заметки которую хотите удалить: "))
        a.delete_notes(del_notes)
        print(a.print_notes())
        print("Заметка успешно удалена!")
    # запись в заметки
    elif num.startswith("записать"):
        num = num.split(" ", 1)[1]
        a.record(num)
        print(a.print_notes())
        print("Заметка успешно дабавленна!")
    # вывод на экран всех заметок
    elif num.startswith("заметки"):
        print(a.print_notes())
    # вся статистика игрока
    elif num == "статистика":
        print(a.__str__())
    # поиск главы и вовод её на экран
    elif num.isdigit():
        number = int(num)
        textGL = poisk(number)
        steps = next_steps(textGL)
        enemys = fight_poisk(textGL)
        print(textGL)
        print(steps)
        # ларец
        if poisk_box != None:
            add_steps(textGL)
        # битва на дереве
        fight_treee = fight_tree(textGL, steps, enemys)
        if fight_treee == False:
            break
        # если игрок погибает
        if steps == []:
            print("Игра закончена")
            break
        # разговор с умирающим разбойником
        if textGL.find("когда увидишь две березы") != -1:
            poisk_two_treee = poisk_two_tree()
            score -= 2
    # нахождение клада около двух берёз
    elif num == "2 берёзы" and textGL.find("на холме рядом с дорогой стоят две невысокие березки") != -1 and poisk_two_treee == True:
        poisk_trove()
    else:
        print('Такого числа нет')