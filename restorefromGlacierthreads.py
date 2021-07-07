import concurrent.futures
import boto3

sess = boto3.session.Session()
client = sess.client("s3")


def restore_from_glacier(bucket, file):
    obj = sess.resource('s3').Object(bucket, file)
    #print(obj.storage_class)
    if obj.storage_class == 'GLACIER' and obj.restore is None:
        resp = client.restore_object(
            Bucket=bucket,
            Key=file,
            RestoreRequest={
                'Days': 80,
                'GlacierJobParameters': {
                    'Tier': 'Bulk'
                }
            }
        )
        print(resp.get('ResponseMetadata').get('HTTPStatusCode'))
        return resp


bucketname = 'bucket_name'
my_bucket = sess.resource('s3').Bucket(bucketname)
files = my_bucket.objects.all()
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = []
    for f in files:
        #print(f.key)
        futures.append(executor.submit(restore_from_glacier(bucketname,f.key)))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
