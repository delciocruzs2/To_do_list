import customtkinter as ctk
import sys
from PIL import Image
from database import _DataBase, DataBaseError


class Application(ctk.CTk):
    """
    Frontend of the application contains the graphical settings, such as screen configuration,
    frames, and buttons, which will render the main graphical interface.
    """
    
    def __init__(self) -> object:
        self.__root = ctk.CTk()
        self._db = _DataBase()
        self._FullscreenSettings()
        self.colors()
        self.header()
        self.nav()
        self.main()
        self.__root.mainloop()

    def _FullscreenSettings(self) -> object:
        """ Sensitive graphic settings, such as mode, screen size, icon, etc... """
        self.__root.title('To Do List')
        self.__root.geometry('890x500')
        self.__root.resizable(False,False)
        self.__root._set_appearance_mode('light')
        self.__root.iconbitmap('./image/favicon.ico')

    def colors(self) -> object:
        """ Colors for use in the system. """
        self.lavender = '#E6E6FA'
        self.royalBlue = '#4169E1'
        self.darkSlateGray = '#2F4F4F'
        self.orange = '#FFA500'
        self.lime = '#00FF00'
        self.black = '#000000'

    def header(self) -> object:
        """ Regarding the header, this function contains the frame and the presentation logo. """
        # MAIN FRAME
        self.frame_header = ctk.CTkFrame(self.__root, fg_color= self.orange)
        self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.13)
        # PROCESSING IMAGE
        image_logo = ctk.CTkImage(light_image=Image.open('./image/logo_tarefas.png'),dark_image=Image.open('./image/logo_tarefas.png'), size=(70,50))
        image = ctk.CTkLabel(self.frame_header, image=image_logo, text= None)
        image.place(relx=0, rely=0.05, relwidth=0.2)
        # MAIN TEXT
        sentense = ctk.CTkLabel(self.frame_header, text='Sistema de gerenciador de tarefas', font=('arial', 30))
        sentense.place(relx=0.14, rely=0.1, relwidth=0.52, relheight=0.7)
    
    def nav(self) -> object:
        """ Navigation buttons for accessing the functionality frames. """
        # CREATE NAVIGATION FRAME
        self.frame_nav = ctk.CTkFrame(self.__root, fg_color= self.lavender)
        self.frame_nav.place(relx=0, rely=0.13, relwidth=0.25, relheight=0.87)

        # BUTTON ALL TASK
        self.button_all_task = ctk.CTkButton(self.frame_nav,
                                             fg_color= self.darkSlateGray,
                                             text='Mostrar todas tarefas',
                                             command=self.all_task)
        self.button_all_task.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        # BUTTON NEW TASK
        self.button_new_task = ctk.CTkButton(self.frame_nav,
                                             fg_color= self.darkSlateGray,
                                             text='Nova tarefas',
                                             command=self.new_task)
        self.button_new_task.place(relx=0, rely=0.2, relwidth=1, relheight=0.2)

        # BUTTON UPDATE TASK
        self.button_update_task = ctk.CTkButton(self.frame_nav,
                                                fg_color= self.darkSlateGray,
                                                text='Atualizar tarefas',
                                                command=self.update_task)
        self.button_update_task.place(relx=0, rely=0.4, relwidth=1, relheight=0.2)

        # BUTTON DELETE TASK
        self.button_delete_task = ctk.CTkButton(self.frame_nav,
                                                fg_color= self.darkSlateGray,
                                                text='Excluir tarefas',
                                                command=self.delete_task)
        self.button_delete_task.place(relx=0, rely=0.6, relwidth=1, relheight=0.2)

        # BUTTON ABOUT
        self.button_about = ctk.CTkButton(self.frame_nav,
                                          fg_color= self.darkSlateGray,
                                          text='About',
                                          command=self.about)
        self.button_about.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

    def all_task(self) -> object:
        """ List all the tasks """
        self.frame_all_task = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_all_task.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_all_task, text='Todas as tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

    def new_task(self) -> object:
        """ Add a new task """
        # create frame
        self.frame_new_task = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_new_task.place(relx=0, rely=0, relwidth=1, relheight=1)

        # text apresentation
        text_base = ctk.CTkLabel(self.frame_new_task, text='Adicionar nova tarefa', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        # text title
        text_title = ctk.CTkLabel(self.frame_new_task,
                                  text='Nome da tarefa:',
                                  text_color=self.darkSlateGray)
        text_title.place(relx=0.07, rely=0.1, relwidth=0.14, relheight=0.1)

        # Entry title
        _title = ctk.CTkEntry(self.frame_new_task,)
        _title.place(relx=0.07, rely=0.17, relwidth= 0.5, relheight=0.08)

        # text description
        text_description = ctk.CTkLabel(self.frame_new_task,
                                  text='Descrição da tarefa:',
                                  text_color=self.darkSlateGray)
        text_description.place(relx=0.07, rely=0.25, relwidth=0.18, relheight=0.08)

        # TextBox description
        _description = ctk.CTkTextbox(self.frame_new_task)
        _description.place(relx=0.07, rely=0.32, relwidth=0.8, relheight=0.2)

        # Button add
        button_add_task = ctk.CTkButton(self.frame_new_task,
                                        fg_color= self.lime,
                                        text_color= self.black,
                                        border_width=1,
                                        text= 'Adicionar',
                                        command= lambda: self.integration_add(_title.get(),_description.get("1.0", "end-1c")))
        button_add_task.place(relx=0.35, rely=0.57, relwidth=0.3, relheight=0.07)

    
    def update_task(self) -> object:
        """ Update a task """
        # create frame
        self.frame_update_task = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_update_task.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_update_task, text='Atualizar tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)
    
    def delete_task(self) -> object:
        """ Delete tasks """
        # create frame
        self.frame_delete_task = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_delete_task.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_delete_task, text='Deletar tarefas', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)
    
    def about(self) -> object:
        """ Presentation about the project, creator, contact, general provisions """
        # create frame
        self.frame_about = ctk.CTkFrame(self.frame_main, fg_color=self.lavender, border_width=3)
        self.frame_about.place(relx=0, rely=0, relwidth=1, relheight=1)
        # text apresentation
        text_base = ctk.CTkLabel(self.frame_about, text='About', fg_color=self.darkSlateGray)
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

    def main(self) -> object:
        # create frame
        self.frame_main = ctk.CTkFrame(self.__root, border_width=3, fg_color= self.lavender)
        self.frame_main.place(relx=0.25, rely=0.13, relwidth=0.75, relheight=0.87)

    def integration_add(self, title:str, description:str):
        """ Integration with the add_data function"""
        if not title or not description:
                message_error = ctk.CTkLabel(self.frame_new_task,
                                             text_color= self.darkSlateGray,
                                            text="""Error ao adicionar tarefa\nOs campos não podem está vazios""") 
                message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
                return
        
        try:
            with _DataBase() as db:
                db.add_data(title, description)
            message_check = ctk.CTkLabel(self.frame_new_task,
                                        text_color=self.darkSlateGray,
                                        text='Adicionado com sucesso') 
            message_check.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
        except DataBaseError:
            message_error = ctk.CTkLabel(self.frame_new_task,
                                         text_color= self.darkSlateGray,
                                         text='Error ao adicionar') 
            message_error.place(relx=0.35, rely=0.64, relwidth=0.3, relheight=0.07)
            
    


if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)