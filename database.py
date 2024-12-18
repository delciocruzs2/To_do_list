import sqlite3

class DataBaseError(Exception):
    pass


class _DataBase:

    def __init__(self) -> object:
        try:
            self.__db = sqlite3.connect('TaskDataBase.db') 
            self.__cursor = self.__db.cursor() 
        except sqlite3.Error as e:
            self.__db = None
            raise DataBaseError(f'Error ao conectar o banco de dados: {e}')

    def create_tables(self) -> object:
        try:
            self.__cursor.execute("""CREATE TABLE IF NOT EXISTS task(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                description TEXT
                                )""")
            self.__db.commit()
        except sqlite3.Error as e:
            raise DataBaseError(f'Error creating the table in the database: {e}')
    
    def close_db(self) -> None:
        if self.__db:
            try:
                self.__db.close()
            except sqlite3.Error as e:
                raise DataBaseError(f'"Error closing the connection to the database: {e}')
    
    def add_data(self, title:str, description:str):
        try:
            self.__cursor.execute("""
            INSERT INTO task(title, description)
            VALUES(?,?)""",(title,description))
            self.__db.commit()
        except sqlite3.Error as e:
            raise DataBaseError(f'Error adding data: {e}')

    def __enter__(self) -> object:
        return self
    
    def __exit__(self, exc_type,exc_value, traceback):
        self.close_db()

if __name__ == '__main__':
    try:
        with _DataBase() as db:
            db.create_tables()
    except RuntimeError as e:
        raise DataBaseError(f'Error in database execution: {e}')

