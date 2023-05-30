class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class Calculator:
    def divide(self, a, b):
        if b == 0:
            raise CustomException1("Деление на ноль недопустимо.")
        return a / b

    def power(self, a, b):
        if b < 0:
            raise CustomException2("Возведение в отрицательную степень недопустимо.")
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise CustomException3("Извлечение квадратного корня из отрицательного числа недопустимо.")
        return a ** 0.5
      
      
class Application:
    def __init__(self):
        self.calculator = Calculator()

    def calculate_division(self, a, b):
        try:
            result = self.calculator.divide(a, b)
            print("Результат деления: {}".format(result))
        except CustomException1 as e:
            print("Ошибка при делении: {}".format(str(e)))
        except Exception as e:
            print("Произошла неизвестная ошибка: {}".format(str(e)))

    def calculate_power(self, a, b):
        try:
            result = self.calculator.power(a, b)
            print("Результат возведения в степень: {}".format(result))
        except CustomException2 as e:
            print("Ошибка при возведении в степень: {}".format(str(e)))
        except Exception as e:
            print("Произошла неизвестная ошибка: {}".format(str(e)))

    def calculate_sqrt(self, a):
        try:
            result = self.calculator.sqrt(a)
            print("Результат извлечения квадратного корня: {}".format(result))
        except CustomException3 as e:
            print("Ошибка при извлечении квадратного корня: {}".format(str(e)))
        except Exception as e:
            print("Произошла неизвестная ошибка: {}".format(str(e)))


app = Application()

app.calculate_division(10, 2)
app.calculate_division(10, 0)

app.calculate_power(2, 3)
app.calculate_power(2, -3)

app.calculate_sqrt(16)
app.calculate_sqrt(-16)
