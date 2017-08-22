
# This is the Python program that will sort the pictures into separate folders


# This function will take a photolink, and extract the address of the photo
def extract_address(photoLink):
    
    address = photoLink.split('/')[-2]+'/'+photoLink.split('/')[-1]
  
    return address




# This function will download an image into 
def download_image(path):
    
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
    
    
    
    
    return 0