import tkinter as tk

class Finestra:
	def __init__(self):
		self.finestra = tk.Tk()
		self.finestra.geometry("400x300")
		self.finestra.title("Esempio Menu Tkinter")
        
		self.crea_widgets()
        
		self.finestra.mainloop()
        
	def crea_widgets(self):
		# creo il frame per il menù
		menubar = tk.Menu(self.finestra)
        
		# creo la voce di menù "File" con due sottomenu
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Apri", command=self.apri_file)
		filemenu.add_command(label="Salva", command=self.salva_file)
		filemenu.add_separator()
		filemenu.add_command(label="Esci", command=self.finestra.quit)
		menubar.add_cascade(label="File", menu=filemenu)
        
		# creo la voce di menù "Aiuto" con un sottomenu
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Info", command=self.info)
		menubar.add_cascade(label="Aiuto", menu=helpmenu)
        
		# configuro la finestra per usare il menù appena creato
		self.finestra.config(menu=menubar)
        
	def apri_file(self):
		print("Apre un file")
        
	def salva_file(self):
		print("Salva un file")
        
	def info(self):
		print("Informazioni sull'app")
        

Finestra()


	

