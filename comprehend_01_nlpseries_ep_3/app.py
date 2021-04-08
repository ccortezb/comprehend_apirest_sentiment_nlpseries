import json
import boto3

#cliente de comprehend
client = boto3.client('comprehend')

#funcion principal para llamar a comprehend
def lambda_handler(event, context):

    #tomamos los datos del evento json entrante
    print("event puro:", event)
    #Accessing data
    puro = json.dumps(event) #intentando cambiar aqui sino vuelvo a la linea 13
    text = puro[0]
    json_object = json.loads(puro)
    print("texto a analizar: ", json_object["body"])
    Body = json.dumps(json_object["body"])
    print("Body:", Body)

    #detectamos el sentimiento 
    print("iniciando analisis de sentimiento....")
    sentiment = client.detect_sentiment(Text = Body, LanguageCode = 'es') #llamada al API de comprehend detect_semtiment
    sentRes = sentiment['Sentiment'] #los valores posibles son Positive, Neutral, or Negative
    sentScore = sentiment['SentimentScore'] #medicion en porcentajes de los valores conseguidos
    print(sentRes)
    print(sentScore)

    #Entity Extraction en Comprehend
    print("iniciando extraccion de entidades....")
    entities = client.detect_entities(Text = Body, LanguageCode = 'es') #llamada al API para entity extraction
    entities = entities['Entities'] #traer todas las entidades reconocidas
    print(entities)
    textEntities = [dict_item['Text'] for dict_item in entities] #los textos identificados como entidades
    typeEntities = [dict_item['Type'] for dict_item in entities] #el tipo de entidad que pertenece cada texto
    print(textEntities)
    print(typeEntities)
    
    
    return {
        'statusCode': 200,
        'body': str(sentiment) + str(entities) #valor retonado de toda la funcion
    }