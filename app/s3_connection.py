import os
import boto3
from botocore.exceptions import NoCredentialsError
from botocore.exceptions import ClientError
import logging
from flask import flash

s3 = boto3.client('s3')#,
                    #aws_access_key_id = os.environ.get('aws_access_key_id'),
                    #aws_secret_access_key = os.environ.get('aws_secret_access_key'))
BUCKET_NAME = os.environ.get('BUCKET_NAME')

def upload_s3(file, file_name):
    try:
        s3.upload_fileobj(file, BUCKET_NAME, file_name)
        return True
    except FileNotFoundError:
        flash('Arquivo não encontrado.')
        return False
    except NoCredentialsError:
        flash('Credencial não disponível.')
        return False


def download_s3(file_name, expiration=3600):

    try:
        url = s3.generate_presigned_url(
            ClientMethod='get_object', Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name},
                ExpiresIn=expiration)

    except FileNotFoundError:
        flash('Arquivo não encontrado.')
        return None
    except NoCredentialsError:
        flash('Credencial não disponível.')
        return None
    except ClientError as e:
        logging.error(e)
        return None

    return url