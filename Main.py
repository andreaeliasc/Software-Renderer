#Universidad del Valle de Guatemala
#Graficas por Computador
#Andrea Elias
#17048

from gl import *

#Definicion de funcion para renderizar la Escena del Proyecto 1
def renderizarEscenaProyecto():
    #Se inician los componentes principales y necesarios para el renderizado de la Escena
    glInit()
    glCreateWindow(1000,1000)
    glClear()
    glColor(1,1,1)

    #Se renderiza el fondo de la escena
    fondo = Textura("fondo3.bmp")
    objeto.framebuffer = fondo.pixels
    
   
    
    #Se extrae la textura del normalMap
    mapeoNormal = Textura("normalMapVidrio.bmp")
    fur = Textura("fur.bmp")
    plumas = Textura("feathers.bmp")
    
    
    
    
    #Se colocan los valores que daran lugar a la view, camara, proyeccion & viewport 
    glLookAt(V3(-0.2,0,20),V3(0,0,0),norm(V3(0,1,0)))
    glLoadViewportMatrix(0, 0)

    #Primeros 5 modelos de la escena con sus correspondientes transformaciones y shaders a cada uno

    glLoad("hOLA1.obj", mtl="hOLA1.mtl", scale=(0.0017,0.0017,0.0017),translate=(-0.45,-0.65,-2),rotate=(0,-0.6,0),shade = 2)
    glLoad("oso1.obj", mtl="oso1.mtl", scale=(0.039,0.039,0.039),translate=(0,-1.7,8),rotate=(0,0,0),shade = 5, mapeo = fur)
    glLoad("genie3.obj", mtl="genie3.mtl", scale=(0.027,0.027,0.027),translate=(-0.28,-0.780,-2),rotate=(0,0,0), shade = 2)
    glLoad("aladdin.obj", mtl="aladdin.mtl", scale=(0.00067,0.00067,0.00067),translate=(-0.8,-0.7,-2),rotate=(0,0.7,0),shade = 1)
    glLoad("IAGO.obj", mtl="IAGO.mtl", scale=(0.02,0.02,0.02),translate=(0.5,-0.75,8),rotate=(0,0,0), shade = 5, mapeo = plumas)
   
   
    
    

    #Modelos complementarios de la escena
    glLoad("copasRoja.obj", mtl="copasRoja.mtl", scale=(0.023,0.023,0.023),translate=(0,-0.80,5),rotate=(0.7,-1,0), shade = 3) 
    glLoad("copaVerde.obj", mtl="copaVerde.mtl", scale=(0.029,0.029,0.029),translate=(-0.7,-1.1,15),rotate=(1.8,-1.8,0), shade = 3, mapeo = mapeoNormal)

    #Renderizacion de la Escena
    glFinish("Bienvenido a Agrabah.bmp")

#Menu para Interaccion
opcion = 1
while opcion != 2: 
        print("Bienvenido al renderizador de Escena Proyeccto 1:\n1. Renderizar Escena\n2. Salir")
        opcion = input("Ingrese la opcion que desea renderizar: ")
        try:
                opcion = int(opcion)
                if opcion == 1:
                    renderizarEscenaProyecto()
                else: 
                        print("Ha ingresado una opcion invalida")
        except ValueError:
                print("El dato que ingreso no es valido")
print("Hasta Pronto\n")
