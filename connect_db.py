import sqlite3


class Connect_DB:
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def __enter__(self):
        self.my_db = sqlite3.connect('instance/identifier.sqlite')
        self.row_factory = self.dict_factory
        self.cursor = self.my_db.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.my_db:
            if exc_type is None:
                self.my_db.commit()
            self.my_db.close()
