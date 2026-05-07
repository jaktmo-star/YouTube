import customtkinter as ctk
from pytubefix import YouTube

#configurações visual
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

#função baixar video
def baixar():
    link_youtube = link.get()
    yt = YouTube (link_youtube)
    #baixa resolução padrão
    yt.streams.first().download()
    status.configure(text='Download concluído')

#criação de janela
janela = ctk.CTk()
janela.geometry('600x400')
janela.title('Downloads de videos do youtube')

#Elementos da tela
#Label título
titulo = ctk.CTkLabel(
    janela, 
    text="Downloads de videos do youtube",
    font=('Arial',20,'bold'),
    text_color='red'
)
titulo.pack(pady=20)

#icone da janela
janela.iconbitmap('youtube.ico')

link = ctk.CTkEntry(
    janela, 
    placeholder_text="Insira o link desejado",
    width=300,
    height=35,
    corner_radius=8,
)
link.pack(pady=20)
#botão
download = ctk.CTkButton(
    janela, 
    text="Download", 
    command=baixar,
    fg_color='#1f7fa5',
    hover_color='#147020',
    corner_radius=10
)
download.pack(pady=20)
#status download concluido
status=ctk.CTkLabel(
    janela, 
    text="",
    text_color="green"
)
status.pack(pady=20)

#loop para geração da janela
janela.mainloop()
