"""Carlos Fernando Pacheco
Grupo #213022_525
Programa  INGENIERIA DE TELECOMUNICACIONES
Fundamentos de Programación - Evaluacion Final
Código Fuente: autoría propia"""
# ==========================================
# Programa: Cálculo de Horas Semanales
# ==========================================

# Lista de recursos con nombres ya definidos
nombres = ["Carlos", "Emilio", "Luis", "Marta"]

# Matriz donde se almacenarán los datos
recursos = []

# Solicitar horas trabajadas
for nombre in nombres:

    print("\n===================================")
    print("Registro de horas para:", nombre)
    print("===================================")

    lunes = int(input("Horas trabajadas el lunes: "))
    martes = int(input("Horas trabajadas el martes: "))
    miercoles = int(input("Horas trabajadas el miércoles: "))
    jueves = int(input("Horas trabajadas el jueves: "))
    viernes = int(input("Horas trabajadas el viernes: "))

    # Guardar datos en la matriz
    recursos.append([
        nombre,
        lunes,
        martes,
        miercoles,
        jueves,
        viernes
    ])


# Función para calcular horas y clasificación
def calcular_jornada(recurso):

    nombre = recurso[0]

    total_horas = sum(recurso[1:])

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# Mostrar resultados
print("\n===================================")
print("RESULTADOS FINALES")
print("===================================\n")

for recurso in recursos:

    nombre, total, clasificacion = calcular_jornada(recurso)

    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("-----------------------------------")