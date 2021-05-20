import os
import random

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
class Fight(Player):
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
                        self.enemy = cube() + int(a[1])
                        print("------БОЙ НАЧАЛСЯ------")
                        print("\t(" + a[0] + ")")
                        print("На кубиках выпало: ", self.enemy - int(a[1]))
                        print("Его сила удара: ", self.enemy)
                        self.player = cube() + self.skill
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
                self.enemy = cube() + int(i[1])
                print("------БОЙ НАЧАЛСЯ------")
                print("\t(" + i[0] + ")")
                print("На кубиках выпало: ", self.enemy - int(i[1]))
                print("Его сила удара: ", self.enemy)
                self.player = cube() + self.skill
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

a = Player()
b = Bag()
c = Fight()
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
        enemys = fight_poisk(textGL)
        print(textGL)
        if enemys != None:
            print("Начался бой!")
            print(c.fight_enemy())
            if c.fight_enemy() == True:
                print("Ваши характеристики", a.__str__())
            else:
                print("Вы проиграли!")
                break
        if steps == []:
            print("Игра закончена")
            break
        print(steps)
    else:
        print('Такого числа нет')