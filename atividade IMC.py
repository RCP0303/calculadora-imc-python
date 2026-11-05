
import tkinter as tk
from tkinter import messagebox

# janela principal
janela = tk.Tk()

janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.geometry("650x350")
janela.resizable(False, False)


# funcao do calculo

def calcular():

    nome = entrada_nome.get()
    endereco = entrada_endereco.get()
    altura = entrada_altura.get()
    peso = entrada_peso.get()

    if nome == "" or endereco == "" or altura == "" or peso == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    try:
        altura = float(altura.replace(",", ""))
        peso = float(peso.replace(",", ""))

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite valores numéricos válidos para altura e peso!"
        )
        return

    if altura <= 0 or peso <= 0:
        messagebox.showerror(
            "Erro",
            "Altura e peso devem ser maiores que zero!"
        )
        return

    altura = altura / 100

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = "Abaixo do peso"

    elif imc < 25:
        classificacao = "Peso normal"

    elif imc < 30:
        classificacao = "Sobrepeso"

    elif imc < 35:
        classificacao = "Obesidade grau I"

    elif imc < 40:
        classificacao = "Obesidade grau II"

    else:
        classificacao = "Obesidade grau III"

    resultado.config(
        text=f"RESULTADO\n\n"
             f"Paciente: {nome}\n"
             f"Endereço: {endereco}\n"
             f"IMC: {imc:.2f}\n"
             f"Classificação: {classificacao}"
    )


# funcao para reiniciar

def reiniciar():
    entrada_nome.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)

    resultado.config(text="Resultado")


# funcao para sair

def sair():
    janela.destroy()


# campo de nome

label_nome = tk.Label(janela, text="Nome do Paciente:")
label_nome.grid(row=0, column=0, padx=10, pady=12, sticky="w")

entrada_nome = tk.Entry(janela, width=55)
entrada_nome.grid(row=0, column=1, columnspan=2, padx=5, pady=12)


# campo de endereco

label_endereco = tk.Label(janela, text="Endereço Completo:")
label_endereco.grid(row=1, column=0, padx=10, pady=12, sticky="w")

entrada_endereco = tk.Entry(janela, width=55)
entrada_endereco.grid(row=1, column=1, columnspan=2, padx=5, pady=12)


# campo da altura

label_altura = tk.Label(janela, text="Altura (cm):")
label_altura.grid(row=2, column=0, padx=10, pady=12, sticky="w")

entrada_altura = tk.Entry(janela, width=20)
entrada_altura.grid(row=2, column=1, padx=5, pady=12, sticky="w")


# campo do peso

label_peso = tk.Label(janela, text="Peso (Kg):")
label_peso.grid(row=3, column=0, padx=10, pady=12, sticky="w")

entrada_peso = tk.Entry(janela, width=20)
entrada_peso.grid(row=3, column=1, padx=5, pady=12, sticky="w")


# quadro de resultado

resultado = tk.Label(
    janela,
    text="Resultado",
    width=30,
    height=8,
    relief="solid",
    bd=1,
    font=("Arial", 10),
    justify="left",
    anchor="nw",
    padx=8,
    pady=8
)

resultado.grid(
    row=2,
    column=2,
    rowspan=2,
    padx=10,
    pady=5
)


# botao calcular

botao_calcular = tk.Button(
    janela,
    text="Calcular",
    width=12,
    command=calcular
)

botao_calcular.grid(row=4, column=0, padx=5, pady=15)


# botao reiniciar

botao_reiniciar = tk.Button(
    janela,
    text="Reiniciar",
    width=12,
    command=reiniciar
)

botao_reiniciar.grid(row=4, column=1, padx=5, pady=15)


# botao sair

botao_sair = tk.Button(
    janela,
    text="Sair",
    width=12,
    command=sair
)

botao_sair.grid(row=4, column=2, padx=5, pady=15)


# deixa janela aberta
janela.mainloop()
