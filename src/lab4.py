class Student:
    def __init__(self, first_name='...', last_name='...', rating=0, hight=0):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__rating = rating
        self.__hight = hight

    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name


    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name


    def get_rating(self):
        return self.__rating
    def set_rating(self, rating):
        self.__rating = rating


    def get_hight(self):
        return self.__hight
    def set_hight(self, hight):
        self.__hight = hight


    def __str__(self):
        return f'Student: {self.__first_name}, {self.__last_name}, {self.__rating}, {self.__hight}'

    def __repr__(self):
        return f'Student: {self.__first_name}, {self.__last_name}, {self.__rating}, {self.__hight}'


    def __del__(self):
        print(f'deleted Student: {self.__first_name}, {self.__last_name}')


def main():
    Student1 = Student('Ihor',  'Kolomoiskyi', 85, 175)
    Student2 = Student('Volodymyr', 'Zelenskyy', 65, 155)
    Student3 = Student('Viktor', 'Yanukovych', 50, 193)

    print(Student1)
    print(Student2)
    print(Student3)

    print(Student1)
if __name__ == '__main__':
      main()

