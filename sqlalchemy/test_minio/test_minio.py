import boto3

# s3 = boto3.resource(service_name='s3', endpoint_url="http://localhost:9000")

# for bucket in s3.buckets.all():
#     print(bucket.name)

# print(s3.meta.client)
# s3.create_bucket(Bucket='test_bucket')
# print(s3.list_buckets())

# Kết nối với minio
s3 = boto3.resource('s3', aws_access_key_id='access_key',
         aws_secret_access_key= 'secret_key', endpoint_url="http://localhost:9000")

# Tạo bucket mới
# s3.create_bucket(
#       Bucket='test1')

# Upload image/file
# Cách 1:
# s3.Bucket('test').put_object(Key='Fc.jpg', Body=data)

# Cách 2:
data = open('/media/tranhau/hdd/training/sqlalchemy/test_minio/Fc.jpg', 'rb')
s3.meta.client.put_object(
    Bucket='test', 
    Key='Fc1113.jpg', 
    Metadata={
        'Content-type': 'image/jpeg',
        'user': 'tran hau'
        },
    Body=data,
    ContentType='image/jpeg'
    )

# data = open('/media/tranhau/hdd/training/sqlalchemy/test_minio/hello.txt', 'rb')
# s3.meta.client.put_object(Bucket='test', Key='hello.txt', Body=data, ContentType='text/txt')

# Lấy link ảnh
url = s3.meta.client.generate_presigned_url('get_object', ExpiresIn=100, Params={'Bucket': 'test', 'Key': 'Fc1113.jpg'})

print(url)