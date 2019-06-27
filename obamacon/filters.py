from PIL import Image

# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file_name):
    img = Image.open(file_name)
    return img
    


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img_object):
    img_object.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
# def save_img(object type, string type)
# save_name is name of image; currently placeholder
# 
def save_img(img_object, save_name):
    img_object.save(save_name)
    
#holds on image object (testing)
img = load_img("guessilldie.jpg")
save_img(img, "cat.jpg")


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img_object):
    # create new empty list where you will put all new pixel values into (hint: use append)
    original_pixels = img_object.getdata()
    # Use for loop to iterate through every single pixel
        # at every pixel, sum up the RGB values
        # use conditionals and boolean checks (if else) to determine which new color to change to 
