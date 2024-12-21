import sqlite3

class DataBaseError(Exception):
    pass


class _DataBase:

    # System function -> development
    def __init__(self) -> object:
        try:
            self.__db = sqlite3.connect('TaskDataBase.db') 
            self.__cursor = self.__db.cursor() 
        except sqlite3.Error as e:
            self.__db = None
            raise DataBaseError(f'Error ao conectar o banco de dados: {e}')

    # System function -> development
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
    
    # System function -> development
    def close_db(self) -> None:
        if self.__db:
            try:
                self.__db.close()
            except sqlite3.Error as e:
                raise DataBaseError(f'"Error closing the connection to the database: {e}')

    # System function -> development
    def __enter__(self) -> object:
        return self
        
    # System function -> development
    def __exit__(self, exc_type,exc_value, traceback):
        self.close_db()
    
    def add_data(self, title:str, description:str):
        try:
            title = title.capitalize()
            description = description.capitalize()
            self.__cursor.execute("""
            INSERT INTO task(title, description)
            VALUES(?,?)""",(title,description))
            self.__db.commit()
        except sqlite3.Error as e:
            self.__db.rollback()
            raise DataBaseError(f'Error adding data: {e}')
     
    def show_all_results(self) -> list:
        try:
            self.__cursor.execute("""
            SELECT * 
            FROM task;
            """)
            result = self.__cursor.fetchall()
            return result
        except sqlite3.Error as e:
            raise DataBaseError(f'Error displaying all results: {e}')
    
    def update_data(self, id:int, new_title:str, new_description:str) -> None:
        try:
            self.__cursor.execute("""
            UPDATE task
            SET title = ?,
                description = ?
            WHERE id = ?;
            """, (new_title, new_description,id))
            return self.__db.commit()
        except sqlite3.Error as e:
            self.__db.rollback()
            raise DataBaseError(f'Error updating data: {e}')
    
    def delete_data(self, id:int):
        try:
            self.__cursor.execute("""
            DELETE FROM task
            WHERE id = ?;
                                  
            """,(id,))
            self.__db.commit()
        except sqlite3.Error as e:
            self.__db.rollback()
            raise DataBaseError(f'Error deleting data: {e}')

    



if __name__ == '__main__':

    """
    This section should only be used to modify the database structure (in functions identified as such # System function -> development)
    or for testing, by changing the parameters below
    """

    try:
        with _DataBase() as db:
            db.add_data('title','description')
            db.delete_data('id')
            db.update_data('id','new_titile','new_description')
            print(db.show_all_results())
    except RuntimeError as e:
        raise DataBaseError(f'Error in database execution: {e}')

