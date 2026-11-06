#importamos flask 
from flask import Flask 
app=Flask (__name__)

#Definimos la ruta principal
@app.route ("/")
def HolaFlask():
    return "<h1> ¡Hola Flask! </h1> <hr>"

#Ahora reemplazamos ruta dos por otro ejercicio
#1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de 30%, 30% y 40% respectivamente.
@app.route ("/notas")
@app.route ("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas (nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> El resultado es: {resultado}</h1> <hr>"


#Ahora reemplazamos ruta tres por otro ejercicio
#2.) Un programa que al capturar la edad de una persona diga si es:  
# Menor de edad (Menor a 18 años)  
# Adulto (Mayor o igual a 18 años y menor a 60 años)  
#Adulto mayor (Mayor o igual a 60 años)  
@app.route ("/edad")
@app.route ("/edad/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1> La persona es:{R}</h1> <hr>"

if __name__=='__main__':
    #El valor True indica que la app se deja en modo debug
    app.run(debug=True)