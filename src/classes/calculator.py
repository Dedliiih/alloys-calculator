class Calculator:
    def __init__(self, alloys, menu):
        self.alloys = alloys
        self.menu = menu

    def calculate_component_weight(self):
        components_list = self.alloys.create_components_list()
        try:
            alloy_weight = int(input("Ingrese el peso total de la aleación en gramos"))
            for component in components_list:
                weight = (component["percentage"] / 100) * alloy_weight
                print(f"El peso de {component["component"]} corresponde a {int(weight)} gramos")
            self.menu.confirm_new_alloy()
        except ValueError:
            self.calculate_component_weight()