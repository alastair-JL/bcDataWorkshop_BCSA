# This is the Python program that will sort the pictures into separate folders
# import necessary libraries
import boto3
import os
from botocore import UNSIGNED
from botocore.client import Config
from s3Download import listObjectKeys

# This function will take a photolink, and extract the address of the photo
def extract_address(photoLink):

    address = photoLink.split('/')[-2]+'/'+photoLink.split('/')[-1]
  
    return address


def download_image(path,target):
    # initialize s3 client
    s3_anon = boto3.client('s3', region_name='ca-central-1',
                       config=Config(signature_version=UNSIGNED))
    # Download the specific image
    
    key='Photos/UBC Image Data/docs/'+path
    #fileName = './tmp/'+path.split('/')[1]
    fileName = target+path.split('/')[1]
    
    print(fileName)
   # s3_anon.download_file(Bucket='bcsa-data', Key=key, Filename='./tmp/temp.png')
    s3_anon.download_file(Bucket='bcsa-data', Key=key, Filename=fileName)
    return 0

# This function will download an image into the 'tmp' directory as 'temp.png'
def download_image_as_tmp(path):
    # initialize s3 client
    s3_anon = boto3.client('s3', region_name='ca-central-1',
                       config=Config(signature_version=UNSIGNED))
    # Download the specific image
    
    key='Photos/UBC Image Data/docs/'+path
    
    print(path)
    s3_anon.download_file(Bucket='bcsa-data', Key=key, Filename='./tmp/temp.png')
    #s3_anon.download_file(Bucket='bcsa-data', Key=key, Filename=fileName)
    return 0

# This function will take a photolink string, extract the address of it, and download the image into
# the appropriate folder based on a hazard rating.
def sort_image(photoLink, hazardRating):
    
    # First we use the extract address function to get path of the image file
    image_path = extract_address(photoLink)
   
    
    # Now we score the image into low or high 
    if(hazardRating >= 3):
        category='high'
    else:
        category='low'
            
    
    # Now we download the image into the appropriate folder
    target = './'+category+'/'
    
    print('hazard rating of image: '+ category +'\n')
    print('downloaded to: '+ './tmp/temp.png')
    
    download_image(image_path,target)
    
    return 0

# Will download an image into the tmp folder, and return the label of the image
def download_image_into_tmp(photoLink, hazardRating):
    
    # First we use the extract address function to get path of the image file
    image_path = extract_address(photoLink)
   
    
    # Now we score the image into low or high 
    if(hazardRating >= 3):
        category='high'
    else:
        category='low'
            
    
    # Now we download the image into the appropriate folder
    target = './'+category+'/'
    
    print('hazard rating of image: '+ category +'\n')

    download_image_as_tmp(image_path)
    
    statinfo = os.stat('./tmp/temp.png')    # Call up some info about the image
    Size = statinfo.st_size/(1024**2) # Retrieve the size of the image
    
    return category,Size

