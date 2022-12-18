from flask import Flask #importando la librería Flask en nuestro archivo.
from flask import request, jsonify #Importando algunos modulos de Flask


#Creando una nueva instancia del servidor Flask.
app = Flask(__name__) 


#Creando mi primer decorador (@app.route) y definiendo el primer path de la API: GET /
@app.route('/')
#Definiendo mi primera funcion dentro del decorador, método se llamará 
# cuando el cliente haga el request en el home
def inicio(): 
    #flask devolverá "Hola Desarrolladores", esto podría ser un string HTML o un string JSON o una función.
    return 'Hola Desarrolladores!' 


@app.route("/estudiantes") #aquí especificamos la ruta para el endpoint.
def estudiantes(): #aquí declaramos una función que se llamará cuando se realice una request a esa url
    return "Hola estudiantes!" #aquí especificamos el string que queremos responder al cliente.


#Si quieres que tus endpoint responda a metodos HTTP como (POST, PUT o DELETE)
# puedes especificarlo en el decorador (@app.route)  de esta forma.
@app.route("/alumnos", methods=['POST', 'GET']) # aquí especificamos que estos endpoints aceptan solicitudes POST y GET.
def obtenerAlumnos(): #definiendo una funcion dentro de mi decorador
  if request.method == 'POST': # podemos entender qué tipo de request estamos manejando usando un condicional
    return "Se recibió la petición HTTP por método POST"
  else:
    return "Se recibió la petición HTTP por método GET"


# El método jsonify lo usamos para convertir un diccionario llamado alumnos 
# en un string JSON antes de devolverlo al cliente.
@app.route("/lista-alumnos")
def getAlumnos():
    alumnos = {
      "id": 1,
      "name": "Urian"
    },
    {
      "id": 2,
      "name": "Brenda"
    }
    
    respuesta = jsonify(alumnos)
    respuesta.status_code = 200 # Asignamos el codigo 200 cuando todo salio Ok 
    return respuesta



#Manejo de errores y validaciones
@app.route('/profesores', methods=['POST'])
def listProf():
    # POST request
        body = request.get_json() # obtener el request body de la solicitud
        if body is None:
            return "El cuerpo de la solicitud es nulo", 400
        if 'nombre' not in body:
            return 'Especificar nombre',400
        if 'email' not in body:
            return 'Especificar email', 400

        return "OK", 200



#Por ultimo iniciamos el servidor en el localhost arrando nuestra aplicación.
if __name__ == '__main__': 
    app.run(debug=True, port=5000) 