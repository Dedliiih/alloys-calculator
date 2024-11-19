from src.classes.menu import Menu
from src.classes.calculator import Calculator
from src.utils.clear_console import clear_console
from src.utils.components import components

class Alloys:
    def __init__(self):
        self.selected_components = []
        self.component_percentages = []
        self.total_percentage = 0
        self.menu = Menu(self)
        self.calculator = Calculator(self, self.menu)

    def get_total_percentage(self):
        return self.total_percentage

    def set_total_percentage(self, new_total):
        self.total_percentage = new_total

    def assign_component(self, component):
        if component in self.selected_components:
            self.select_components("No pueden haber componentes repetidos. Seleccione nuevamente un componente.")

        self.selected_components.append(component)

    def show_components(self):
        rows = 4
        columns_data = [components[i:i + rows] for i in range(0, len(components), rows)]
        transposed = list(zip(*columns_data))

        for row in transposed:
            row_items = [f"{components.index(item) + 1}. {item}" for item in row if item]
            print(" | ".join(row_items))

    def select_components(self, message):
        clear_console()
        self.show_components()
        print(message)
        try:
            choice = int(input())
            if choice > len(components) or choice < 1:
                self.select_components("El componente seleccionado no existe. Digita uno de los números que aparecen en pantalla")
            self.assign_component(components[choice - 1])
            if len(self.selected_components) >= 2:
                return self.menu.confirm_new_component()
            self.select_components("Seleccione el segundo componente que requiera para realizar el cálculo")
        except ValueError:
            self.select_components("Debes ingresar uno de los numeros que aparecen en pantalla. No debes ingresar letras")


    def assign_percentage_component(self, message):
        for component in self.selected_components:
            total_percentage = self.get_total_percentage()
            actual_maximum = 100 - total_percentage
            while True:
                print(message)
                percentage = int(input(f"Ingrese el porcentaje del componente {component}. Porcentaje disponible: {actual_maximum}"))

                if percentage < 0:
                    print("El porcentaje no debe ser menor a 0")
                    continue

                if percentage > actual_maximum:
                    print("No puedes superar el porcentaje máximo restante")
                    continue

                else:
                    break
            self.component_percentages.append(percentage)
            self.set_total_percentage(sum(self.component_percentages))

        if self.get_total_percentage() < 100:
            self.component_percentages = []
            self.set_total_percentage(0)
            self.assign_percentage_component("Los porcentajes son incorrectos, debes cubrir el 100% de la aleación. Ingrésalos nuevamente")
        self.menu.confirm_percentages()

    def create_components_list(self):
        components_list = []
        for component, percentage in zip(self.selected_components, self.component_percentages):
            components_list.append({
                "component": component,
                "percentage": percentage
            })
        return components_list
