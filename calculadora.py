import tkinter as tk

# Funciones de operaciones
def presionar_boton(valor):
    pantalla.insert(tk.END, valor)

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular():
    try:
       resultado = eval(pantalla.get())
       limpiar_pantalla()
       pantalla.insert(0, str(resultado))
    except Exception:
       limpiar_pantalla()
       pantalla.insert(0, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title=("Calculadora")
ventana.geometry=("300x400")

# Pantalla de texto
pantalla = tk.Entry(ventana, font=("Arial", 20), justify="right", bd=10)
pantalla.grid(row=0, column=0, columnspan=4, ipady=10, padx=10, pady=10)

# Diseño de los botones
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'c', '0' ,'=' ,'+',
]

# Crear y acomodar botones en lacuadricula (grid)
fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        cmd = calcular
    elif boton == 'c':
        cmd = limpiar_pantalla
    else:
        cmd = lambda x=boton: presionar_boton(x)

    tk.Button(ventana, text=boton, font=("Arial", 14), command=cmd, width=5, height=2). grid(row=fila, column=columna, padx=5, pady=5)

    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

ventana.mainloop()