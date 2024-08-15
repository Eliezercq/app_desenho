import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

# Função para criar o desenho
def criar_desenho(texto):
    # Criando uma imagem em branco
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)

    # Definindo a fonte e o tamanho
    fonte = ImageFont.truetype("arial.ttf", 20)

    # Desenhando o texto na imagem
    draw.text((10, 10), texto, fill='black', font=fonte)

    # Exibindo a imagem
    img.show()

# Função para lidar com o evento de clique no botão
def clicar_botao():
    texto = entrada.get()
    criar_desenho(texto)

# Criando a janela
janela = tk.Tk()
janela.title("Transformador de Texto em Desenho")

# Criando a entrada de texto
entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

# Criando o botão
botao = tk.Button(janela, text="Transformar em Desenho", command=clicar_botao)
botao.pack(pady=5)

# Rodando a aplicação
janela.mainloop()