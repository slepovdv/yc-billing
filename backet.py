import boto3
import os
import io
from dotenv import load_dotenv


def aws_session(region_name='ru-central1'):
    return boto3.session.Session(aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID_BILLING'],
                                 aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY_BILLING'],
                                 region_name=region_name)


def get_data(bucket_name, file_name):
    session = aws_session()
    resource = session.resource('s3', endpoint_url='https://storage.yandexcloud.net')
    obj = resource.Object(bucket_name, file_name)
    io_stream = io.BytesIO()
    obj.download_fileobj(io_stream)

    io_stream.seek(0)
    return io_stream.read().decode('utf-8')


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
