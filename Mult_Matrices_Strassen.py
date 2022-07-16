from tkinter import*
from tkinter import messagebox
from random import*
from time import time

#Variables globales
arrA = []
arrB = []
arrC = []
textA = NONE
textB = NONE
textC = NONE
textCC = NONE
cerrar = False

"""
	Funciones del  Algoritmo de Strassen
"""
# divide una matriz en 4 submatrices
def splitM(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    x_middle = rows // 2
    y_middle = columns // 2
    matrix_11 = [M[:x_middle] for M in matrix[:y_middle]]
    matrix_12 = [M[x_middle:] for M in matrix[:y_middle]]
    matrix_21 = [M[:x_middle] for M in matrix[y_middle:]]
    matrix_22 = [M[x_middle:] for M in matrix[y_middle:]]
    return matrix_11, matrix_12, matrix_21, matrix_22

# suma de matrices
def add_m(A, B):
	longA = len(A)
	arrT = [[0]*longA for _ in range(longA)]
	for k in range(longA):
		for i in range(longA):
			arrT[k][i] = A[k][i]+B[k][i]
	return arrT

# resta de matrices
def sub_m(A, B):
	longA = len(A)
	arrT = [[0]*longA for _ in range(longA)]
	for k in range(longA):
		for i in range(longA):
			arrT[k][i] = A[k][i]-B[k][i]
	return arrT

# matriz vacia de filxcol
def new_m(fil, col):
    return [[] for _ in range(col)]

# unir 4 submatrices
def matrix_merge(matrix_11, matrix_12, matrix_21, matrix_22):
		matrix_total = []
		rows1 = len(matrix_11)
		rows2 = len(matrix_21)
		for i in range(rows1):
			matrix_total.append(matrix_11[i]+matrix_12[i])
		for j in range(rows2):
			matrix_total.append(matrix_21[j]+matrix_22[j])
		return matrix_total

# algoritmo principal de strassen
def strassen(matrix_a, matrix_b):
	q = len(matrix_a)
	if q==1:
		d = [[0]]
		d[0][0] = matrix_a[0][0] * matrix_b[0][0]
		return d
	else:
		a,b,c,d = splitM(matrix_a)
		e,f,g,h = splitM(matrix_b)
		P11 = sub_m(f,h)
		P21 = add_m(a,b)
		P31 = add_m(c,d)
		P41 = sub_m(g,e)
		P51 = add_m(a,d)
		P52 = add_m(e,h)
		P61 = sub_m(b,d)
		P62 = add_m(g,h)
		P71 = sub_m(a,c)
		P72 = add_m(e,f)
		
		P1 = strassen(a, P11)
		P2 = strassen(P21, h)
		P3 = strassen(P31, e)
		P4 = strassen(d, P41)
		P5 = strassen(P51, P52)
		P6 = strassen(P61, P62)
		P7 = strassen(P71, P72)
		
		r = add_m(sub_m(add_m(P5, P4), P2), P6)
		s = add_m(P1, P2)
		t = add_m(P3, P4)
		u = sub_m(sub_m(add_m(P5,P1),P3),P7)
		matrix_product = matrix_merge(r,s,t,u)
		return matrix_product

# metodo tradicional para resolver matrices
def MetodoTradicional(matrix_a, matrix_b):
	filasA = len(matrix_a)
	columnasB = len(matrix_b[0])
	filasB = len(matrix_b)
	R=[[0 for x in range(columnasB)] for y in range(filasA)]

	for i in range(filasA):
		for j in range(columnasB):
			for k in range(filasB):
				R[i][j] += matrix_a[i][k] * matrix_b[k][j]
	return R

# valida la entrada correcta de datos
def validar(str1):
	if("x" not in str1): return True
	lugarX = str1.index("x")
	Nro1 = str1[:lugarX]
	Nro2 = str1[lugarX+1:]
	if(Nro1 == "" or Nro2 == ""): return True
	Nros = "0123456789"
	for k1 in Nro1:
		if(k1 not in Nros): return True
	for k2 in Nro2:
		if(k2 not in Nros): return True
	return False

# obtiene numero del formato filxcol
def obtenerNro(str1):
	lugarX = str1.index("x")
	Nro1T = str1[:lugarX]
	Nro2T = str1[lugarX+1:]
	Nro1 = int("".join(Nro1T))
	Nro2 = int("".join(Nro2T))
	return Nro1,Nro2

"""
	Funciones de los formularios
"""
# multiplicar unicamente con el metodo tradicional
def MultiplicarMatricesT():
	global arrA, arrB, arrC
	global textC
	filA, colA = obtenerNro(tamañoMatrizA.get())
	filB, colB = obtenerNro(tamañoMatrizB.get())

	# matrices de filxcol de 0's
	matriz_A = [[0 for k in range(colA)] for k in range(filA)]
	matriz_B = [[0 for k in range(colB)] for k in range(filB)]

	# multplicar matrices con el metodo tradicional
	# recuperar valores de los formularios
	for i in range(filA):
		for j in range(colA):
			matriz_A[i][j] = int(arrA[i][j].get())
	for i in range(filB):
		for j in range(colB):
			matriz_B[i][j] = int(arrB[i][j].get())

	# Metodo tradicional para multiplicar matrices
	tiempoMNormalT.set("")
	start_time2 = time() #Inicio
	matriz_Ct = MetodoTradicional(matriz_A, matriz_B)
	elapsed_time2= time() - start_time2 #Fin
	messagebox.showinfo(message="Termino la ejecución por \nel método tradicional", title="Exito")
	tiempoMNormalT.set(elapsed_time2)
	strCt = ''
	if(colA>8 or colB>8):
		textC.delete("1.0","end")
	for k1 in range(filA):
		for k2 in range(colB):
			Nrot = matriz_Ct[k1][k2]
			arrC[k1][k2].set(Nrot)
			totalDig = len(str(Nrot))
			if(colA>8):
				strCt+=' '*(4-totalDig) + str(Nrot)+' '
		if(colA>8): strCt+='\n'
	if(colA>8):
		textC.insert('insert', strCt)

def MultiplicarMatrices():
	global arrA, arrB, arrC, textCC
	global textC
	# matrices de AxA de 0's
	matriz_A = [[0 for k in range(len(arrA))] for k in range(len(arrA))]
	matriz_B = [[0 for k in range(len(arrB))] for k in range(len(arrB))]
	# recuperar valores de los formularios
	for i in range(len(arrA)):
		for j in range(len(arrB)):
			matriz_A[i][j] = int(arrA[i][j].get())
			matriz_B[i][j] = int(arrB[i][j].get())

	# Metodo tradicional para multiplicar matrices
	tiempoMStrassen.set("")
	start_time2 = time() #Inicio
	matriz_Ct = MetodoTradicional(matriz_A, matriz_B)
	elapsed_time2= time() - start_time2 #Fin
	messagebox.showinfo(message="Termino la ejecución por \nel método de Straseen", title="Exito")
	tiempoMStrassen.set(elapsed_time2)
	strCt = ''
	if(int(tamañoMatriz.get())>8):
		textC.delete("1.0","end")
	for k1 in range(len(arrC)):
		for k2 in range(len(arrC)):
			Nrot = matriz_Ct[k1][k2]
			arrC[k1][k2].set(Nrot)
			totalDig = len(str(Nrot))
			if(int(tamañoMatriz.get())>8):
				strCt+=' '*(4-totalDig) + str(Nrot)+' '
		if(int(tamañoMatriz.get())>8): strCt+='\n'
	if(int(tamañoMatriz.get())>8):
		textC.insert('insert', strCt)

	# Metodo Strassen para multiplicar matrices
	tiempoMNormal.set("")
	start_time1 = time() #Inicio
	matriz_Cs = strassen(matriz_A, matriz_B)
	elapsed_time1= time() - start_time1 #Fin
	messagebox.showinfo(message="Termino la ejecución por \nel método tradicional", title="Exito")
	tiempoMNormal.set(elapsed_time1)
	if(int(tamañoMatriz.get())>8):
		textCC.delete("1.0","end")
		textCC.insert('insert', strCt)

# llenar los matrices con numeros aleatorios entre (0,100)
def GenerarAleatorio1():
	global arrA, arrB
	global textA, textB
	tiempoMNormal.set("")
	tiempoMStrassen.set("")
	strAt = ''
	strBt = ''
	if(int(tamañoMatriz.get())>8):
		textA.delete("1.0","end")
		textB.delete("1.0","end")

	for k1 in range(len(arrA)):
		for k2 in range(len(arrB)):
			nroRandomA = randint(0,99)
			nroRandomB = randint(0,99)
			arrA[k1][k2].set(nroRandomA)
			arrB[k1][k2].set(nroRandomB)
			if(int(tamañoMatriz.get())>8):
				strAt+=' '*(nroRandomA//10 < 1) + str(nroRandomA)+' '
				strBt+=' '*(nroRandomB//10 < 1) + str(nroRandomB)+' '
		if(int(tamañoMatriz.get())>8):
			strAt+='\n'
			strBt+='\n'
	if(int(tamañoMatriz.get())>8):
		textA.insert('insert', strAt)
		textB.insert('insert', strBt)

def GenerarAleatorio2():
	global arrA, arrB
	global textA, textB
	strAt = ''
	strBt = ''
	filA, colA = obtenerNro(tamañoMatrizA.get())
	filB, colB = obtenerNro(tamañoMatrizB.get())
	if(colA>8 or colB>8):
		textA.delete("1.0","end")
		textB.delete("1.0","end")
	for k1 in range(filA):
		for k2 in range(colA):
			nroRandomA = randint(0,99)
			arrA[k1][k2].set(nroRandomA)
			if(colA>8):
				strAt+=' '*(nroRandomA//10 < 1) + str(nroRandomA)+' '
		if(colA>8): strAt+='\n'

	for k1 in range(filB):
		for k2 in range(colB):
			nroRandomB = randint(0,99)
			arrB[k1][k2].set(nroRandomB)
			if(colB>8):
				strBt+=' '*(nroRandomB//10 < 1) + str(nroRandomB)+' '
		if(colB>8): strBt+='\n'
	if(colA>8 or colB>8):
		textA.insert('insert', strAt)
		textB.insert('insert', strBt)

# dibujar tablas de ingreso de matrices M. tradicional y Strassen
def Tablas():
	global arrA, arrB, arrC
	global textA, textB, textC, textCC
	valPermitidos = [2**x for x in range(14)] # funciona para 2^n
	if(tamañoMatriz.get()==''): # si no se ingresa un numero
		messagebox.showerror(message="Ingrese un valor valido", title="Error")
	elif(int(tamañoMatriz.get()) not in valPermitidos): # si el valor ingresado no esta permitido
		tamañoMatriz.set("")
		messagebox.showerror(message="""Ingrese una potencia de 2\nEjemplo: 1,2,4,8,16,32,64,...""", title="Error")
	else:
		"""
			Elementos de la rubraiz
		"""
		raizMatrices = Toplevel(raizPrincipal)
		raizPrincipal.iconify()
		raizMatrices.title("Ingresar Matrices")
		raizMatrices.geometry('1150x700')
		raizMatrices.resizable(0, 0)
	    
	    # Titulos de la subraiz
		Titulo1 = Label(raizMatrices, text="Ingrese las matrices:")
		Titulo1.place(x=10, y=20)
		Titulo1.config(fg="#0B4069",
	             font=("Consolas",18))

		TituloResul = Label(raizMatrices, text="Resultados:")
		TituloResul.place(x=810, y=20)
		TituloResul.config(fg="#37359C",
	             font=("Consolas",18))

		TiempoTrad = Label(raizMatrices, text="Tiempo Metodo tradicional (seg):")
		TiempoTrad.place(x=780, y=100)
		TiempoTrad.config(fg="#37359C",
	             font=("Consolas",12))

		val_TiempoTrad = Entry(raizMatrices, justify=CENTER, textvariable=tiempoMNormal, state="disabled")
		val_TiempoTrad.place(x = 780, y = 125)

		TiempoStr = Label(raizMatrices, text="Tiempo Metodo Strassen (seg):")
		TiempoStr.place(x=780, y=200)
		TiempoStr.config(fg="#37359C",
	             font=("Consolas",12))

		val_TiempoStr = Entry(raizMatrices, justify=CENTER, textvariable=tiempoMStrassen, state="disabled")
		val_TiempoStr.place(x = 780, y = 225)

		# Total de campos de entrada
		totalLabel = int(tamañoMatriz.get())

		# variables Matriz A
		TituloA = Label(raizMatrices, text="A = ")
		TituloA.place(x=10, y=75)
		TituloA.config(fg="#71102E",
	             font=("Arial",32))

		tiempoMNormal.set("")
		tiempoMStrassen.set("")

		arrA = [[] for i in range(totalLabel)]
		for k1 in range(totalLabel):
			for k2 in range(totalLabel):
				arrA[k1].append(StringVar())

		# variables B
		TituloB = Label(raizMatrices, text="B = ")
		TituloB.place(x=400, y=75)
		TituloB.config(fg="#71102E",
	             font=("Arial",32))

		arrB = [[] for i in range(totalLabel)]
		for k1 in range(totalLabel):
			for k2 in range(totalLabel):
				arrB[k1].append(StringVar())

		# variables C
		arrC = [[] for i in range(totalLabel)]
		for k1 in range(totalLabel):
			for k2 in range(totalLabel):
				arrC[k1].append(StringVar())

		if(totalLabel in [1,2,4,8]):

			arrCT = arrC.copy()
			# Matriz A
			for i1 in range(totalLabel):
				for i2 in range(totalLabel):
					Nro = Entry(raizMatrices, justify=CENTER, textvariable=arrA[i1][i2])
					Nro.place(x = 100+30*i2, y = 80+30*i1, width=25,height=25)

			# Matriz B
			for i1 in range(totalLabel):
				for i2 in range(totalLabel):
					Nro = Entry(raizMatrices, justify=CENTER, textvariable=arrB[i1][i2])
					Nro.place(x = 490+30*i2, y = 80+30*i1, width=25,height=25)

			# Matriz C
			for i1 in range(totalLabel):
				for i2 in range(totalLabel):
					Nro = Entry(raizMatrices, justify=CENTER, textvariable=arrC[i1][i2], state="disabled")
					Nro.place(x = 100+40*i2, y = 425+30*i1, width=35,height=25)

			# Matriz CT
			for i1 in range(totalLabel):
				for i2 in range(totalLabel):
					Nro = Entry(raizMatrices, justify=CENTER, textvariable=arrCT[i1][i2], state="disabled")
					Nro.place(x = 490+40*i2, y = 425+30*i1, width=35,height=25)

			# simbolo X y =
			if(totalLabel == 4):
				TituloX = Label(raizMatrices, text="X")
				TituloX.place(x=300, y=110)
				TituloX.config(fg="#71102E",
			             font=("Arial",32))
			elif(totalLabel == 8):
				TituloX = Label(raizMatrices, text="X")
				TituloX.place(x=350, y=170)
				TituloX.config(fg="#71102E",
			             font=("Arial",32))
			elif(totalLabel == 2 or totalLabel == 1):
				TituloX = Label(raizMatrices, text="X")
				TituloX.place(x=250, y=80)
				TituloX.config(fg="#71102E",
			             font=("Arial",32))
		else:

			TituloX = Label(raizMatrices, text="X")
			TituloX.place(x=355, y=170)
			TituloX.config(fg="#71102E",
			             font=("Arial",32))

			# Matriz A
			xscrollbarA = Scrollbar(raizMatrices, orient=HORIZONTAL)
			xscrollbarA.place(x=100,y=320,width=240)

			yscrollbarA = Scrollbar(raizMatrices, orient=VERTICAL)
			yscrollbarA.place(x=340,y=80,height=240)

			textA = Text(raizMatrices,wrap=NONE,
			            xscrollcommand=xscrollbarA.set,
			            yscrollcommand=yscrollbarA.set)
			textA.place(x=100, y=80, width=240,height=240)

			xscrollbarA.config(command=textA.xview)
			yscrollbarA.config(command=textA.yview)

			# Matriz B
			xscrollbarB = Scrollbar(raizMatrices, orient=HORIZONTAL)
			xscrollbarB.place(x=490,y=320,width=240)

			yscrollbarB = Scrollbar(raizMatrices, orient=VERTICAL)
			yscrollbarB.place(x=730,y=80,height=240)

			textB = Text(raizMatrices,wrap=NONE,
			            xscrollcommand=xscrollbarB.set,
			            yscrollcommand=yscrollbarB.set)
			textB.place(x=490, y=80, width=240,height=240)

			xscrollbarB.config(command=textB.xview)
			yscrollbarB.config(command=textB.yview)

			# Matriz C Strassen
			xscrollbarC = Scrollbar(raizMatrices, orient=HORIZONTAL)
			xscrollbarC.place(x=100,y=665,width=240)

			yscrollbarC = Scrollbar(raizMatrices, orient=VERTICAL)
			yscrollbarC.place(x=340,y=425,height=240)

			textC = Text(raizMatrices,wrap=NONE,
			            xscrollcommand=xscrollbarC.set,
			            yscrollcommand=yscrollbarC.set)
			textC.place(x=100, y=425, width=240,height=240)

			xscrollbarC.config(command=textC.xview)
			yscrollbarC.config(command=textC.yview)

			#  Matriz C tradicional
			xscrollbarC = Scrollbar(raizMatrices, orient=HORIZONTAL)
			xscrollbarC.place(x=490,y=665,width=240)

			yscrollbarC = Scrollbar(raizMatrices, orient=VERTICAL)
			yscrollbarC.place(x=730,y=425,height=240)

			textCC = Text(raizMatrices,wrap=NONE,
			            xscrollcommand=xscrollbarC.set,
			            yscrollcommand=yscrollbarC.set)
			textCC.place(x=490, y=425, width=240,height=240)

			xscrollbarC.config(command=textCC.xview)
			yscrollbarC.config(command=textCC.yview)

		#Textos de resultados
		ResulStrassen = Label(raizMatrices, text="Resultado Straseen:")
		ResulStrassen.place(x=95, y=380)
		ResulStrassen.config(fg="#37359C",
	             font=("Consolas",18))
		ResulTrad = Label(raizMatrices, text="Resultado Tradicional:")
		ResulTrad.place(x=465, y=380)
		ResulTrad.config(fg="#37359C",
	             font=("Consolas",18))
		# Resolver matrices
		Button(raizMatrices, text='Resolver', command=MultiplicarMatrices).place(x=650, y=350)
		# generar numeros aleatorios
		Button(raizMatrices, text='Generar valores aleatorios', command=GenerarAleatorio1).place(x=15, y=350)

# dibujar tablas de ingreso de matrice M. tradicional
def TablasMT():
	global arrA, arrB, arrC
	global textA, textB, textC
	if(tamañoMatrizA.get()=='' or tamañoMatrizB.get()==''): # si no se ingresa un numero
		messagebox.showerror(message="Ingrese un valor valido", title="Error")
	elif(validar(tamañoMatrizA.get()) or validar(tamañoMatrizB.get())):
		messagebox.showerror(message="Revise la entrada\nFormato correcto: NroxNro", title="Error")
	else:
		filA, colA = obtenerNro(tamañoMatrizA.get())
		filB, colB = obtenerNro(tamañoMatrizB.get())
		if(colA!=filB):
			messagebox.showerror(message="REVISE LA ENTRADA:\nRecuerde que para multiplicar matrices\nel numero de columnas de A debe ser\nigual que el número de filas de B: \naxNro - Nroxb", title="Imposible multiplicar")
		else:
			"""
			Elementos de la rubraiz
			"""
			raizMatricesT = Toplevel(raizPrincipal)
			raizPrincipal.iconify()
			raizMatricesT.title("Ingresar Matrices")
			raizMatricesT.geometry('1500x400')
			raizMatricesT.resizable(0, 0)
		    
		    # Titulos de la subraiz
			Titulo1 = Label(raizMatricesT, text="Ingrese las matrices:")
			Titulo1.place(x=10, y=20)
			Titulo1.config(fg="#0B4069",
		             font=("Consolas",18))

			TituloResul = Label(raizMatricesT, text="Resultados:")
			TituloResul.place(x=1235, y=20)
			TituloResul.config(fg="#37359C",
		             font=("Consolas",18))

			# tiempo de ejecucion
			TiempoTrad = Label(raizMatricesT, text="Tiempo Metodo tradicional (seg):")
			TiempoTrad.place(x=1205, y=100)
			TiempoTrad.config(fg="#37359C",
		             font=("Consolas",12))

			val_TiempoTrad = Entry(raizMatricesT, justify=CENTER, textvariable=tiempoMNormalT, state="disabled")
			val_TiempoTrad.place(x = 1205, y = 125)

			# variables Matriz A
			TituloA = Label(raizMatricesT, text="A = ")
			TituloA.place(x=10, y=75)
			TituloA.config(fg="#71102E",
		             font=("Arial",32))
			# muestra el tamaño de la matriz A
			Label(raizMatricesT, text=str(filA)+"x"+str(colA)).place(x=20,y=120)

			arrA = [[] for i in range(filA)]
			for k1 in range(filA):
				for k2 in range(colA):
					arrA[k1].append(StringVar())

			# variables B
			TituloB = Label(raizMatricesT, text="B = ")
			TituloB.place(x=400, y=75)
			TituloB.config(fg="#71102E",
		             font=("Arial",32))
			# muestra el tamaño de la matriz B
			Label(raizMatricesT, text=str(filB)+"x"+str(colB)).place(x=410,y=120)
			# muestra el tamaño de la matriz C
			Label(raizMatricesT, text=str(filA)+"x"+str(colB)).place(x=800,y=120)

			arrB = [[] for i in range(filB)]
			for k1 in range(filB):
				for k2 in range(colB):
					arrB[k1].append(StringVar())

			# variables C
			arrC = [[] for i in range(filA)]
			for k1 in range(filA):
				for k2 in range(colB):
					arrC[k1].append(StringVar())

			if(colA<=8 and colB<=8):
				# Matriz A
				for i1 in range(filA):
					for i2 in range(colA):
						Nro = Entry(raizMatricesT, justify=CENTER, textvariable=arrA[i1][i2])
						Nro.place(x = 100+30*i2, y = 80+30*i1, width=25,height=25)

				# Matriz B
				for i1 in range(filB):
					for i2 in range(colB):
						Nro = Entry(raizMatricesT, justify=CENTER, textvariable=arrB[i1][i2])
						Nro.place(x = 490+30*i2, y = 80+30*i1, width=25,height=25)

				# Matriz C
				for i1 in range(filA):
					for i2 in range(colB):
						Nro = Entry(raizMatricesT, justify=CENTER, textvariable=arrC[i1][i2], state="disabled")
						Nro.place(x = 880+40*i2, y = 80+30*i1, width=35,height=25)

				TituloX = Label(raizMatricesT, text="X")
				TituloX.place(x=350, y=170)
				TituloX.config(fg="#71102E",
				             font=("Arial",32))
				Titulo_ = Label(raizMatricesT, text="=")
				Titulo_.place(x=775, y=160)
				Titulo_.config(fg="#71102E",
				             font=("Arial",48))
			else:
				TituloX = Label(raizMatricesT, text="X")
				TituloX.place(x=355, y=170)
				TituloX.config(fg="#71102E",
				             font=("Arial",32))
				Titulo_ = Label(raizMatricesT, text="=")
				Titulo_.place(x=775, y=160)
				Titulo_.config(fg="#71102E",
				             font=("Arial",48))

				# Matriz A
				xscrollbarA = Scrollbar(raizMatricesT, orient=HORIZONTAL)
				xscrollbarA.place(x=100,y=320,width=240)

				yscrollbarA = Scrollbar(raizMatricesT, orient=VERTICAL)
				yscrollbarA.place(x=340,y=80,height=240)

				textA = Text(raizMatricesT,wrap=NONE,
				            xscrollcommand=xscrollbarA.set,
				            yscrollcommand=yscrollbarA.set)
				textA.place(x=100, y=80, width=240,height=240)

				xscrollbarA.config(command=textA.xview)
				yscrollbarA.config(command=textA.yview)

				# Matriz B
				xscrollbarB = Scrollbar(raizMatricesT, orient=HORIZONTAL)
				xscrollbarB.place(x=490,y=320,width=240)

				yscrollbarB = Scrollbar(raizMatricesT, orient=VERTICAL)
				yscrollbarB.place(x=730,y=80,height=240)

				textB = Text(raizMatricesT,wrap=NONE,
				            xscrollcommand=xscrollbarB.set,
				            yscrollcommand=yscrollbarB.set)
				textB.place(x=490, y=80, width=240,height=240)

				xscrollbarB.config(command=textB.xview)
				yscrollbarB.config(command=textB.yview)

				# Matriz C
				xscrollbarC = Scrollbar(raizMatricesT, orient=HORIZONTAL)
				xscrollbarC.place(x=880,y=320,width=240)

				yscrollbarC = Scrollbar(raizMatricesT, orient=VERTICAL)
				yscrollbarC.place(x=1120,y=80,height=240)

				textC = Text(raizMatricesT,wrap=NONE,
				            xscrollcommand=xscrollbarC.set,
				            yscrollcommand=yscrollbarC.set)
				textC.place(x=880, y=80, width=240,height=240)

				xscrollbarC.config(command=textC.xview)
				yscrollbarC.config(command=textC.yview)

			# Resolver matrices
			Button(raizMatricesT, text='Resolver', command=MultiplicarMatricesT).place(x=750, y=350)
			# generar numeros aleatorios
			Button(raizMatricesT, text='Generar valores aleatorios', command=GenerarAleatorio2).place(x=15, y=350)

# Mulplicar matrices comparando los metodos de Strassen y Tradicional
def StraVSMetTrad():
	raizStraVSMT = Toplevel(raizPrincipal)
	raizPrincipal.iconify()
	raizStraVSMT.title("Multiplicación de Matrices Metodo Straseen vs Tradicional")
	raizStraVSMT.resizable(0, 0)
	raizStraVSMT.geometry('350x150')	
	# Titulos
	Titulo1 = Label(raizStraVSMT, text="Ingrese el tamaño de las matrices")
	Titulo1.place(x=15, y=25)
	Titulo1.config(fg="#240505",
	             font=("Consolas",12))
	Titulo2 = Label(raizStraVSMT, text="de entrada:")
	Titulo2.place(x=15, y=47)
	Titulo2.config(fg="#240505",
	             font=("Consolas",12))

	# Entrada del tamaño
	tamMatriz = Entry(raizStraVSMT, justify=CENTER, textvariable=tamañoMatriz)
	tamMatriz.place(x=135, y=70)

	#Boton iniciar proceso
	Button(raizStraVSMT, text='Ir', command=Tablas).place(x=270, y=68)

# Multiplicar matrices por metodo tradicional
def MetTrad():
	raizMT = Toplevel(raizPrincipal)
	raizPrincipal.iconify()
	raizMT.title("Multiplicación de Matrices Método Tradicional")
	raizMT.resizable(0, 0)
	raizMT.geometry('370x170')	
	# Titulos
	Titulo1 = Label(raizMT, text="Ingrese el tamaño de las matrices mxn: ")
	Titulo1.place(x=15, y=25)
	Titulo1.config(fg="#240505",
	             font=("Consolas",12))

	# Entrada del tamaño de matriz A
	Titulo2 = Label(raizMT, text="Matriz A:")
	Titulo2.place(x=55, y=70)

	tamMatrizA = Entry(raizMT, justify=CENTER, textvariable=tamañoMatrizA)
	tamMatrizA.place(x=135, y=70)

	# Entrada del tamaño de matriz B
	Titulo3 = Label(raizMT, text="Matriz B:")
	Titulo3.place(x=55, y=100)

	tamMatrizB = Entry(raizMT, justify=CENTER, textvariable=tamañoMatrizB)
	tamMatrizB.place(x=135, y=100)

	#Boton iniciar proceso
	Button(raizMT, text='Ir', command=TablasMT).place(x=270, y=80)


# Configuracion principal de la raiz
raizPrincipal = Tk()
raizPrincipal.title("Multiplicación de Matrices")
raizPrincipal.resizable(0, 0)
raizPrincipal.geometry('400x300')

#Variables
tamañoMatriz = StringVar()
tamañoMatriz.set('')
tamañoMatrizA = StringVar()
tamañoMatrizA.set('')
tamañoMatrizB = StringVar()
tamañoMatrizB.set('')
tiempoMNormal = StringVar()
tiempoMNormal.set('')
tiempoMStrassen = StringVar()
tiempoMStrassen.set('')
tiempoMNormalT = StringVar()
tiempoMNormalT.set('')
textoMatrizA = StringVar()
textoMatrizA.set('')

# Elementos de la raiz
Button(raizPrincipal, text='Salir', command=raizPrincipal.destroy).pack(side=BOTTOM)

botMulTradStra = Button(raizPrincipal, text='Método Tradicional \nvs \nMétodo Strassen', 
	command=StraVSMetTrad, compound="c",
	activeforeground="#7292BA", activebackground="#C7D4E7",
	cursor="hand2",
	relief="groove")
botMulTradStra.place(x=50, y=30, width=300, height=100)
botMulTradStra.config(fg="#1B416B", font=("Consolas",18))

botMulTrad = Button(raizPrincipal, text='Método Tradicional', 
	command=MetTrad, compound="c",
	activeforeground="#7292BA", activebackground="#C7D4E7",
	cursor="hand2",
	relief="groove")
botMulTrad.place(x=50, y=150, width=300, height=100)
botMulTrad.config(fg="#1B416B", font=("Consolas",18))

raizPrincipal.mainloop()