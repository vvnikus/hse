class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail


class Contacts:
    def __init__(self):
        self.baza = [[], [], [], [], [], []]
    def __add__(self, contact):
        self.baza[0].append(len(self.baza[0]) + 1)
        familia = contact.name.split(" ")
        while len(familia) < 3:
            familia.append(None)
        self.baza[1].append(familia[0])
        self.baza[2].append(familia[1])
        self.baza[3].append(familia[2])
        if contact.phone != '':
            self.baza[4].append(contact.phone)
        else:
            self.baza[4].append(None)
        if contact.mail != '':
            self.baza[5].append(contact.mail)
        else:
            self.baza[5].append(None)

    def getContact(self, id):
        ans = "ID - " + str(self.baza[0][id]) + "\n"
        if self.baza[1][id] != None:
            ans += "ФИО: " + self.baza[1][id]
        if self.baza[2][id] != None:
            ans += " " + self.baza[2][id]
        if self.baza[3][id] != None:
            ans += " " + self.baza[3][id]
        if self.baza[4][id] != None:
            ans += "\n" + "Номер телефона: " + self.baza[4][id]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.baza[5][id] != None:
            ans += "\n" + "Почта: " + self.baza[5][id] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def phoneSearch(self, phone):
        if self.baza[4].__contains__(phone):
            id = self.baza[4].index(phone)
            print(self.getContact(id))
        else:
            print("отсутсвует")

    def mailSearch(self, mail):
        if self.baza[5].__contains__(mail):
            id = self.baza[5].index(mail)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")

    def search(self, familia):
        ids = []
        if familia[0] != None:
            for i in range(len(self.baza[1])):
                if familia[0] == self.baza[1][i]:
                    ids.append(self.baza[0][i] - 1)
        if familia[1] != None:
            if familia[0] != None:
                for id in ids:
                    if familia[1] != self.baza[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.baza[2])):
                    if familia[1] == self.baza[2][i]:
                        ids.append(self.baza[0][i] - 1)

        if familia[2] != None:
            if familia[0] != None or familia[1] != None:
                for id in ids:
                    if familia[2] != self.baza[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.baza[3])):
                    if familia[2] == self.baza[3][i]:
                        ids.append(self.baza[0][i] - 1)

        if len(ids) == 0:
            print("отсутсвует")
        else:
            for id in ids:
                print(self.getContact(id))

    def getWithoutPhoneOrMail(self, num):
        if num == 1:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None:
                    print(self.getContact(i))
            return
        if num == 2:
            for i in range(len(self.baza[5])):
                if self.baza[5][i] == None:
                    print(self.getContact(i))
            return
        if num == 3:
            for i in range(len(self.baza[4])):
                if self.baza[4][i] == None and self.baza[5][i] == None:
                    print(self.getContact(i))
            return

    def change(self, id, contact):
        id -= 1
        familia = contact.name.split(" ")
        while len(familia) < 3:
            familia.append(None)
        self.baza[1][id] = familia[0]
        self.baza[2][id] = familia[1]
        self.baza[3][id] = familia[2]
        if len(contact.phone) > 0:
            self.baza[4][id] = contact.phone
        else:
            self.baza[4][id] = None
        if len(contact.mail) > 0:
            self.baza[5][id] = contact.mail
        else:
            self.baza[5][id] = None

    def printAll(self):
        for i in range(len(self.baza[0])):
            print(self.getContact(i))

def printCommands():
    print("Список доступных команд: ")
    print("1 - Вывести контакты", "2 - Поиск по номеру", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")


print("Введите название файла")
fileName = input()
file = open(fileName, encoding='utf-8')
b = Contacts()
for st in file:
    arr = st.split(",")
    contact = Contact(arr[0],arr[1].replace(" ",""),arr[2].replace(" ","").replace("\n",""))
    b.__add__(contact)
print("База сформирована")
printCommands()
z = int(input())
while z!="akdna@@@kdn":
    if z==1:
        b.printAll()
    elif z==2:
        print("Введите номер")
        phone = input()
        b.phoneSearch(phone)
    elif z == 3:
        print("Введите почту")
        mail = input()
        b.mailSearch(mail)
    elif z == 4:
        familia = []
        print("Введите фамилию или пустую строку")
        f = input()
        if f=='':
            familia.append(None)
        else:
            familia.append(f)
        print("Введите имя или пустую строку")
        i = input()
        if i == '':
            familia.append(None)
        else:
            familia.append(i)
        print("Введите отчество или пустую строку")
        m = input()
        if o == '':
            familia.append(None)
        else:
            familia.append(o)
        b.search(familia)
    elif z == 5:
        print("выберите метод поиска: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        b.getWithoutPhoneOrMail(num)
    elif z == 6:
        print("Введите id контакта, который хотите изменить и новые данные для него", "(в две разные строки)", sep="\n")
        id = int(input())
        q = input().split(",")
        contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        b.change(id, contact)
    elif z == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    z = int(input())
