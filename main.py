import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_Calculator

class CalculatorApp(QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variáveis para armazenar a operação e os valores
        self.current_operation = None
        self.current_value = ""

        # Conectando botões
        self.setup_connections()

    def setup_connections(self):
        self.btnPlus.clicked.connect(lambda checked: self.set_operation("+"))
        self.btnMinus.clicked.connect(lambda checked: self.set_operation("-"))
        self.btnMultiply.clicked.connect(lambda checked: self.set_operation("*"))
        self.btnDivide.clicked.connect(lambda checked: self.set_operation("/"))
        self.btn0.clicked.connect(lambda checked: self.add_number(0))
        self.btn1.clicked.connect(lambda checked: self.add_number(1))
        self.btn2.clicked.connect(lambda checked: self.add_number(2))
        self.btn3.clicked.connect(lambda checked: self.add_number(3))
        self.btn4.clicked.connect(lambda checked: self.add_number(4))
        self.btn5.clicked.connect(lambda checked: self.add_number(5))
        self.btn6.clicked.connect(lambda checked: self.add_number(6))
        self.btn7.clicked.connect(lambda checked: self.add_number(7))
        self.btn8.clicked.connect(lambda checked: self.add_number(8))
        self.btn9.clicked.connect(lambda checked: self.add_number(9))
        self.btnComma.clicked.connect(self.add_comma)
        self.btnPercent.clicked.connect(self.add_percent)
        self.btnEqual.clicked.connect(self.calculate_result)
        self.btnClear.clicked.connect(self.clear)

    def add_number(self, number):
        self.current_value += str(number)
        self.lineEdit.setText(self.current_value)


    def set_operation(self, operation):
        self.current_operation = operation
        self.current_value += operation
        self.lineEdit.setText(self.current_value)

    def calculate_result(self):
        try:
            result = eval(self.current_value)
            self.lineEdit.setText(str(result))
            self.current_value = str(result)
            self.current_operation = None
        except Exception as e:
            self.lineEdit.setText("Error")
            self.current_value = ""

    def clear(self):
        self.current_value = ""
        self.current_operation = None
        self.lineEdit.setText("")
    
    def add_comma(self):
        self.current_value += "."
        self.lineEdit.setText(self.current_value)

    def add_percent(self):
        try:
            current_float = float(self.current_value)
            self.current_value = str(current_float / 100)
            self.lineEdit.setText(self.current_value)
        except ValueError:
            self.lineEdit.setText("Error")   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
