import os.path


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        if os.path.isfile(self.__file_name):
            self.file_new = open(self.__file_name, 'r')
            self.file_new.close()
        else:
            self.file_new = open(self.__file_name, 'w')
            self.file_new.close()

    def get_products(self):
        self.file = open(self.__file_name, 'r')
        return self.file.read()

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(product.__str__() + '\n')
                file.close()
            else:
                print(f'������� {product.name} ��� ���� � ��������')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
