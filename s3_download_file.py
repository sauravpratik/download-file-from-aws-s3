from boto3 import client
import boto3
import os


aws_key = 'XXXXXXXXXXXXX'   # provide your aws access key
aws_secret = 'YYYYYYYYYYY'  # provide your aws secret

connection = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id=aws_key,
    aws_secret_access_key=aws_secret
)


bucket_name = 'XXXXXXXXXXX'  # provide the S3 bucket name from which you want to download file
prefix_name = 'XX'    # provide the prefix if present


download_path = input('Where you want to download the files:')


if download_path == '':
	print("Pls provide download path")
	exit(1)

else:
    paginator = connection.get_paginator("list_objects")
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix_name)

    for page in page_iterator:
        if "Contents" in page:
            for key in page["Contents"]:
                    keyString = key["Key"]
                    print(keyString)
                    (path_splitted, file) = os.path.split(keyString)
                    download_path_local = download_path + '/' + path_splitted + '/' + file
                    os.makedirs(download_path + '/' + path_splitted, exist_ok=True)

                    connection.download_file(bucket_name, keyString, download_path_local)
                    print("File Downloaded" + file )

    print("Download Complete")
