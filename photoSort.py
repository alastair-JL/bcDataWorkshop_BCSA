
# This is the Python program that will sort the pictures into separate folders


# This function will take a photolink, and extract the address of the photo
def extract_address(photoLink):

    address=photoLink.split('/')[-2]+'/'+photoLink.split('/')[-1]
    
    return address





# This function will take a photolink string, extract the address of it, and download the image into
# the appropriate folder based on a hazard rating.
def sort_image(photoLink):
    
    
    
    return 0