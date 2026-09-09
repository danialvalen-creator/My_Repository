import math
import os

class Calculator:
    def __init__(self):
        self.expression = ""
        self.running = True
    
    def clear_screen(self):
        """Очистка экрана"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Отображение меню"""
        self.clear_screen()
        print("=" * 50)
        print("           КАЛЬКУЛЯТОР (Консольная версия)")
        print("=" * 50)
        print("\nДоступные операции:")
        print("  +   -   *   /   -  базовые операции")
        print("  √   -  квадратный корень")
        print("  ±   -  смена знака")
        print("  C   -  очистка")
        print("  ⌫   -  удалить последний символ")
        print("  =   -  вычислить результат")
        print("  q   -  выход")
        print("\n" + "=" * 50)
        
        if self.expression:
            print(f"\nВыражение: {self.expression}")
        else:
            print("\nВведите выражение:")
    
    def evaluate_expression(self):
        """Вычисление выражения"""
        try:
            
            expr = self.expression.replace('√', 'math.sqrt')
            result = eval(expr)
            
            if isinstance(result, float):
                result = round(result, 10)
                if result == int(result):
                    result = int(result)
            
            print(f"\nРезультат: {result}")
            self.expression = str(result)
            input("\nНажмите Enter для продолжения...")
            return True
        except Exception as e:
            print(f"\nОшибка: Некорректное выражение!")
            self.expression = ""
            input("\nНажмите Enter для продолжения...")
            return False
    
    def process_input(self, user_input):
        """Обработка ввода пользователя"""
        if user_input.lower() == 'q':
            self.running = False
            return
        
        elif user_input == 'C':
            self.expression = ""
        
        elif user_input == '⌫':
            self.expression = self.expression[:-1]
        
        elif user_input == '=':
            self.evaluate_expression()
        
        elif user_input == '±':
            if self.expression:
                if self.expression[0] == '-':
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
        
        else:
            self.expression += user_input
    
    def run(self):
        """Основной цикл программы"""
        while self.running:
            self.display_menu()
            
            user_input = input("> ").strip()
            
            if user_input:
                self.process_input(user_input)

def main():
    calculator = Calculator()
    calculator.run()
    print("\nСпс!")

if __name__ == "__main__":
    main()
