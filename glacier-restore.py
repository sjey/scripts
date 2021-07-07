import boto3


def restore(bucket):
    s3 = boto3.resource('s3')

    my_bucket = s3.Bucket(bucket)

    i = 0
    for file in my_bucket.objects.all():
        obj = s3.Object(file.bucket_name, file.key)
        #print(file.key, file.storage_class, obj.restore)
        if file.storage_class == 'GLACIER' and obj.restore == None:
            i += 1
            # print(file.key)
            resp = my_bucket.meta.client.restore_object(
                Bucket=file.bucket_name,
                Key=file.key,
                RestoreRequest={
                    'Days': 80,
                    'GlacierJobParameters': {
                        'Tier': 'Bulk'
                    }
                }
            )
            if resp.get('ResponseMetadata').get('HTTPStatusCode') != 202:
                print(file.key, obj.restore, resp)

    print(bucket, i)


if __name__ == '__main__':
    restore('bucket_name')
