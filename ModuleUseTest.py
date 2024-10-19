#This is used for testing the module and is not apart of the end project,
# Ether remove me manually or make a Tests folder and use the .ignore file to handled me.
import ToASCII
from PIL import Image
from PIL import ImageEnhance

path = "TestImages/big_tree.png"

my_image = Image.open(path)

# Some char_sets gradients that might be good ascetically
# Each one ordered from highest intensity to lowest
# " .:-=+*#%@" 
# "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
char_gradient =  " .:-=+*#%@"[::-1]
 
print(ToASCII.convert_image_to_ascii(my_image, 140,-1, char_gradient))