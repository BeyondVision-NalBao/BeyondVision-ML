from google.cloud import storage

bucket_name = ''    # 서비스 계정 생성한 bucket 이름 입력
source_file_name = ''    # GCP에 업로드할 파일 절대경로
destination_blob_name = ''    # 업로드할 파일을 GCP에 저장할 때의 이름


storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)