from flask import Flask, render_template, request,session,redirect,url_for

app = Flask(__name__)
# Necesario cuando se usa session
app.secret_key = 'unaclavesecreta'

@app.route("/")
def carrito():
    # Verificando si lista esta en la session
    if 'lista' not in session:
        # Inicializar la lista
        session['lista'] = []
    return render_template('index.html',lista = session['lista'])  

@app.route("/procesa",methods=['GET','POST'])  
def procesa():
    producto = request.form.get("producto")
    if 'lista' in session and producto:
        # Producto adicionado en la lista
        session['lista'].append(producto)
        # Aseguramos que la session ha sido modificado
        session.modified =  True
    return redirect(url_for("carrito"))    

@app.route("/vaciar",methods=["GET"])
def vaciar():
    # Elimina de session lista
    session.pop("lista",None)
    return redirect(url_for("carrito"))

if __name__ == "__main__":
    app.run(debug=True)