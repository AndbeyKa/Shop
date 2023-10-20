#Создание класса с необходимыми атрибутами.
class Market:
    Cola = 'Cola (1)'
    Sprite = 'Sprite (2)'
    Fanta = 'Fanta (3)'
    ColaPrice = 100
    SpritePrice = 90
    FantaPrice = 105

    #Создание функции (или метода), которая автоматически выполняется, при создании нового экземпляра.
    def __init__(self):
        print(self.Cola, self.ColaPrice)
        print(self.Sprite, self.SpritePrice)
        print(self.Fanta, self.FantaPrice)
    
    #Создание функции выбора товара, расчет его цены в зависимости от количества литров.
    def purchase(self):
        x = 0
        liters = 0
        while x != 999: 
            x = int(input('Введите артикул товара, или 999 для возврата в корзину: '))
            if x == 1:
                liters = int(input('Введите количество литров: '))
                self.slots.append(f'Наименование товара: {self.Cola}, Стоимость товара: {self.ColaPrice*liters} рублей, Количество товара: {liters} литра(ов)') 
            if x == 2:
                liters = int(input('Введите количество литров: '))
                self.slots.append(f'Наименование товара: {self.Sprite}, Стоимость товара: {self.SpritePrice*liters} рублей, Количество товара: {liters} литра(ов)') 
            if x == 3:
                liters = int(input('Введите количество литров: '))
                self.slots.append(f'Наименование товара: {self.Fanta}, Стоимость товара: {self.FantaPrice*liters} рублей, Количество товара: {liters} литра(ов)') 
            if x != 999 and x != 1 and x != 2 and x !=3:
                print('Error: Ошибка ввода артикула товара!')

    #Создание метода, для возможности редактирования цены товара в классе, другими пользователями.
    @classmethod
    def set_cls_prise(cls, ColaPrice=100, SpritePrice=90, FantaPrice=105):
        cls.ColaPrice = ColaPrice
        cls.SpritePrice = SpritePrice
        cls.FantaPrice = FantaPrice

#Создание переменной (экземпляра класса), вызов методов.
a = Market()
a.slots = [] 
a.purchase()

print(a.slots)