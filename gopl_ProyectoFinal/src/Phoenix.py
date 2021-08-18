"""
###############################################
Proyecto Final: Media Center (PHOENIX)
Fundamentos de Sistemas Embebidos
Semestre 2021-2
Creación: 16/08/2021
Última modificación: 17/08/2021

Integrantes:González Pacheco Leonardo Alonso
            Hernández Hernández Edgar
            Ruiz Aguilar Eduardo
###############################################
"""

import pygame 
import threading 
import vlc 
import os 
from tkinter import* 
from PIL import ImageTk, Image
import webbrowser

#Ventana Inicio
class Ventana:
    #Constructor de la ventana
    def __init__(self,ventana):
        self.ventana=ventana#El atributo ventana se inicializa con el
                            #valor mandado por el constructor, que es un
                            #objeto Tk, el cual permite crear ventanas con
                            #diferentes objetos dentro de ella
        self.opcion = 0
        ventana['background']='#000000'
        ventana.title("Reproductor Phoenix")#Ponemos el título a la ventana
        self.imagen = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/netflix.png').resize((100, 100)))
        self.boton  = Button(ventana, image = self.imagen, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.netflix).place(x=50,y=0)#Coloca el botón
        
        self.imagen1 = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/Spotify.png').resize((100, 100)))
        self.boton1  = Button(ventana, image = self.imagen1, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.spotify).place(x=1100,y=0)                                                              #Spotify y el comando spotify
        
        self.imagen2 = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/Amazon.png').resize((100, 100)))
        self.boton2  = Button(ventana, image = self.imagen2, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.primeVideo).place(x=50,y=500)
        
        self.imagen3 = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/Disney.png').resize((100, 100)))
        self.boton3  = Button(ventana, image = self.imagen3, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000',command=self.disney).place(x=1100,y=500)
        
        self.imagen4 = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/USB.png').resize((200, 200)))
        self.boton4  = Button(ventana, image = self.imagen4, width= 200, height=200,relief="flat", borderwidth=0, bg='#000000', command=self.memoria).place(x=550,y=400)
        
        self.imagen5 = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
        self.boton5  = Button(ventana, image = self.imagen5, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=600,y=50)
    """En estas sección se muestran los métodos que se activan al presionar los
    botones"""
    def netflix(self):
        self.opcion = 1
        self.ventana.destroy()
    def spotify(self):
        self.opcion = 2
        self.ventana.destroy()
    def primeVideo(self):
        self.opcion = 3
        self.ventana.destroy()
    def disney(self):
        self.opcion = 4
        self.ventana.destroy()
    def memoria(self):
        self.ventana.destroy()
    def salir(self):
        self.opcion = 5
        self.ventana.destroy()
    
    def dev(self):
        return self.opcion

#Ventana USB
class Ventana2:
    #Constructor de la segunda ventana
    def __init__(self,ventana,opcion):
        self.opcion=opcion
        self.ventana=ventana
        ventana.title("Interfaz Memoria")
        ventana['background']='#000000'
        ventana.geometry("700x400")
        ext_audio=[".mp3"] 
        musica=encontrar(ext_audio)
        
        ext_video=[".mp4",".mkv"]
        videos=encontrar(ext_video)
        
        ext_imagenes=[".jpg",".png",".jfif",".jpeg"]
        fotos=encontrar(ext_imagenes)
        
        if(len(musica)==0 and len(videos)==0 and len(fotos)==0):
            self.lab=Label(ventana, bg="black", fg="white", font=('Arial',15),text="No hay contenido").place(x=570,y=170)
            self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
            self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=600,y=280)

        if(len(musica)!=0):
            self.bMusica = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/musica.png').resize((100, 100)))
            self.botonMusica = Button(ventana, image = self.bMusica, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.musica).place(x=50,y=280)
            self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
            self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=600,y=500)

        if(len(arr2)!=0):
            self.bFotos = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/imagen.png').resize((100, 100)))
            self.botonFotos  = Button(ventana, image = self.bFotos, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.fotos).place(x=250,y=280)
            self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
            self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=600,y=500)
        
        if(len(arr3)!=0):
            self.bVideos = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/Video.png').resize((100, 100)))
            self.botonVideos  = Button(ventana, image = self.bVideos, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.videos).place(x=450,y=280)
            self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
            self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=600,y=500)

    def musica(self):
        self.opcion=1
        self.ventana.destroy()
    def fotos(self):
        self.opcion=2
        self.ventana.destroy()
    def videos(self):
        self.opcion=3
        self.ventana.destroy()
    def salir(self):
        self.opcion=5
        self.ventana.destroy()
    def regresa(self):
        return self.opcion

