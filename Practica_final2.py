#1. Mostrar mensaje "Por favor ingresar las medidas de la pieza del mueble en centimetros: "
cms = float(input("Por favor ingresar las medidas de la pieza del mueble en centimetros: "))

#2. Convertir las medidas en centimetros a pulgadas
#Medidas en centrimetros / 2.54
pulgadas = cms / 2.54

#3. Mostrar mensaje "Las medidas en pulgadas de la pieza ingresada son: ", medida_en_pulgadas
print("Las medidas en pulgadas de la pieza ingresada son: ") 
print(pulgadas," pulgadas")
