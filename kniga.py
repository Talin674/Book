import os
import random

#сделать функцию бросания кубика
class Bag(object):
    def __init__(self, max_items=7):
        self.tbag = []
        self.max_items = max_items
    def add(self, item):
        if len(self.tbag) > self.max_items:
            self.tbag.append(item)
        else:
            print('Больше нет места!')
    def delete(self, index_item):
        del self.tbag[index_item]
    def show(self):
        ret = ""
        index_item = 0
        for i in self.tbag:
            ret = ret + str(index_item) + "\t" + i
            index_item += 1
        return ret

class Fight(object):
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

class Player(object):
    def __init__(self, skill=random.randint(1, 6) + 6, stamina=random.randint(1, 12) + 12,
                 luck=random.randint(1, 6) + 6, money=15):
        self.skill = skill
        self.stamina = stamina
        self.luck = luck
        self.money = money
        self.bag = Bag
    def __str__(self):
        statistic = {"Мастерство=":self.skill, "Выносливость=":self.stamina, "Удача=":self.luck, "Деньги=":self.money, "Инвентарь=":self.bag().tbag}
        return statistic.items()


# f = os.path.join("D:\Python/Book", "Braslavskiy_Podzemelya-Chernogo-zamka_lU7lVg_178246.txt")
f = "Braslavskiy_Podzemelya-Chernogo-zamka_lU7lVg_178246.txt"

q = open(f, 'r', encoding='utf-8')
for s in range(70):
    print(q.readline())
q.close()
score = 2
slovo1 = "—", "(", "то", "на"
slovo2= "Мастерство 1\nВыносливость" , "Мастерство 2\nВыносливость", "Мастерство 3\nВыносливость", "Мастерство 4\nВыносливость", \
        "Мастерство 5\nВыносливость", "Мастерство 6\nВыносливость", "Мастерство 7\nВыносливость", "Мастерство 8\nВыносливость", "Мастерство 9\nВыносливость"
slovo3 = "Мастерство", "Выносливость"
spisok = "уменьшить на ", "надо на ", "уменьшите на ", "увеличив на ", "уменьшив на ", "увеличьте на "

def cube():
    dice = random.randint(1, 12)
    return dice

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

def findNum(r, s, position):
    x = 2
    position = r.find(s, position + 1)
    if position == -1:
        # print ("Не обнаружен переход!")
        return None
    # print (position)
    if s == "(":
        x = 1
    if s == "Мастерство":
        x = 10
    if s == "Выносливость":
        x = 12
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

def fight_poisk(r):
    while True:
        for battle in slovo2:
            spt = r.find(battle)
            if spt != None:
                #print("Бой обнаружен!")
                return True

def next_steps(r):
    steps = []
    steps_enemy = []
    steps_enemy2 = []
    steps_enemy3 = []
    steps_fight = []
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
            if fight_poisk(r):
                for b in slovo3:
                    spt = findNum(r, b, position)
                    position += 1
                    length = len(steps_fight)
                    if spt != None and spt != "":
                        steps_fight.append(spt)
                        for m in steps_fight:
                            if length == 2:
                                for q in range(2):
                                    steps_enemy.append(m)
                            if length == 4:
                                for n in range(2):
                                    steps_enemy2.append(m)
                            if length == 6:
                                steps_enemy3.append(m)
                            print(m)
    return steps, steps_enemy, steps_enemy2, steps_enemy3

a = Player()
b = Bag
c = Fight

textGL = poisk(1)
steps = next_steps(textGL)
print(textGL)
print(steps)
while True:
    print('Чтобы открыть инвентарь - напишите "инвентарь". Если хотите выпить из фляги - напишите "фляга"')
    print('Чтобы посмотреть статистику вашего персонажа введите - "статистика"')
    num = input('Введите число из представленных в главе: ')
    if num == "фляга":
        if score > 0:
            score -= 1
            print('Вы использовали флягу (выносливость +2). У вас осталось', score, 'использованеи(ий)')
            a.stamina += 2
        else:
            print('У вас закончилось попытки')
    elif num == "статистика":
        print(a.__str__())
    elif num.isdigit():
        number = int(num)
        textGL = poisk(number)
        steps = next_steps(textGL)
        print(textGL)
        if steps == []:
            print("Игра закончена")
            break
        print(steps)
    else:
        print('Такого числа нет')