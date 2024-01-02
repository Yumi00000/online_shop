from connect_db import Connect_DB


def load_from_db(selected_cl: str, table: str, linked_column=None):
    with Connect_DB() as cursor:
        cursor_string = f'SELECT {selected_cl} FROM "{table}"'
        if linked_column:
            cursor_string += ' WHERE '
            condition = []
            vals = []
            for key, val in linked_column.items():
                condition.append(f'{key} = ?')
                vals.append(val)

            cursor_string += ' AND '.join(condition)
            print(cursor_string, vals)
            cursor.execute(cursor_string, vals)

        else:
            print(cursor_string)

            cursor.execute(cursor_string)
        return cursor.fetchall()


def read_multiply_data_from_db(selected_cl: str, table: list, conditions, linked_column=None):
    with Connect_DB() as cursor:
        cursor_string = f'SELECT {selected_cl} FROM "{table[0]}" INNER JOIN '
        for one_table in table[1:]:

            cursor_string += f'"{one_table}" ON '
            cursor_string += 'AND'.join(conditions[table.index(one_table) - 1])
            if linked_column:
                cursor_string += ' WHERE '
                condition = []
                vals = []
                for key, val in linked_column.items():
                    condition.append(f'{key} = ?')
                    vals.append(val)

                cursor_string += ' AND '.join(condition)
                print(cursor_string, vals)
                cursor.execute(cursor_string, vals)

            else:
                print(cursor_string)

                cursor.execute(cursor_string)

        return cursor.fetchall()


def insert_data_in_db(table: str, values: dict):
    with Connect_DB() as cursor:
        columns = ', '.join(f'"{key}"' for key in values.keys())
        placeholders = ', '.join(['?' for _ in values.values()])
        query = f'INSERT INTO "{table}" ({columns}) VALUES ({placeholders})'

        print("Query:", query)
        print("Values:", list(values.values()))

        cursor.execute(query, list(values.values()))
        return cursor.fetchall()


def update_data_in_db(table: str, columns: dict, linked_columns: dict):
    with Connect_DB() as cursor:
        cursor_string = f'UPDATE "{table}" SET '
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
