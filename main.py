import os
import boto3
import pymongo
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.resource("s3")
client = boto3.client("cognito-idp")

stage = os.getenv("STAGE")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name_prefix = os.getenv("DB_NAME_PREFIX")
host = os.getenv("DB_HOST")

if stage == "stage":
    USER_POOL_ID = os.getenv("USER_POOL_ID_STAGE")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME_STAGE")
    database_name = f"{db_name_prefix}_{stage}"

if stage == "dev":
    USER_POOL_ID = os.getenv("USER_POOL_ID_DEV")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME_DEV")
    database_name = f"{db_name_prefix}_{stage}"

if stage == "test":
    USER_POOL_ID = os.getenv("USER_POOL_ID_TEST")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME_TEST")
    database_name = f"{db_name_prefix}_{stage}"

if stage == "prod":
    USER_POOL_ID = os.getenv("USER_POOL_ID_PROD")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME_PROD")
    database_name = f"{db_name_prefix}_{stage}"

# Lists the users in the Amazon Cognito user pool.
response = client.list_users(
    UserPoolId=USER_POOL_ID,
)

for user in response["Users"]:
    # Deletes a user as an administrator. Works on any user.
    client.admin_delete_user(
        UserPoolId=USER_POOL_ID,
        Username=user["Username"],
    )

# Empty particular S3 Bucket
bucket = s3.Bucket(S3_BUCKET_NAME)
bucket.objects.all().delete()

db_uri = f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(db_uri)
mydb = myclient[database_name]

# Lists all collections of particular database
for coll in mydb.list_collection_names():
    mycol = mydb[coll]
    mycol.drop()
