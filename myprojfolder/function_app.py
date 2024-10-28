
import azure.functions as func
import datetime
import json
import logging
import pymongo

app = func.FunctionApp()

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    nome = req.params.get('nome')

    uri = "mongodb+srv://giorgio2006:TWoA7kZsvL30k6Ua@cluster0563.wr9rvs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0563"
    client = pymongo.MongoClient(uri)
    db = client.ingredients
    cir = db.noael
    document = cir.find_one({'ingrediente': nome})
    if document:
        return func.HttpResponse(document['testo'])


        

    