from tkinter import *
import customtkinter as ctk
root = ctk.CTk()

# Titulo
marco_0 =ctk.CTkFrame(root)
marco_0.grid(row=0,
            column=2,
            padx=30,
            pady=30)
Titulo = ctk.CTkLabel(marco_0,text="Ficha de inscripcion").pack()




#Marcos estudiantes

marco_estudiantes1 = ctk.CTkFrame(root)
marco_estudiantes1.grid(row=1,
            column=0,
            padx=15,
            pady=10
            )


marco_estudiantes2 = ctk.CTkFrame(root)
marco_estudiantes2.grid(row = 2,
            column = 0,
            padx=15,
            pady=10,
            )


marco_estudiantes3 = ctk.CTkFrame(root,)
marco_estudiantes3.grid(row=3,
            column=0,
            padx=15,
            pady=10
            )

marco_estudiantes4 = ctk.CTkFrame(root,)
marco_estudiantes4.grid(row=4,
            column=0,
            padx=15,
            pady=10
            )

marco_estudiantes5 = ctk.CTkFrame(root,)
marco_estudiantes5.grid(row=5,
            column=0,
            padx=15,
            pady=10
            )

#MARCOS PADRE
marco_padre1 = ctk.CTkFrame(root)
marco_padre1.grid(row=1,
            column=1,
            padx=15,
            pady=10
            )


marco_padre2 = ctk.CTkFrame(root)
marco_padre2.grid(row = 2,
            column = 1,
            padx=15,
            pady=10,
            )


marco_padre3 = ctk.CTkFrame(root,)
marco_padre3.grid(row=3,
            column=1,
            padx=15,
            pady=10
            )

marco_padre4 = ctk.CTkFrame(root,)
marco_padre4.grid(row=4,
            column=1,
            padx=15,
            pady=10
            )

marco_padre5 = ctk.CTkFrame(root,)
marco_padre5.grid(row=5,
            column=1,
            padx=15,
            pady=10
            )


#MARCO MADRE

marco_madre1 = ctk.CTkFrame(root)
marco_madre1.grid(row=1,
            column=3,
            padx=15,
            pady=10
            )


marco_madre2 = ctk.CTkFrame(root)
marco_madre2.grid(row = 2,
            column = 3,
            padx=15,
            pady=10,
            )


marco_madre3 = ctk.CTkFrame(root,)
marco_madre3.grid(row=3,
            column=3,
            padx=15,
            pady=10
            )

marco_madre4 = ctk.CTkFrame(root,)
marco_madre4.grid(row=4,
            column=3,
            padx=15,
            pady=10
            )

marco_madre5 = ctk.CTkFrame(root,)
marco_madre5.grid(row=5,
            column=3,
            padx=15,
            pady=10
            )

#MARCO REPRESENTANTE

marco_representante1 = ctk.CTkFrame(root)
marco_representante1.grid(row=1,
            column=4,
            padx=15,
            pady=10
            )


marco_representante2 = ctk.CTkFrame(root)
marco_representante2.grid(row = 2,
            column = 4,
            padx=15,
            pady=10,
            )


marco_representante3 = ctk.CTkFrame(root,)
marco_representante3.grid(row=3,
            column=4,
            padx=15,
            pady=10
            )

marco_representante4 = ctk.CTkFrame(root,)
marco_representante4.grid(row=4,
            column=4,
            padx=15,
            pady=10
            )

marco_representante5 = ctk.CTkFrame(root,)
marco_representante5.grid(row=5,
            column=4,
            padx=15,
            pady=10
            )






#Marco estudiantes DATOS

texto_pantalla2 = ctk.CTkLabel(marco_estudiantes1,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_estudiantes1,
                            placeholder_text="Apellidos y nombres",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_estudiantes2,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_estudiantes2,
                            placeholder_text="Fecha de nacimiento",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_estudiantes3,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_estudiantes3,
                            placeholder_text="Edad",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_estudiantes4,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_estudiantes4,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_estudiantes5,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_estudiantes5,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


# MARCO PADRE DATOS ###

texto_pantalla2 = ctk.CTkLabel(marco_padre1,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_padre1,
                            placeholder_text="Apellidos y nombres",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_padre2,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_padre2,
                            placeholder_text="Fecha de nacimiento",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_padre3,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_padre3,
                            placeholder_text="Edad",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_padre4,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_padre4,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_padre5,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_padre5,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


# MARCO MADRE DATOS

texto_pantalla2 = ctk.CTkLabel(marco_madre1,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_madre1,
                            placeholder_text="Apellidos y nombres",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_madre2,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_madre2,
                            placeholder_text="Fecha de nacimiento",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_madre3,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_madre3,
                            placeholder_text="Edad",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_madre4,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_madre4,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_madre5,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_madre5,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


# MARCO REPRESENTANTE DATOS

texto_pantalla2 = ctk.CTkLabel(marco_representante1,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_representante1,
                            placeholder_text="Apellidos y nombres",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_representante2,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_representante2,
                            placeholder_text="Fecha de nacimiento",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_representante3,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_representante3,
                            placeholder_text="Edad",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_representante4,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_representante4,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()


texto_pantalla2 = ctk.CTkLabel(marco_representante5,
                            text="Datos Estudiante")
texto_pantalla2.pack()
N_A_estudiante= entry= ctk.CTkEntry(marco_representante5,
                            placeholder_text="Lugar/Estado",)
N_A_estudiante.pack()




root.geometry('900x500')
root.mainloop()