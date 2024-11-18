from src.utils.alloys import components as components


class Alloys:
    def __init__(self):
        self.selected_components = []

    def show_components(self):
        rows = 4
        columns_data = [components[i:i + rows] for i in range(0, len(components), rows)]
        transposed = list(zip(*columns_data))

        for row in transposed:
            row_items = [f"{components.index(item) + 1}. {item}" for item in row if item]
            print(" | ".join(row_items))

    def select_components(self, message):
        self.show_components()
        print(message)
        choice = int(input())
        self.selected_components.append(components[choice - 1])
        print(self.selected_components)
        self.confirm_new_alloy()

    def confirm_new_alloy(self):
        print("¿Desea añadir un nuevo componente? Digite uno de los números mostrados en pantalla")
        print("1. Si")
        print("2. No")
        option = input()
        match option:
            case "1":
                self.select_components("Seleccione el nuevo componente que requiera para realizar el cálculo")
            case "2":
                pass
            case _:
                print("Debes digitar uno de los números mostrados en pantalla")
                self.confirm_new_alloy()


def app():
    print("Bienvenido a la calculadora de aleaciones")
    alloys = Alloys()
    alloys.select_components("Seleccione los componentes que requiera para realizar el cálculo")


