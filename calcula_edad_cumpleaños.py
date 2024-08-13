import datetime
from dateutil.relativedelta import relativedelta

def calcular_edad_y_cumpleaños():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}!")

    año_actual = datetime.date.today().year
    mes_actual = datetime.date.today().month
    dia_actual = datetime.date.today().day

    año_nacimiento = int(input("Ingrese su año de nacimiento: "))
    mes_nacimiento = int(input("Ingrese su mes de nacimiento (1-12): "))
    dia_nacimiento = int(input("Ingrese su día de nacimiento (1-31): "))

    fecha_nacimiento = datetime.date(año_nacimiento, mes_nacimiento, dia_nacimiento)
    fecha_actual = datetime.date(año_actual, mes_actual, dia_actual)

    edad = fecha_actual - fecha_nacimiento

    años = edad.days // 365
    meses = (edad.days % 365) // 30
    dias = (edad.days % 365) % 30

    print(f"Ok, {nombre}, tu edad es: {años} años, {meses} meses y {dias} días")

    # Calcular la próxima fecha de cumpleaños
    proximo_cumpleaños = fecha_nacimiento.replace(year=fecha_actual.year)
    if proximo_cumpleaños < fecha_actual:
        proximo_cumpleaños = proximo_cumpleaños.replace(year=fecha_actual.year + 1)

    # Calcular la diferencia entre la fecha actual y la próxima fecha de cumpleaños
    diferencia = relativedelta(proximo_cumpleaños, fecha_actual)

    # Mostrar la diferencia en meses y días
    print(f"Faltan {diferencia.months} meses y {diferencia.days} días para tu cumpleaños")

# Llamar a la función
calcular_edad_y_cumpleaños()

