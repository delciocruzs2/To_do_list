import sqlite3


class _DataBase:

    def __init__(self) -> object:
        try:
            self.__db = sqlite3.connect('TaskDataBase.db') 
            self.__cursor = self.__db.cursor() 
        except sqlite3.Error as e:
            self.__db = None
            raise(f'Error ao conectar o banco de dados: {e}')

    def create_tables(self) -> object:
        try:
            self.__cursor.execute("""CREATE TABLE IF NOT EXISTS task(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                description TEXT
                                )""")
            self.__db.commit()
        except sqlite3.Error as e:
            raise(f'Error creating the table in the database: {e}')
    
    def close_db(self) -> None:
        if self.__db:
            try:
                self.__db.close()
            except sqlite3.Error as e:
                raise(f'"Error closing the connection to the database: {e}')


if __name__ == '__main__':
    try:
        db = _DataBase()
        db.create_tables()
    except sqlite3.Error:
        pass
    finally:
        db.close_db()
    

