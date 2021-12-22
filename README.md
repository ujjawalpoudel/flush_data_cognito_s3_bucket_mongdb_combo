# flush_data_cognito_s3_bucket_mongdb_combo
This project help us to flush data from conginto, s3 bucket and mongdb combined

**Step 1**
Create Virtual Environment of python3.7
```
python3.7 -m venv venv
```
**Step 2**
Activate Virtual Environment
```
source venv/bin/activate
```
**Step 3**
Install all packages from requirement.txt
```
pip install -r requirements.txt
```
**Step 4**
Create .env file and edit according to your configuration
```
STAGE=stage_name
DB_HOST=cluster0.****.mongodb.net (as like this)
DB_USER=mongodb user name
DB_PASSWORD=mongodb password
DB_NAME_PREFIX=buildingdecision(database name except stage name(Example dev, test, prod))
USER_POOL_ID_STAGE = user_pool_id for stage
S3_BUCKET_NAME_STAGE = s3 bucket name for stage
```
**Step 5**
Excecute main.py file
```
python main.py
```
