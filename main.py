import customtkinter as ctk
import sys
from PIL import Image


class Application(ctk.CTk):
    
    def __init__(self) -> object:
        self.__root = ctk.CTk()
        self._FullscreenSettings()
        self.colors()
        self.header()
        self.nav()
        self.main()
        self.__root.mainloop()


    def _FullscreenSettings(self) -> object:
        self.__root.title('To Do List')
        self.__root.geometry('890x500')
        self.__root.resizable(False,False)
        self.__root._set_appearance_mode('light')
        self.__root.iconbitmap('./image/favicon.ico')

    def colors(self) -> object:
        self.lavender = '#E6E6FA'
        self.royalBlue = '#4169E1'
        self.darkSlateGray = '#2F4F4F'

    def header(self) -> object:
        # MAIN FRAME
        self.frame_header = ctk.CTkFrame(self.__root, fg_color= self.royalBlue)
        self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.13)
        # PROCESSING IMAGE
        image_logo = ctk.CTkImage(light_image=Image.open('./image/logo_tarefas.png'),dark_image=Image.open('./image/logo_tarefas.png'), size=(70,50))
        image = ctk.CTkLabel(self.frame_header, image=image_logo, text= None)
        image.place(relx=0, rely=0.05, relwidth=0.2)
        # MAIN TEXT
        sentense = ctk.CTkLabel(self.frame_header, text='Sistema de gerenciador de tarefas', font=('arial', 30))
        sentense.place(relx=0.14, rely=0.1, relwidth=0.52, relheight=0.7)
    
    def nav(self) -> object:
        self.frame_nav = ctk.CTkFrame(self.__root, fg_color= self.lavender)
        self.frame_nav.place(relx=0, rely=0.13, relwidth=0.25, relheight=0.87)

        self.button_all_ask = ctk.CTkButton(self.frame_nav, text='Mostrar todas tarefas', command=self.all_ask)
        self.button_all_ask.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        self.button_new_ask = ctk.CTkButton(self.frame_nav, text='Nova tarefas', command=self.new_ask)
        self.button_new_ask.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

        self.button_update_ask = ctk.CTkButton(self.frame_nav, text='Atualizar tarefas', command=self.update_ask)
        self.button_update_ask.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        self.button_delete_ask = ctk.CTkButton(self.frame_nav, text='Excluir tarefas', command=self.delete_ask)
        self.button_delete_ask.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)

        self.button_about = ctk.CTkButton(self.frame_nav, text='About', command=self.about)
        self.button_about.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

    def all_ask(self) -> object:
        self.frame_all_ask = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_all_ask.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_all_ask, text='Todas as tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

    def new_ask(self) -> object:
        self.frame_new_ask = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_new_ask.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_new_ask, text='Adicionar nova tarefa', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)
    
    def update_ask(self) -> object:
        self.frame_update_ask = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_update_ask.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_update_ask, text='Atualizar tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)
    
    def delete_ask(self) -> object:
        self.frame_delete_ask = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_delete_ask.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_delete_ask, text='Deletar tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)
    
    def about(self) -> object:
        self.frame_about = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_about.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_about, text='About', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

    def main(self) -> object:
        self.frame_main = ctk.CTkFrame(self.__root, border_width=3, fg_color= self.lavender)
        self.frame_main.place(relx=0.25, rely=0.13, relwidth=0.75, relheight=0.87)

    


if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)