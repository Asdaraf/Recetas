f = open("ingredientes.txt","r")

lineas_ingredientes = f.readlines()

stock_ingredientes = {}

for stock in lineas_ingredientes:
    fila_ingrediente = stock.strip().split(" ")
    
    ingrediente = fila_ingrediente[0]
    stock = int(fila_ingrediente[1])

    stock_ingredientes[ingrediente] = stock

f2 = open("recetas.csv","r")

lineas_recetas = f2.readlines()

recetas = {}

for receta in lineas_recetas:
    fila_receta = receta.strip().split(",")
    
    receta = fila_receta[0]
    ingredientes = fila_receta[1:]

    recetas[receta] = ingredientes

def prepararReceta(receta):
    if receta in recetas.keys():
        for ingred in recetas[receta]:
            if stock_ingredientes[ingred] == 0:
                print(f"No se puede hacer {receta} porque falta {ingred}")
                
        for ingred in recetas[receta]:   
            if stock_ingredientes[ingred] != 0:
                stock_ingredientes[ingred] -= 1               
    else:
        print(f"Lo siento, pero no preparamos {receta}")

def reponer(lista):
    for i in lista:
        if i in stock_ingredientes:
            stock_ingredientes[i] += 1
        else:
            stock_ingredientes[i] = 1
    
def printStock():
    print("Stock actual de ingredientes disponibles")
    for stock,cant in stock_ingredientes.items():
        print(stock,cant)

def stop():
    exit()

while True:
    
    ingresar_accion = input("Ingresa la receta que quieres o REPONER: ")
    ingresar_accion = ingresar_accion.split(" ")
    
    accion = ingresar_accion[0].title()
    contenido = ingresar_accion[1:]

    if accion == "Preparar":
        prepararReceta(contenido[0])
        printStock()
    
    elif accion == "Reponer":
        reponer(contenido[0:])
        printStock()

    elif accion == "Stop":
        stop()