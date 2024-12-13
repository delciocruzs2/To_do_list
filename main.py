import customtkinter
import sys

class Application(customtkinter.CTk):
    
    def __init__(self) -> object:
        super().__init__()
        self.__root = customtkinter.CTk()
        self._FullscreenSettings()
        self.__root.mainloop()


    def _FullscreenSettings(self) -> object:
        self.__root.title('To Do List')
        self.__root.geometry('890x500')
        self.__root.resizable(False,False)
















if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)