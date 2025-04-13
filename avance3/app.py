from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Articulo:
    def __init__(self, articulo_id, nombre, cantidad):
        self.id = articulo_id
        self.nombre = nombre
        self.cantidad_disponible = cantidad
        self.cantidad_prestada = 0

class ComunalStorage:
    def __init__(self):
        self.articulos = {}
        self.id_counter = 1

    def agregar_articulo(self, nombre, cantidad):
        articulo = Articulo(self.id_counter, nombre, cantidad)
        self.articulos[self.id_counter] = articulo
        self.id_counter += 1

    def eliminar_articulo(self, articulo_id):
        if articulo_id in self.articulos:
            del self.articulos[articulo_id]

    def actualizar_articulo(self, articulo_id, cantidad):
        if articulo_id in self.articulos:
            self.articulos[articulo_id].cantidad_disponible += cantidad

    def obtener_articulos(self):
        return self.articulos.values()

almacen = ComunalStorage()

@app.route('/')
def index():
    articulos = almacen.obtener_articulos()
    return render_template('index.html', articulos=articulos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    almacen.agregar_articulo(nombre, cantidad)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:articulo_id>')
def eliminar(articulo_id):
    almacen.eliminar_articulo(articulo_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)