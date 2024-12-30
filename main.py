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
        self.grey = '#808080'

    def header(self) -> object:
        """ Regarding the header, this function contains the frame and the presentation logo. """
        # MAIN FRAME
        self.frame_header = ctk.CTkFrame(self.__root,
                                        fg_color= self.darkSlateGray)
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
        self.frame_all_task = ctk.CTkScrollableFrame(self.frame_main,
                                           fg_color=self.lavender,
                                           border_width=3)
        self.frame_all_task.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Dattabase connection
        try:
            with _DataBase() as db:
                result = db.show_all_results()
        except DataBaseError:
            message_error = ctk.CTkLabel(self.frame_all_task,
                                         text_color= self.darkSlateGray,
                                         text="Error, algo inesperado aconteceu") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            return

        # structure dict -> id, title, descript
        dict_results_ = {str(item[0]):[item[1],item[2]] for item in result} 

        list_datas = [['ID','Tarefa','Descrição']]

        for _key, _value in dict_results_.items():
            data_all_task = [_key,_value[0],_value[1]]
            list_datas.append(data_all_task)
        
        # table
        for line_index, line in enumerate(list_datas):
            for column_index, value in enumerate(line):
                # Define style for header and regular cells
                bg_color_ = "#F0F8FF" if line_index == 0 else 'white'
                # Cria cada célula da tabela
                celula = ctk.CTkLabel(self.frame_all_task,
                                      text=value,
                                      corner_radius=4,
                                      fg_color=bg_color_,
                                      text_color=self.darkSlateGray,
                                      padx=10,
                                      pady=5)
                # Positions the cell in the grid
                celula.grid(row=line_index,
                            column=column_index,
                            sticky="nsew",
                            padx=1,
                            pady=1)

        # Ensures that the columns adjust automatically
        for coluna in range(len(list_datas[0])):
                self.frame_all_task.columnconfigure(coluna, weight=1)

    def new_task(self) -> object:
        """ Add a new task """
        # create frame
        self.frame_new_task = ctk.CTkFrame(self.frame_main,
                                          fg_color=self.lavender,
                                          border_width=3)
        self.frame_new_task.place(relx=0, rely=0, relwidth=1, relheight=1)

        # text apresentation
        text_base = ctk.CTkLabel(self.frame_new_task,
                                fg_color=self.darkSlateGray,
                                text='Adicionar nova tarefa')
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        # text title
        text_title = ctk.CTkLabel(self.frame_new_task,
                                  text_color=self.darkSlateGray,
                                  text='Nome da tarefa:',
                                  )
        text_title.place(relx=0.07, rely=0.1, relwidth=0.14, relheight=0.1)

        # Entry title
        _title = ctk.CTkEntry(self.frame_new_task)
        _title.place(relx=0.07, rely=0.17, relwidth= 0.5, relheight=0.08)

        # text description
        text_description = ctk.CTkLabel(self.frame_new_task,
                                        text_color=self.darkSlateGray,
                                        text='Descrição da tarefa:')
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
        self.frame_update_task = ctk.CTkFrame(self.frame_main,
                                              fg_color=self.lavender,
                                              border_width=3)
        self.frame_update_task.place(relx=0, rely=0, relwidth=1, relheight=1)

        # text apresentation
        text_base = ctk.CTkLabel(self.frame_update_task,
                                 fg_color=self.darkSlateGray,
                                 text='Atualizar tarefas', )
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        # text choose
        text_choose = ctk.CTkLabel(self.frame_update_task,
                                   text_color=self.darkSlateGray,
                                   text='Selecione a tarefa que será atualizada:')
        text_choose.place(relx=0.07, rely=0.1, relwidth=0.33, relheight=0.1)

        # Database connection 
        with _DataBase() as db:
            result = db.show_all_results()
        self.list_titles_update = [item[1] for item in result] # List titles -> List str

         # combobox
        combobox_choose = ctk.CTkComboBox(self.frame_update_task,
                                          values= self.list_titles_update)
        combobox_choose.place(relx=0.07, rely=0.17, relwidth= 0.8, relheight=0.08)

        # button select result 
        button_select = ctk.CTkButton(self.frame_update_task,
                                      border_width=1,
                                      fg_color=self.grey,
                                      text_color=self.black,
                                      text='selecionar',
                                      command= lambda: self.update_source(combobox_choose.get()))
        button_select.place(relx=0.07, rely=0.28, relwidth=0.26, relheight=0.06)
  
    def delete_task(self) -> object:
        """ Delete tasks """
        # create frame
        self.frame_delete_task = ctk.CTkFrame(self.frame_main,
                                              fg_color=self.lavender,
                                              border_width=3)
        self.frame_delete_task.place(relx=0, rely=0, relwidth=1, relheight=1)

        # text apresentation
        text_base = ctk.CTkLabel(self.frame_delete_task,
                                 fg_color=self.darkSlateGray,
                                 text='Deletar tarefas')
        text_base.place(relx=0, rely=0, relwidth=1, relheight=0.09)

        # text choose
        text_choose = ctk.CTkLabel(self.frame_delete_task,
                                   text_color=self.darkSlateGray,
                                   text='Selecione a tarefa que será excluida:')
        text_choose.place(relx=0.07, rely=0.1, relwidth=0.32, relheight=0.1)

        # Database connection 
        with _DataBase() as db:
            result = db.show_all_results()
        self.list_titles = [item[1] for item in result] # List titles -> List str

         # combobox
        combobox_choose = ctk.CTkComboBox(self.frame_delete_task,
                                          values= self.list_titles)
        combobox_choose.place(relx=0.07, rely=0.17, relwidth= 0.8, relheight=0.08)

        # button select result 
        button_select = ctk.CTkButton(self.frame_delete_task,
                                      border_width=1,
                                      fg_color=self.grey,
                                      text_color=self.black,
                                      text='selecionar',
                                      command= lambda: self.delete_source(combobox_choose.get()))
        button_select.place(relx=0.07, rely=0.28, relwidth=0.26, relheight=0.06)

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
                self.frame_new_task.after(3000, lambda: message_error.destroy())
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
        finally:
            self.frame_new_task.after(2500, self.new_task)
            
    def update_source(self, value) -> None:
        """ the function must handle the parameter selected by the user, and return 
        to the update_commit function the real id to be update """
        # error verefication
        if not value or value not in self.list_titles_update:
            message_error = ctk.CTkLabel(self.frame_update_task,
                                         text_color= self.darkSlateGray,
                                         text="Error ao encontrar tarefa\nparametros não existem") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            self.frame_update_task.after(2500,lambda: message_error.destroy())
            return
        
        # Database connection
        try:
            with _DataBase() as db:
                result = db.show_all_results()
        except DataBaseError:
            message_error = ctk.CTkLabel(self.frame_update_task,
                                         text_color= self.darkSlateGray,
                                         text="Error, algo inesperado aconteceu") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            return

        # structure dict -> id, title, descript
        dict_results_ = {str(item[0]):[item[1],item[2]] for item in result} 

        # The list contains equal values in case of true
        temporary_list = [_value[0] for _key,_value in dict_results_.items() if _value[0] == value] 

        # conditional on quantity of tasks -> referent temporary list
        if len(temporary_list) > 1 :
            _message_ = ctk.CTkLabel(self.frame_update_task,
                                         text_color= self.darkSlateGray,
                                         text=f'Existem {len(temporary_list)} tarefas com esse nome\ndefina a tarefa que deseja editar') 
            _message_.place(relx=0.25, rely=0.34, relwidth=0.5, relheight=0.1)

            # combobox to list
            list_values = []
            for _key_,_value_ in dict_results_.items():
                if _value_[0] == value:
                    _result_ = f'{_key_}   :   {_value_[0]}   -   {_value_[1]}'
                    list_values.append(_result_)

            # ComboBox with ID, keys, and values
            id_combobox= ctk.CTkComboBox(self.frame_update_task,
                                              values= list_values)
            id_combobox.place(relx=0.07, rely=0.43, relwidth= 0.8, relheight=0.08)
            id_finally = id_combobox.get()
            id_finally = id_finally[:4] # parameter -> _id

            # text new title
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Novo titulo: ')
            text_update_confirme.place(relx=0.07, rely=0.51, relwidth=0.1, relheight=0.08)

            # Entry new titile
            new_title_entry = ctk.CTkEntry(self.frame_update_task)
            new_title_entry.place(relx=0.22,rely=0.52, relwidth=0.6, relheight=0.05)

            #text new description
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Nova descrição: ')
            text_update_confirme.place(relx=0.07, rely=0.56, relwidth=0.14, relheight=0.08)

            # Entry new description
            new_description_entry= ctk.CTkEntry(self.frame_update_task)
            new_description_entry.place(relx=0.22,rely=0.58, relwidth=0.6, relheight=0.05)

            # text confirme
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                    text_color=self.darkSlateGray,
                                                    text=f'Confirme para editar tarefa')
            text_update_confirme.place(relx=0.07, rely=0.63, relwidth=0.23, relheight=0.08)

            # button confirme
            button_update_confirme = ctk.CTkButton(self.frame_update_task,
                                    border_width=1,
                                    fg_color=self.lime,
                                    text_color=self.black,
                                    text='confirmar',
                                    command= lambda: self.update_commit(id_finally,new_title_entry.get(),new_description_entry.get()))
            button_update_confirme.place(relx=0.35, rely=0.64, relwidth=0.26, relheight=0.06)
        else:
            # defining id
            for _key,_value in dict_results_.items():
                if _value[0] == value:
                    result_id = _key
                    break

            # Check result of selection
            for _key,_value in dict_results_.items():
                if _value[0] == value:
                    result_finale = [_key,_value[0],_value[1]] # title, description
                    break
            task_select = ctk.CTkLabel(self.frame_update_task,
                                  text_color= self.darkSlateGray,
                                  text=f"""-----  {result_finale[1]}  -----\n\n{result_finale[2]}""") 
            task_select.place(relx=0.07, rely=0.35, relwidth=0.8, relheight=0.16)

            # text new title
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Novo titulo: ')
            text_update_confirme.place(relx=0.07, rely=0.51, relwidth=0.1, relheight=0.08)

            # Entry new titile
            new_title_entry = ctk.CTkEntry(self.frame_update_task)
            new_title_entry.place(relx=0.22,rely=0.52, relwidth=0.6, relheight=0.05)

            #text new description
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Nova descrição: ')
            text_update_confirme.place(relx=0.07, rely=0.56, relwidth=0.14, relheight=0.08)

            # Entry new description
            new_description_entry= ctk.CTkEntry(self.frame_update_task)
            new_description_entry.place(relx=0.22,rely=0.58, relwidth=0.6, relheight=0.05)

            # text confirme
            text_update_confirme = ctk.CTkLabel(self.frame_update_task,
                                                    text_color=self.darkSlateGray,
                                                    text=f'Confirme para editar tarefa')
            text_update_confirme.place(relx=0.07, rely=0.63, relwidth=0.23, relheight=0.08)

            # button confirme
            button_update_confirme = ctk.CTkButton(self.frame_update_task,
                                    border_width=1,
                                    fg_color=self.lime,
                                    text_color=self.black,
                                    text='confirmar',
                                    command= lambda: self.update_commit(result_id,new_title_entry.get(),new_description_entry.get()))
            button_update_confirme.place(relx=0.35, rely=0.64, relwidth=0.26, relheight=0.06)         

    def update_commit(self,_id:str ,new_title:str, new_description:str) -> None:
        """ Confirm the updating in the database """
        _id = int(_id)
        # conditional vereficy
        if not new_title or not new_description:
            message_error = ctk.CTkLabel(self.frame_update_task,
                                        text_color= self.darkSlateGray,
                                        text="Error ao atualizar tarefa\nParametros vazios") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            self.frame_update_task.after(2500, lambda: message_error.destroy())
            return
        else:
            try:
                with _DataBase() as db:
                    db.update_data(_id,new_title,new_description)
                message_ = ctk.CTkLabel(self.frame_update_task,
                                            text_color= self.darkSlateGray,
                                            text="Atualizado com sucesso") 
                message_.place(relx=0.25, rely=0.74, relwidth=0.5, relheight=0.2)
            except DataBaseError:
                message_error = ctk.CTkLabel(self.frame_update_task,
                                            text_color= self.darkSlateGray,
                                            text="Error ao atualizar tarefa") 
                message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            finally:
                self.frame_update_task.after(2500, self.update_task)

    def delete_source(self, value) -> None:
        """ the function must handle the parameter selected by the user, and return 
        to the delete_commit function the real id to be deleted """
        # error verefication
        if not value or value not in self.list_titles:
            message_error = ctk.CTkLabel(self.frame_delete_task,
                                         text_color= self.darkSlateGray,
                                         text="Error ao deletar tarefa\nparametros não existem") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            self.frame_delete_task.after(2500,lambda: message_error.destroy())
            return
        
        # Database connection
        try:
            with _DataBase() as db:
                result = db.show_all_results()
        except DataBaseError:
            message_error = ctk.CTkLabel(self.frame_delete_task,
                                         text_color= self.darkSlateGray,
                                         text="Error, algo inesperado aconteceu") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
            return

        # structure dict -> id, title, descript
        dict_results_ = {str(item[0]):[item[1],item[2]] for item in result} 

        # The list contains equal values in case of true
        temporary_list = [_value[0] for _key,_value in dict_results_.items() if _value[0] == value] 

        # conditional on quantity of tasks -> referent temporary list
        if len(temporary_list) > 1 :
            message_ = ctk.CTkLabel(self.frame_delete_task,
                                         text_color= self.darkSlateGray,
                                         text=f'Existem {len(temporary_list)} tarefas com esse nome\ndefina a tarefa que deseja excluir') 
            message_.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.2)

            # combobox to list
            list_values = []
            for _key_,_value_ in dict_results_.items():
                if _value_[0] == value:
                    _result_ = f'{_key_}   :   {_value_[0]}   -   {_value_[1]}'
                    list_values.append(_result_)

            # ComboBox with ID, keys, and values
            id_combobox= ctk.CTkComboBox(self.frame_delete_task,
                                              values= list_values)
            id_combobox.place(relx=0.07, rely=0.51, relwidth= 0.8, relheight=0.08)
            id_finally = id_combobox.get()
            id_finally = id_finally[:4]

            # text confirme
            text_delete_confirme = ctk.CTkLabel(self.frame_delete_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Confirme para deletar tarefa')
            text_delete_confirme.place(relx=0.07, rely=0.6, relwidth=0.8, relheight=0.08)

            # button confirme
            button_delete_confirme = ctk.CTkButton(self.frame_delete_task,
                                      border_width=1,
                                      fg_color=self.grey,
                                      text_color=self.black,
                                      text='confirmar',
                                      command= lambda: self.delete_commit(id_finally))
            button_delete_confirme.place(relx=0.35, rely=0.68, relwidth=0.26, relheight=0.06)


        else:
            for _key,_value in dict_results_.items():
                if _value[0] == value:
                    result_finale = [_key,_value[0],_value[1]] # title, description
                    break
            task_select = ctk.CTkLabel(self.frame_delete_task,
                                  text_color= self.darkSlateGray,
                                  text=f"""-----  {result_finale[1]}  -----\n\n{result_finale[2]}""") 
            task_select.place(relx=0.07, rely=0.4, relwidth=0.8, relheight=0.2)

            # text confirme
            text_delete_confirme = ctk.CTkLabel(self.frame_delete_task,
                                                text_color=self.darkSlateGray,
                                                text=f'Confirme para deletar tarefa')
            text_delete_confirme.place(relx=0.07, rely=0.6, relwidth=0.8, relheight=0.08)

            # button confirme
            button_delete_confirme = ctk.CTkButton(self.frame_delete_task,
                                      border_width=1,
                                      fg_color=self.grey,
                                      text_color=self.black,
                                      text='confirmar',
                                      command= lambda: self.delete_commit(result_finale[0]))
            button_delete_confirme.place(relx=0.35, rely=0.68, relwidth=0.26, relheight=0.06)
        
    def delete_commit(self, value:str) -> None:
        """ Confirm the deletion in the database """
        value = int(value)
        try:
            with _DataBase() as db:
                db.delete_data(value)
            message_ = ctk.CTkLabel(self.frame_delete_task,
                                    text_color= self.darkSlateGray,
                                    text="Deletada com sucesso") 
            message_.place(relx=0.25, rely=0.74, relwidth=0.5, relheight=0.2)
        except DataBaseError:
            message_error = ctk.CTkLabel(self.frame_delete_task,
                                         text_color= self.darkSlateGray,
                                         text="Error ao deletar tarefa") 
            message_error.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.2)
        finally:
            self.frame_delete_task.after(2500, self.delete_task)
            

if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)