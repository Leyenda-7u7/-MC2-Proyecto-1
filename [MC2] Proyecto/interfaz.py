import tkinter as tk
from tkinter import messagebox
from grafo import generargrafo

from PIL import ImageTk, Image

#Se debe instalar el modulo pillow con el siguiente comando en consola ----> pip install Pillow

from prueba import recorridoancho


class GraphGenerator:
    
    FONDO_VENTANA = '#570CB3'
    FONDO_MENU = '#570CB3'
    
    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.root = tk.Tk()
        self.root.title("Generador de Grafos")
        self.canvas = tk.Canvas(self.root, width=800, height=400)
        self.canvas.pack(side=tk.TOP, padx=10, pady=10)
        self.frame = tk.Frame(self.root)
        self.root['bg'] = self.FONDO_VENTANA
        self.frame['bg'] = self.FONDO_MENU
        self.frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        
        self.button3 = tk.Button(self.frame, text="Agregar Vértice", command=self.agregar_vertice, font=("DejaVu Sans", 11),fg="white", bg="#3F00BD", width=13)
        self.button3.grid(row=1, column=0, padx=5, pady=5)
        
        self.entry1 = tk.Entry(self.frame, font=("DejaVu Sans", 11), width=13, )
        self.entry1.grid(row=1, column=1, padx=5, pady=5)
        
        self.button = tk.Button(self.frame, text="Arista (A--B)", command=self.agregar_arista, font=("DejaVu Sans", 11),fg="white", bg="#3F00BD", width=13)
        self.button.grid(row=2, column=0, padx=5, pady=5)
        
        self.entry2 = tk.Entry(self.frame,  font=("DejaVu Sans", 11), width=13)
        self.entry2.grid(row=2, column=1, padx=5, pady=5)
        
        self.listbox = tk.Listbox(self.frame,  font=("DejaVu Sans", 11), width=13)
        self.listbox.grid(row=1, column=2, rowspan=5, padx=5, pady=5)
        
        self.label4 = tk.Label(self.frame, text="Vertices", font=("Arial", 10),fg="white", bg="#250070", width=11)
        self.label4.grid(row=0, column=2, padx=5, pady=10)
        
        self.listbox1 = tk.Listbox(self.frame,  font=("DejaVu Sans", 11), width=13)
        self.listbox1.grid(row=1, column=5, rowspan=5, padx=5, pady=2)
        
        self.label5 = tk.Label(self.frame, text="Aristas", font=("Arial", 10),fg="white", bg="#250070", width=11)
        self.label5.grid(row=0, column=5, padx=5, pady=10)

        
        
        self.button2 = tk.Button(self.frame, text="Generar Grafo", command=self.generar_grafo, font=("DejaVu Sans", 12),fg="white", bg="#3F00BD", width=15)
        self.button2.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.grafo1 = tk.Label(self.root)
        self.grafo1.place(x=10, y=10)
        self.grafo2 = tk.Label(self.root)
        self.grafo2.place(x=414, y=10)

        self.separacion = tk.Label(self.root,height=200,bg='#570CB3',width=1,font=('Arial',1))
        self.separacion.place(x=410,y=10)
        
        self.root.mainloop()

    def agregar_vertice(self):
        vertice = self.entry1.get()
        if not vertice:
            messagebox.showerror("Error", "Por favor ingrese todos los campos")
            return
        if vertice in self.vertices:
            messagebox.showerror("Error", "No se pueden agregar vertices repetidos")
            return
        self.vertices.append(vertice)
        self.listbox.insert(tk.END, f"{vertice}")
        self.entry1.delete(0, 'end')

    def agregar_arista(self):
        arista = self.entry2.get()
        if not arista:
            messagebox.showerror("Error", "Por favor ingrese todos los campos")
            return
        if '--' not in arista:
            messagebox.showerror("Error", "La entrada tiene que tener el formato (X--Y)")
            return
        lis = arista.split('--')
        if lis[0] not in self.vertices:
            messagebox.showerror("Error", f'El vertice "{lis[0]}" no existe')
            return
        elif lis[1] not in self.vertices:
            messagebox.showerror("Error", f'El vertice "{lis[1]}" no existe')
            return
        elif lis[0] == lis[1]:
            messagebox.showerror("Error", 'Los vertices deben ser distintos')
            return
        invert = f'{lis[1]}--{lis[0]}'
        if invert in self.aristas or arista in self.aristas:
            messagebox.showerror("Error", "No se pueden agregar aristas repetidas")
            return
        self.aristas.append(arista)
        self.listbox1.insert(tk.END, f"{arista}")
        self.entry2.delete(0, 'end')

    def generar_grafo(self):
        if self.vertices == []:
            messagebox.showerror("Error", "No existen elementos para generar un grafo")
            return
        recorrido = recorridoancho(self.vertices, self.aristas)
        generargrafo(self.vertices,self.aristas,recorrido)
        img = ImageTk.PhotoImage(Image.open('Grafo.png').resize((396,400)))
        self.grafo1.config(image=img)
        self.grafo1.image = img
        img2 = ImageTk.PhotoImage(Image.open('Grafo2.png').resize((396, 400)))
        self.grafo2.config(image=img2)
        self.grafo2.image = img2

if __name__ == "__main__":
    graph_generator = GraphGenerator()
