from src.classes.calculator import Calculator
from src.utils.clear_console import clear_console

class Menu:
    def __init__(self, alloys):
        self.alloys = alloys
        self.calculator = Calculator(self.alloys, self)

    def confirm_percentages(self):
        clear_console()
        print("Porcentajes ingresados:")
        for component, percentage in zip(self.alloys.selected_components, self.alloys.component_percentages):
            print(f"{component}: {percentage}%")
        print("¿Los porcentajes ingresados con correctos?")
        print("1. Sí")
        print("2. No, quiero ingresarlos nuevamente")
        option = input()
        match option:
            case "1":
                self.calculator.calculate_component_weight()
            case "2":
                self.alloys.selected_components = []
                self.alloys.component_percentages = []
                self.alloys.set_total_percentage(0)
                self.alloys.select_components("Seleccione el primer componente que requiera para realizar el cálculo")
            case _:
                pass

    def confirm_new_component(self):
        clear_console()
        print("¿Desea añadir un nuevo componente? Digite uno de los números mostrados en pantalla")
        print("1. Si")
        print("2. No")
        option = input()
        match option:
            case "1":
                self.alloys.select_components("Seleccione el nuevo componente que requiera para realizar el cálculo")
            case "2":
                self.alloys.assign_percentage_component("Asigne el porcentaje de cada componente en la aleación")
            case _:
                print("Debes digitar uno de los números mostrados en pantalla")
                self.confirm_new_component()

    def confirm_new_alloy(self):
        print("¿Desea llevar a cabo otro cálculo?")
        print("1. Si")
        print("2. No")
        option = input()
        match option:
            case "1":
                self.alloys.select_components("Seleccione el primer componente que requiera para realizar el cálculo")
            case "2":
                return
            case _:
                print("Debes digitar uno de los números mostrados en pantalla")
                self.confirm_new_alloy()