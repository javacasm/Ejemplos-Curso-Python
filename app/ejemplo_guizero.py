from guizero import App, Text, PushButton, Picture, Combo, TextBox

app = App(title="Primera aplicación en Python", height = 800, width = 1200)

colors = ["black", "white", "red", "green", "blue", "gold", "olive drab","peru","tomato",'sienna','gray70',"#ff0000",'#00ff00','#0000ff','#990099','Color que no existe']

app.text_color = colors[0] # black
app.bg = colors[5]  # gold

# cambia el corlor del fondo
def update_bg():
    app.bg = bg_combo.value

# cambia el color del texto
def update_text():
    app.text_color = text_combo.value

# muestra el nombre de la caja en el texto de arriba
def mostrar_nombre():
    if nameBox.value in ['Pepe','pepe', 'pp','p']:
        introText.value = f"Bienvenido {nameBox.value},  administrador del sistema"
    else:
        introText.value = f"Hola {nameBox.value},  bienvenido a mi primera aplicación Python"

# función salir de la aplicación
def salir():
    app.destroy()
    exit()

introText = Text(app, text = "Hola, bienvenidos a mi primera aplicación Python")

# Etiqueta de "Como te llamas"
labelName = Text(app, text = '¿Cómo te llamas?')

# Caja de texto donde escribimos el nombre
nameBox = TextBox(app)

# botón "Pulsame"
okButton = PushButton(app, text = "Púlsame", command = mostrar_nombre )

# Colores propios del botón
okButton.bg = colors[1]
okButton.text_color = colors[3]

colorBGLabel = Text(app, text = "Color de fondo")
bg_combo = Combo(app, options=colors, selected=app.bg, command = update_bg)

colorTextLabel = Text(app, text="Color del texto")
text_combo = Combo(app, options=colors, selected=app.text_color, command = update_text)

closeButton = PushButton(app, text ='Salir', command = salir)


imagenes = ['cat-space.gif','nyancat2.gif','nyancat.gif']

nImagen = 0 # la primera imagen

pic = Picture(app, image = 'imagenes/'+imagenes[nImagen], height = 200)

def cambiaImagen():
    global nImagen
    nImagen = nImagen + 1
    if nImagen >= len(imagenes):
        nImagen = 0
    pic.image = 'imagenes/'+imagenes[nImagen]

changeImageButton = PushButton(app, text = 'Siguiente imagen', command = cambiaImagen)

app.display()