import json


def hello(event, context):
    body = {
        "message": "Nombre: Karol Vanessa Vitonco Burbano / edad: 24 años / Ciudad: Calarca - Quindio / Correo:karol.vitonco.5559@eam.edu.co",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

