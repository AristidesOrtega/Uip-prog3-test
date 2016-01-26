#Programa que pregunta el nombre del paciente
#si tiene dolor de cabeza, si tiene dolor de barriga, problema respiratorio
#Si tien dolor de cabeza, y barriga
#Si tiene dolor de cabeza tilenol
#Dolor de estomado pepto
#Si tien problema
#Si tien los Tres hay que internalo

nombre = str(input("Introduzca su nombre "))

h = input("Tiene dolor de cabeza (s/n) ")
s= input("Tiene dolor de estomago (s/n) ")
pr= input("Tiene problema respiratorio (s/n) ")

if h == "s" and s =="s" and pr == "s":
   print (nombre + "hospitalizado")
else:
   if h == "s" and s == "s":
      print(nombre + "toma paracetamol ")
   elif h == "s":
      print (nombre + "toma tylenol ")
   elif s == "s":
      print (nombre + "toma pepto bismol ")
   elif pr == "s":
      print (nombre + "toma pepto norcetin ")
   else:
      print ("toma tylenol " +nombre)
