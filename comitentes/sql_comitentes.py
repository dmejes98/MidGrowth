import pymysql
import pandas as pd
import numpy as np


class DataBase:

    headers = (
        "Identificador",
        "Nombre Comitente",
        "Tipo ID Comitente",
        "No. ID Comitente",
        "Fecha Ingreso",
        "Fecha Actualización",
        "Nombre Ordenante",
        "Tipo ID Ordenante",
        "No. ID Ordenante",
        "e-mail Ordenante",
        "Teléfono Ordenante",
    )

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost", user="root", password="Sttah1312/", db="midgrowth_db"
        )

        self.cursor = self.connection.cursor()
        print("Conexión establecida exitosamente")

    def select_user(self, id):
        sql = f"SELECT * FROM comitentes WHERE idcomitentes = {id}"

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            user = pd.DataFrame(user).T
            rename_col = {i: DataBase.headers[i] for i in range(0, 11, 1)}
            user = user.rename(columns=rename_col)
            user = user.set_index("Identificador")

            return user

        except Exception as e:
            print(e)

    def select_all_users(self):
        sql = "SELECT * FROM comitentes"

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            users = pd.DataFrame(users)
            rename_col = {i: DataBase.headers[i] for i in range(0, 11, 1)}
            users = users.rename(columns=rename_col)
            users = users.set_index("Identificador")

            return users

        except Exception as e:
            print(e)

    def insert_user(self):

        nombre_c = str(input("Nombre del comitente: "))
        tipo_id_c = str(input("Tipo ID del comitente: "))
        num_id_c = str(input("Número ID del comitente: "))
        fecha_ingreso = str(input("Fecha de ingreso (AAAA/MM/DD): "))
        fecha_actualiz = fecha_ingreso
        nombre_ord = str(input("Nombre del ordenante: "))
        tipo_id_ord = str(input("Tipo ID del ordenante: "))
        num_id_ord = str(input("Número ID del ordenante: "))
        email_ord = str(input("e-mail del ordenante: "))
        num_tel_ord = str(input("Teléfono del ordenante: "))

        sql = """INSERT INTO comitentes
        (nombre_c, tipo_id_c, num_id_c, fecha_ingreso, fecha_actualiz, nombre_ord, tipo_id_ord, num_id_ord, email_ord, num_tel_ord)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (
            nombre_c,
            tipo_id_c,
            num_id_c,
            fecha_ingreso,
            fecha_actualiz,
            nombre_ord,
            tipo_id_ord,
            num_id_ord,
            email_ord,
            num_tel_ord,
        )

        try:
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("Comitente registrado exitosamente")

        except Exception as e:
            print(e)
            print("Error en el registro del comitente")

    def update_user(self, id_update):

        print(
            """
        Seleccione el campo que desea actualizar:

        1. Tipo ID Comitente
        2. No. ID Comitente
        3. Nombre Ordenante
        4. Tipo ID Ordenante
        5. No. ID Ordenante
        6. e-mail Ordenante
        7. Teléfono Ordenante
        8. Todos
        
        """
        )

        field_to_update = int(input("Ingrese su selección del campo a actualizar: "))

        field_describe = [
            "fecha_actualiz",
            "tipo_id_c",
            "num_id_c",
            "nombre_ord",
            "tipo_id_ord",
            "num_id_ord",
            "email_ord",
            "num_tel_ord",
            None,
        ]

        try:
            indice = field_describe.index(field_describe[field_to_update])
            if field_to_update == 8:

                for i in range(1, 8, 1):
                    new_data = str(
                        input(f"Ingrese nuevo dato para {field_describe[i]}: ")
                    )
                    sql = f"UPDATE comitentes SET {field_describe[i]} = '{new_data}' WHERE idcomitentes = {id_update}"

                    try:
                        self.cursor.execute(sql)
                        self.connection.commit()
                    except Exception as e:
                        print(e)
                        print("Error en actualización")

            else:
                new_data = str(
                    input(
                        f"Ingrese nuevo dato para {field_describe[field_to_update]}: "
                    )
                )
                sql = f"UPDATE comitentes SET {field_describe[field_to_update]} = '{new_data}' WHERE idcomitentes = {id_update}"

                try:
                    self.cursor.execute(sql)
                    self.connection.commit()

                except Exception as e:
                    print(e)
                    print("Error en actualización")

            update_date = str(input("Fecha de actualización: "))
            sql = f"UPDATE comitentes SET {field_describe[0]} = '{update_date}' WHERE idcomitentes = {id_update}"

            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
            print("Ha ingresado un código de campo no válido para actualización")

    def close_con(self):
        self.connection.close()
        print("Conexión a Base de Datos finalizada")
