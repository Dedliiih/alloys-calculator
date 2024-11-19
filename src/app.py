from src.classes.alloy import Alloys
import time

def app():
    print("------------------------------------------")
    print("Bienvenido a la calculadora de aleaciones")
    print("------------------------------------------")
    time.sleep(3)
    alloys = Alloys()
    alloys.select_components("Seleccione el primer componente que requiera para realizar el cálculo")
