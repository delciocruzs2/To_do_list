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

    def header(self) -> object:
        self.frame_header = ctk.CTkFrame(self.__root, border_width=1, fg_color= self.lavender)
        self.frame_header.place(relx=0, rely=0, relwidth=1, relheight=0.13)
    
    def nav(self) -> object:
        self.frame_nav = ctk.CTkFrame(self.__root, border_width=1, fg_color= self.lavender)
        self.frame_nav.place(relx=0, rely=0.13, relwidth=0.25, relheight=0.87)

    def main(self) -> object:
        self.frame_main = ctk.CTkFrame(self.__root, border_width=1, fg_color= self.lavender)
        self.frame_main.place(relx=0.25, rely=0.13, relwidth=0.75, relheight=0.87)













if __name__ == '__main__':
    try:
        Application()
    except RuntimeError:
        sys.exit(1)