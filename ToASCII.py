import string
from PIL import Image

if __name__ == '__main__':
    import sys
    print("This is to know if this is running as a terminal program or module")
    
def _safe_divied(x,y, default = 0):
    try:
        return x / y
    except ZeroDivisionError:
        return default;
    
def convert_image_to_ascii(image : Image , max_width : int = -1, max_height : int = -1, character_set : string = " `:;+#@") -> string :
    result = "";
    
    if max_width <= -1 and max_height <= -1:
        max_width = image.size[0]
        max_height = image.size[1]
    
    elif max_width <= -1 and max_height > -1:
        max_width = int(_safe_divied(image.size[0] , image.size[1]) * max_height) #Possible div by zero, handled by _safe_divide
    elif max_height <= -1 and max_width > -1:
        max_height = int(_safe_divied(image.size[1] , image.size[0]) * max_width) #Possible div by zero, handled by _safe_divide
    
    if max_height == 0 or max_width == 0:
        return "";
        
    image_resized = image.resize((max_width,max_height),0)
   
    average_pixel_value_range = _get_average_pixel_value_range(image_resized)
                
    for y_position in range(0, image_resized.size[1]):
        for x_position in range(0,image_resized.size[0]) :
           
            pixel_band = image_resized.getpixel((x_position , y_position,))
            average_pixel_vlaue = (pixel_band[0] + pixel_band[1] + pixel_band[2]) / 3
            
            result += _select_char(average_pixel_vlaue, average_pixel_value_range[0], average_pixel_value_range[1], character_set);
        
        result += "\n";
        
    return result;
    
def _select_char(value : float , min : float, max : float, character_set : string) -> chr:
    index = int( ( (len(character_set)-1) / (max - min)) * (value - min)) #Maps value uniformly to an index within range of the char_set
    return character_set[index]
    
def _get_image_average_pixel_value_range(image : Image) -> tuple:
    minumum_average_pixel_vlaue = 255.0;
    maximum_average_pixel_vlaue = 0.00001;
    
    for y_position in range(0, image.size[1]):
        for x_position in range(0,image.size[0]) :

            pixel_band = image.getpixel((x_position , y_position,))
            average_pixel_vlaue = (pixel_band[0] + pixel_band[1] + pixel_band[2]) / 3

            if average_pixel_vlaue < minumum_average_pixel_vlaue:
                minumum_average_pixel_vlaue = average_pixel_vlaue;
           
            if average_pixel_vlaue > maximum_average_pixel_vlaue:
                maximum_average_pixel_vlaue = average_pixel_vlaue;
                
    return (minumum_average_pixel_vlaue, maximum_average_pixel_vlaue);