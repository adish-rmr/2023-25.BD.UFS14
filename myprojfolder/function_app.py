
import azure.functions as func
import datetime
import json
import logging
import pymongo

app = func.FunctionApp()

@app.route(route="MyHttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def MyHttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    nome = req.params.get("name")
    try:
        nome
    except:
        nome = "Formaldehyde"
    try:
        uri = "mongodb+srv://giorgio2006:TWoA7kZsvL30k6Ua@cluster0563.wr9rvs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0563"
    except:
        return func.HttpResponse('error data')
    try:
        client = pymongo.MongoClient(uri)
        db = client.ingredients
        cir = db.noael
    except:
        return func.HttpResponse('client error')
    try:
        document = cir.find_one({'ingrediente': nome})
    except:
        return func.HttpResponse('find error')
    if document:
        return func.HttpResponse(document['testo'])


        

    