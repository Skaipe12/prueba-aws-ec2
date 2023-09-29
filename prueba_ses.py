import boto3
from botocore.exceptions import ClientError

#credenciales de acceso
aws_access_key_id = 'AKIAQOF6SJBHBUTKUL6R'
aws_secret_access_key = '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'
region_name = 'us-east-1'

#cliente de SES con las credenciales
ses = boto3.client(
    'ses',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# detalles del correo
sender_email = 'brayan.estrada@eia.edu.co' 
recipient_email = 'estradaramosb@gmail.com'
subject = 'Ejemplo Mensaje SES 2'
body_text = 'Este es un correo electrónico de prueba enviado desde Amazon SES.'

# envío del correo 
try:
    response = ses.send_email(
        Source=sender_email,
        Destination={
            'ToAddresses': [recipient_email],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body_text,
                }
            },
        },
    )

    # Imprime el mensaje de respuesta de SES
    print("Correo electrónico enviado correctamente: MessageId:", response['MessageId'])

except ClientError as e:
    print("Error al enviar el correo electrónico:", e)
