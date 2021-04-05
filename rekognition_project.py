# webcam photo click
# pip install opencv-python

import cv2
cap = cv2.VideoCapture(0)
myphoto = "mypicture.jpg"
ret, photo = cap.read()
cv2.imwrite(myphoto , photo)
cap.release()

# upload photo to cloud object storage s3
region = "ap-south-1"
bucket = "ai-on-aws-workshop"
upload_img = "file.jpg"

# pip install boto3
# pip install aws
# login to aws using aws configure command (Create IAM user and provide access key id and secret access key)
import boto3
s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myphoto, upload_img)

# connect rek 
rek = boto3.client('rekognition', region)
response = rek.detect_labels(

    Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upload_img,
          }
      },
      MaxLabels=10,
      MinConfidence=90
)

for i in range(4):
    print (response['Labels'][i]['Name'])