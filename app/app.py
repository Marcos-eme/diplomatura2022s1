import socket
from datetime import date

def imprimir_fecha_hoy():
  fecha = date.today()
  fechaFormateada = fecha.strftime("%d/%m/%Y")
  print("Hoy es:", fechaFormateada)

def imprimir_hostname():
  print("Mi nombre de host es: ", socket.gethostname())

def iteracion():
  print("Voy a iterar 10 veces")
  for x in range(10):
   print("Iteracion: ", x)

if __name__== "__main__":
  imprimir_fecha_hoy()
  imprimir_hostname()
  iteracion()