#Ventana audio
class Ventana3:
    def __init__(self,ventana,n):
        self.ventana=ventana
        self.i=0
        self.aux=True
        self.ban=True
        self.n=n
        ventana.title("Reproductor de audio")
        ventana.geometry("700x400")
        ventana['background']='#000000'
        pygame.mixer.music.load(self.n[self.i])#Carga el archivo de audio
        pygame.mixer.music.play()#Se reproduce el archivo cargado
        
        self.bMusica = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/play.png').resize((100, 100)))
        self.botonMusica = Button(ventana, image = self.bMusica, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.play).place(x=300,y=100)

        self.bSiguiente = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/next.png').resize((100, 100)))
        self.botonSiguiente = Button(ventana, image = self.bSiguiente, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.siguiente).place(x=400,y=100)

        self.bAnterior = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/prev.png').resize((100, 100)))
        self.botonAnterior = Button(ventana, image = self.bAnterior, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.anterior).place(x=200,y=100)
        
        self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
        self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=300,y=250)
   
    def play(self):
        '''Si ban es True la música esta reproduciendoce y se quiere pausar'''
        if(self.ban==True):
            pygame.mixer.music.pause()
            self.ban=False
        else:
            pygame.mixer.music.unpause()#Reanuda el audio
            self.ban=True#Pone al atributo ban en True
    '''si la lista está en el ultimo audio de la lista se regresa al primer valor de la lista'''
    def siguiente(self):
        self.i=self.i+1 
        '''Si el valor i es menor al tamaño de la lista se debe
        de detener y pasar al siguiente valor de la lista y reproducirlo'''
        if(self.i<len(self.n)):
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
            '''En caso contrario, significa que se llegó al límite de la lista
            y se debe de reiniciar desde cero'''
        else:
            self.i=0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.n[self.i])
            pygame.mixer.music.play()
            
    def anterior(self):
        self.i=self.i-1
        if(self.i>=0):
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
            
        else:
            self.i=len(self.n)-1#Al índice se le asigna el tamaño de la lista menos 1
            pygame.mixer.music.stop()#Detiene el archivo de audio cargado
            pygame.mixer.music.load(self.n[self.i])#Carga el nuevo archivo de audio de la lista
            pygame.mixer.music.play()#Se reproduce el archivo de audio
    """Sale del menú de audio"""
    def salir(self):
        self.ventana.destroy()#Destruye la ventana
        self.aux=False#El atributo aux se pone en falso, este
                        #se utilizará en otro método, para terminar
                        #la secuencia de un hilo
        pygame.mixer.music.stop()#Se detiene la pista
    def devolver(self):
        return self.aux
    def devolveri(self):
        return self.i#Regresa i
    def poneri(self,a):
        self.i=a#Pone i

def concatena(n):
    for i in range(len(n)):
        contenido=os.listdir('/media/pi/')#Se obtiene el contenido
                                            #de la carpeta /media/pi
                                            #para obtener el nombre de la memoria USB
        n[i]="/media/pi/"+contenido[0]+"/"+n[i]#Se concatena el nombre del archivo
                                                #con la ruta completa de los archivos de la memoria USB
    return n #Regresa la nueva lista

