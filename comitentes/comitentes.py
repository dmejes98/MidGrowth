from sql_comitentes import DataBase


def com_run(comitentes):

    flag = True
    while flag:
        print(
            """
        COMITENTES
        
        Seleccione: 
        1. Consultar un comitente.
        2. Consultar todos los comitentes.
        3. Insertar nuevo comitente.
        4. Actualizar un comitente.
        5. Salir
        """
        )

        try:
            sel = int(input("Digite su selección: "))
            if sel in [1, 2, 3, 4, 5]:
                if sel == 1:
                    id_consulta = int(
                        input("Ingrese el id del comitente a consultar: ")
                    )
                    result_consulta = comitentes.select_user(id_consulta)
                    print(result_consulta)
                    return result_consulta
                elif sel == 2:
                    result_consulta = comitentes.select_all_users()
                    print(result_consulta)
                    return result_consulta
                elif sel == 3:
                    comitentes.insert_user()
                elif sel == 4:
                    id_update = int(input("Ingrese el id del comitente a actualizar: "))
                    comitentes.update_user(id_update)
                else:
                    flag = False

            else:
                print("Selección incorrecta. Intente de nuevo.")

        except Exception as e:
            print(e)


if __name__ == "__main__":

    comitentes = DataBase()
    result = com_run(comitentes)
    comitentes.close_con()
