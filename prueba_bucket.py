import requests
import os
import boto3
import json

# Configuracion las credenciales de AWS
aws_access_key_id = 'AKIA52YRKZTVDBLQ46N5'
aws_secret_access_key = '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'
bucket_name = 'so-bucket-brayantavo'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

categories_url = "https://fakestoreapi.com/products/categories"
response = requests.get(categories_url)

if response.status_code == 200:
    categories_data = response.json()

    # Se itera sobre las categorias
    for category_name in categories_data[:2]:
        # Crear una carpeta para la categoría en S3
        s3_folder = f"brayayin-tavo/{category_name}"
        s3.put_object(Bucket=bucket_name, Key=f"{s3_folder}/")

        # Realizar una solicitud GET a la API de productos por categoría
        products_url = f"https://fakestoreapi.com/products/category/{category_name}"
        response = requests.get(products_url)

        if response.status_code == 200:
            products_data = response.json()

            # Guardar los datos de los productos en la carpeta correspondiente en S3
            for product in products_data[:2]:
                product_name = product['title']

                # Crear un archivo JSON para cada producto
                product_json = json.dumps(product)
                s3.put_object(Bucket=bucket_name, Key=f"{s3_folder}/{product_name}.json", Body=product_json)

else:
    print("Error en la solicitud a la API de categorías")