#Ventana Fotos
class Ventana4:
    #Constructor de Ventana para el control de imágenes
    def __init__(self,ventana,n):
        self.ventana=ventana
        self.i=0
        self.n=n
        
        ventana.title("Reproductor de Imagenes")
        ventana.geometry("700x400")
        ventana['background']='#000000'
        
        self.media=vlc.MediaPlayer(self.n[self.i])
        self.media.play()
        
        self.bSiguiente = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/next.png').resize((100, 100)))
        self.botonSiguiente = Button(ventana, image = self.bSiguiente, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.siguiente).place(x=400,y=100)

        self.bAnterior = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/prev.png').resize((100, 100)))
        self.botonAnterior = Button(ventana, image = self.bAnterior, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.anterior).place(x=200,y=100)
        
        self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
        self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=300,y=250)
        
    '''Adelanta a la siguiente imagen de la lista, si i llega al valor de tamaño de la
    lista+1 el indice de la lista se reinicia(i=0)'''
    def siguiente(self):
        self.media.stop()#Detiene el contenido multimedia
        self.i=self.i+1#Incrementa el valor del índice en 1
        '''Si el valor es menor al tamaño de la lista solo
        carga el siguiente valor de la lista y la reproduce'''
        if(self.i<len(self.n)):
            self.media=vlc.MediaPlayer(self.n[self.i])#Carga el valor de n[i] para poder
                                                    #utilizarlo en el reproductor multimedia
            self.media.play()#Reproduce el archivo
            '''Sino se reinicia el valor de i en 0 se carga el valor
            de la lista y la reproduce'''
        else:
            self.i=0#Reinicia indice
            self.media=vlc.MediaPlayer(self.n[self.i])#Carga el valor de n[i] para poder
                                                    #utilizarlo en el reproductor multimedia
            self.media.play()#Reproduce el archivo
    '''Retrocede a la anterior imagen de la lista, si i es menor a cero
    el valor de i toma el valor del tamaño de la lista-1, para reproducir la última imagen de la lista'''
    def anterior(self):
        self.i=self.i-1#Se decrementa i en uno
        self.media.stop()#Se detiene el contenido multimedia
        if(self.i>=0):
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo multimedia
                                                        #para reproducirlo
            self.media.play()#Se reproduce el archivo
        else:
            self.i=len(self.n)-1#El valor de i toma el valor de tamaño de la lista-1
            self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo multimedia
                                                        #para reproducirlo
            self.media.play()#Se reproduce el archivo
    '''Sale del reproductor de imágenes'''
    def salir(self):
        self.ventana.destroy()#Destruye la ventana
        self.media.stop()#Detiene el contenido multimedia
        
#Ventana Video        
class Ventana5:
    def __init__(self,ventana,n):
        self.ventana=ventana
        self.i=0
        self.aux=True
        self.ban=True
        self.n=n
        ventana.title("Reproductor de video")
        ventana.geometry("700x400")
        ventana['background']='#000000'
        self.media=vlc.MediaPlayer(self.n[self.i])#Se crea el objeto media, con el
                                                #el archivo de la lista n en su posición i
        self.media.play()#Se manda a reproducir el archivo
        
        self.bMusica = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/play.png').resize((100, 100)))
        self.botonMusica = Button(ventana, image = self.bMusica, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.play).place(x=300,y=100)

        self.bSiguiente = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/next.png').resize((100, 100)))
        self.botonSiguiente = Button(ventana, image = self.bSiguiente, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.siguiente).place(x=400,y=100)

        self.bAnterior = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/prev.png').resize((100, 100)))
        self.botonAnterior = Button(ventana, image = self.bAnterior, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.anterior).place(x=200,y=100)
        
        self.exit = ImageTk.PhotoImage(Image.open(r'/home/pi/Documents/CentroMultimedia/Imagenes/exit.png').resize((100, 100)))
        self.botonSalir = Button(ventana, image = self.exit, width= 100, height=100,relief="flat", borderwidth=0, bg='#000000', command=self.salir).place(x=300,y=250)

    def play(self):
        '''Si ban es True el video esta reproduciéndose y se quiere pausar'''
        if(self.ban==True):
            self.media.set_pause(1)#Se pausa el video
            self.ban=False#La bandera se pone en False para que cuando se
                            #oprima el botón ahora reanude el video
        else:
            self.media.play()#Se reanuda el video
            self.ban=True#La bandera se pone en True para que cuando se
                            #oprima el botón ahora pause el video
    def siguiente(self):
       self.media.stop()#Detiene el contenido
       self.i=self.i+1#Incrementa en uno el índice
       if(self.i<len(self.n)):
         self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo de video en un
                                                   #nuevo objeto MediaPlayer
         self.media.play()#Reproduce el archivo multimedia
       else:
         self.i=0#Reinicia el valor de i en cero
         self.media=vlc.MediaPlayer(self.n[self.i])#Se carga el archivo de video en un
                                                    #nuevo objeto MediaPlayer
         self.media.play()#Reproduce el archivo multimedia
    '''El método reto sirve para que al presionar atrasa, el reproductor cargue
    el siguiente video de la memoria y lo reproduzca, si la lista está en el
    primer video de la lista se va al último valor de la lista'''
    def anterior(self):
        self.i=self.i-1
        self.media.stop()
        '''Si el valor i es mayor o igual a 0 se debe
        de detener y pasar al anterior valor de la lista y reproducirlo'''
        if(self.i>=0):
            self.media=vlc.MediaPlayer(self.n[self.i])
            self.media.play()
            '''En caso contrario, significa que i vale 0 y por ende al disminuirlo en 1
            se obtiene un índice negativo generando un error, por ende, se debe de reiniciar desde el ultimo
            valor de la lista'''
        else:
            self.i=len(self.n)-1
            self.media=vlc.MediaPlayer(self.n[self.i])
            self.media.play()
    def salir(self):
        self.ventana.destroy()#Destruye la ventana
        self.media.stop()#Detiene el video
        
