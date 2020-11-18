import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

myClient = MongoClient()

# Criando conexão com a banco de dados


def isConn():
    try:
        myClient = MongoClient(host='localhost', port=27017)
        return True
    except ConnectionFailure:
        return False


def main():
    if(isConn):
        # Criando banco de dados
        myDB = myClient.myDB

        user_doc = {
            "username": "Hashirama",
            "firstname": "Matias",
            "surname": "Mani",
            "email": "matiasdev30@gmail.com",
            "time": "OMNI"
        }

        #Inserindo documento na coleção, se a coleção não estiver criada sera criada
        myDB.users.insert_one(user_doc)

        #Mostrar todas BD
        print(myClient.list_database_names())
        #Mostrar todas coleções da minha BD
        print(myDB.list_collection_names())
    else:
        print('Conexão não estabelecida')


if __name__ == '__main__':
    main()
