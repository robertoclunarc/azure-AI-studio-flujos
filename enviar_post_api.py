from promptflow import tool
import requests

def enviar_post_api(url, body, token, tlf):
    try:
        body = {
             "messaging_product": "whatsapp",
             "recipient_type": "individual",
             "to": tlf, 
             "type": "text",
             "text": {
                 "preview_url": False,
                 "body": body
             }             
        }
        header = {
         'Content-Type': 'application/json',
         'Authorization': f'Bearer {token}'
        }
        # Realizar la solicitud POST
        response = requests.post(url, json=body, headers=header)

        # Verificar el código de respuesta
        if response.status_code == 200:
            print("Solicitud POST exitosa")
        else:
            print(f"Error en la solicitud POST. Código de respuesta: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error: {e}")


@tool
def echo(input: str, urlnotificwhatsapp: str, token: str, telef: str) -> str:
    enviar_post_api(urlnotificwhatsapp, input, token, telef)
    return input