def buscar(a,fichero):
    for i in range(len(a)):#Recorre la lista a
        if fichero.endswith(a[i]):#Revisa si el archivo termina con una extensión dada por la lista a
            return True#Regresa un valor de True si el archivo termina con una extensión de la lista a
    return False#Si el archivo no tiene una extensión valida regresa un false

def encontrar(entrada):
    contenido2=os.listdir('/media/pi/')#Se lista el contenido de la carpeta /media/pi
    '''Se lista el directorio para saber si está conectado alguna USB, si la lista esta
    vacía regresa una lista vacía'''
    if len(contenido2)==0:#Si la lista contenido 2 esta vacía
        return contenido2 #Regresa una lista vacía
    '''Si está conectada una memoria la variable contenido tiene la lista de los
    nombres de las carpetas de las USB. Se escoge la primera USB y
    se concatena con /media/pi/ para obtener el contenido de la USB'''
    contenido=os.listdir('/media/pi/'+contenido2[0])#Se obtiene el contenido de /media/pi+contenido2[0]
    arreglo=[]#Arreglo sera una lista vacía
    """Revisa todos los archivos de la memoria y verifica si
        es un archivo y si cumple con la extensión
        que está determinada por la lista entrada"""
    for fichero in contenido:# Se recorre la lista contenido
                            #con cada cadena fichero de la lista contenido
        if os.path.isfile(os.path.join('/media/pi/'+contenido2[0],fichero))and buscar(entrada,fichero): #Si la ruta de /media/Pi+contenido2[0] es un archivo
                                                                                                        #y el método buscar regresa un True
            arreglo.append(fichero)#La lista arreglo agrega el valor de fichero
    return arreglo#Regresa la lista arreglo

def incrementar(num,**datos):
    while (datos['inicio'].devolver()):#Cuando se oprima el botón salir
                                        #devolver regresara un falso, mientras
                                        #se realizará este ciclo
        #print(pygame.mixer.music.get_busy())
        if(pygame.mixer.music.get_busy()==0):#Pregunta si no se esta reproduciendo algo
            a=datos['inicio'].devolveri()#Se obtiene del objeto de la clase ventana i y se guarda en a
            '''Se analiza si el valor de i llego al tamaño del arreglo menos 1'''
            if(a==len(datos['arreglo'])-1):
                a=-1#Se le asigna -1 a "a"
            a=a+1#Se incrementa el índice para obtener el siguiente audio
            datos['inicio'].poneri(a)#Se poner el valor de i en el objeto de la clase ventana
                                    #para que pueda ser usado por los métodos de los botones
            pygame.mixer.music.load(datos['arreglo'][a])#Carga el nuevo archivo de audio
            pygame.mixer.music.play()#Reproduce el audio
            '''Así cuando termina de reproducirse un audio comienza el otro'''
    '''Cuando se sale de la ventana se debe detener el audio'''
    pygame.mixer.music.stop()#Detiene el audio
    pygame.mixer.quit()#Elimina el objeto que permitía reproducir música
                        #para poder recuperar el audio que este acaparaba

