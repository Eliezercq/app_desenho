import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

def criar_desenho(texto):
    img = Image.new('RGB', (300, 300), color='white')
    draw = ImageDraw.Draw(img)

    fonte = ImageFont.truetype("arial.ttf", 20)

    draw.text((10, 10), texto, fill='black', font=fonte)

    img.show()

def clicar_botao():
    texto = entrada.get()
    criar_desenho(texto)

janela = tk.Tk()
janela.title("Transformador de Texto em Desenho")

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Transformar em Desenho", command=clicar_botao)
botao.pack(pady=5)

janela.mainloop()
