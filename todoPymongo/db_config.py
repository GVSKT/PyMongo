import pymongo

def pymongo_db():
    try:
        #client = pymongo.MongoClient('mongodb+srv://username:password@localhost:27017/demopymongo?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        dblist = myclient.list_database_names()
        mydb = myclient["pymongodemodb"]["todoPymongo_demo"]
        return mydb

    except Exception as ex:
        print("\nError At pymongo_db : ", str(ex))


