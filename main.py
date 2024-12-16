import customtkinter as ctk
import sys

class Application(ctk.CTk):
    
    def __init__(self) -> object:
        self.__root = ctk.CTk()
        self._FullscreenSettings()
        self.header()
        self.nav()
        self.main()
        self.__root.mainloop()


    def _FullscreenSettings(self) -> object:
        self.__root.title('To Do List')
        self.__root.geometry('890x500')
        self.__root.resizable(False,False)


    def header(self) -> object:
        self.frame_header = ctk.CTkFrame(self.__root, border_width=1)
        self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    
    def nav(self) -> object:
        self.frame_nav = ctk.CTkFrame(self.__root, border_width=1)
        self.frame_nav.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.8)

    def main(self) -> object:
        self.frame_main = ctk.CTkFrame(self.__root, border_width=1)
        self.frame_main.place(relx=0.2, rely=0.2, relwidth=0.8, relheight=0.8)













if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)