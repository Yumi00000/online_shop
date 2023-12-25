from connect_db import Connect_DB


def load_from_db(selected_cl: str, tabel: str, linked_column=None):
    with Connect_DB() as cursor:
        cursor_string = f'SELECT {selected_cl} FROM "{tabel}"'
        if linked_column:
            cursor_string += ' WHERE '
            condition = []
            vals = []
            for key, val in linked_column:
                condition.append(f'{key} = ?')
                vals.append(val)
            cursor_string += ' AND '.join(condition)
            cursor.execute(cursor_string, vals)
        else:
            cursor.execute(cursor_string)
        return cursor.fetchall()


def insert_data_in_db(table: str, values: list):
    with Connect_DB() as cursor:
        placeholders = ', '.join(['?' for _ in values])
        cursor.execute(f'INSERT INTO "{table}" VALUES ({placeholders})', values)
        return cursor.fetchall()


def update_data_in_db(table: str, columns: dict, linked_columns: dict):
    with Connect_DB() as cursor:
        cursor_string = f'UPDATE "{table}" SET'
        set_clause = ', '.join([f'{column}=?' for column in columns.keys()])
        cursor_string += set_clause
        values = list(columns.values())

        if linked_columns:
            cursor_string += ' WHERE '
            condition = ' AND '.join([f'{key}=?' for key in linked_columns.keys()])
            cursor_string += condition
            values += list(linked_columns.values())
        cursor.execute(cursor_string, values)
        return cursor.fetchall()



def delete_data_from_db(table: str, condition: str, val):
    with Connect_DB() as cursor:
        cursor.execute(f'DELETE FROM {table} WHERE {condition} = ?', (val,))
        return cursor.fetchall()
