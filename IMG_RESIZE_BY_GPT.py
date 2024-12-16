#this code will change the size of inputted image

#we have to install pillow for this code
#pip install pillow
from PIL import Image

#create a function which will get all the user inputs
def get_user_input():
    image_path = input("Enter the path to the image file: ")
    new_width = int(input("Enter the new width (in pixels): "))
    new_height = int(input("Enter the new height (in pixels): "))
    return image_path, new_width, new_height

#create a function which will resize the image as per the required dimensions(in pixels)
def resize_image(image_path, new_width, new_height):
    try:
        image = Image.open(image_path)
        resized_image = image.resize((new_width, new_height))
        resized_image.show()
        print("Image resized successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Welcome to the Image Resizer!")
    image_path, new_width, new_height = get_user_input()
    resize_image(image_path, new_width, new_height)
