import tkinter as tk

class Finestra:
	def __init__(self):
		self.finestra = tk.Tk()
		self.finestra.geometry("400x300")
		self.finestra.title("Esempio Menu Tkinter")
        
		self.crea_widgets()
        
		self.finestra.mainloop()
        
	def crea_widgets(self):
		# creo il frame per il menu
		menubar = tk.Menu(self.finestra)
        
		# creo la voce di menù "File" con due sottomenu
		# Prima devo creare le voci che voglio mettere all'interno del menu e successivamente aggiungo la cascata
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Apri", command=self.apri_file, activebackground="Green", background="Blue")
		filemenu.add_command(label="Salva", command=self.salva_file, activebackground="Green", background="Blue")
		filemenu.add_separator()
		filemenu.add_command(label="Esci", command=self.finestra.quit, activebackground="Red", background="Blue")
		menubar.add_cascade(label="File", menu=filemenu)
        
		# creo la voce di menù "Aiuto" con un sottomenu
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Info", command=self.info , activebackground="Green", background="Blue")
		menubar.add_cascade(label="Aiuto", menu=helpmenu)
		menubar.add_radiobutton(label="radio1")
		menubar.add_radiobutton(label="radio2")
		menubar.add_checkbutton(label="check1")
		menubar.add_checkbutton(label="check2")
        
		# configuro la finestra per usare il menù appena creato
		self.finestra.config(menu=menubar)
        
	def apri_file(self):
		print("Apre un file")
        
	def salva_file(self):
		print("Salva un file")
        
	def info(self):
		print("Informazioni sull'app")
        

Finestra()


	