bandera=True
while(bandera):
    
    root=Tk()
    a=0
    root.attributes("-zoomed",True)
    vent=Ventana(root)
    root.mainloop()
    valor=vent.dev()

    #Valor=0 indica lectura de memoria USB
    if valor==0:
        r=[".mp3"]
        arr=encontrar(r)
        b=[".mp4"]
        arr2=encontrar(b)
        c=[".jpg",".png",".jfif",".jpeg"]
        arr3=encontrar(c)
        
        '''Se analiza si solo se contiene un solo tipo de
        archivos, entiendase archivos como video, musica o imagenes.Para
        pasar directamente a reproducir ese tipo de archivos'''
        if len(arr)!=0 and len(arr2)==0 and len(arr3)==0:
            a=1
        elif len(arr)==0 and len(arr2)!=0 and len(arr3)==0:
            a=3
        elif len(arr)==0 and len(arr2)==0 and len(arr3)!=0:
            a=2
            '''En dado que no sea el caso, se debe de lanzar la segunda
            ventana para elegir que archivo reproducirá'''
        else:
            root=Tk()
            a=0
            root.attributes("-zoomed",True)
            vent=Ventana2(root,a)

            root.mainloop()
            a=vent.regresa()#Este valor determina que archivo se
                            #reproducirá
        '''a==1 es audio'''
        if a==1:
            ent=pygame.mixer.init()
            a=[".mp3"]
            arr=encontrar(a)
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de los audios
            vent=Ventana3(root,arr)
            '''Se instancia un hilo, para poder ejecutar el método para reproducir cuando
            se acabe un audio el siguiente audio'''
            inicia=threading.Thread(target=incrementar,args=(2,),kwargs={'inicio':vent,'arreglo':arr})
            inicia.start()#Inicia hilo
            root.mainloop()#Loop de la ventana hasta que se elimine
            '''a==2 imágenes'''
        elif a==2:
            a=['.jpg','.png','.jfif','jpeg']#Lista con la extensión de los archivos permitidos para imágenes
            arr=encontrar(a)#Se encuentra la lista de los nombres de los archivos validos
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de las imágenes
            vent=Ventana4(root,arr)
            root.mainloop()
            '''a==3 video'''
        elif a==3:
            a=['.mp4']#Lista con la extensión de los archivos permitidos para videos
            arr=encontrar(a)#Se encuentra la lista de los nombres de los archivos validos
            root=Tk()
            a=0
            arr=concatena(arr)#Obtiene la lista con las rutas completas de los archivos
                                #de los videos
            vent=Ventana5(root,arr)
            root.mainloop()
        '''Se eligio Netflix'''
    elif(valor==1):
        comando="/usr/bin/chromium-browser %s"
        nav=webbrowser.get(comando)#Se utiliza el método get para obtener el navegador
        webbrowser.register("chrome",None,nav)#Con este método se registra el navegador Chrome
                                                #con el nombre de chrome
        nav=webbrowser.get("chrome")#Se obtiene el navegador para utilizarlo
        nav.open("https://www.netflix.com/mx/login")
        
    elif(valor==2):
        comando="/usr/bin/chromium-browser %s"
        nav=webbrowser.get(comando)
        webbrowser.register("chrome",None,nav)
        nav=webbrowser.get("chrome")
        nav.open("https://accounts.spotify.com/es/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=es-MX")#Con esta instrucción se abre la pagina
                                                      
    elif(valor==3):
        comando="/usr/bin/chromium-browser %s"
        nav=webbrowser.get(comando)
        webbrowser.register("chrome",None,nav)
        nav=webbrowser.get("chrome")
        nav.open("https://www.primevideo.com/")
    
    elif(valor==4):
        comando="/usr/bin/chromium-browser %s"
        nav=webbrowser.get(comando)
        webbrowser.register("chrome",None,nav)                                                
        nav=webbrowser.get("chrome")
        nav.open("https://www.disneyplus.com/es-mx")
    
    else:
        bandera=False#Para terminar con el ciclo while