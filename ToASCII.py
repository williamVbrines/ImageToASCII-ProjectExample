import string
from PIL import Image

if __name__ == '__main__':
    import sys
    print("This is to know if this is running as a terminal program or module")
    


def convert_image_to_ascii(image : Image , max_width : int = -1, max_height : int = -1, character_set : string = " `:;+#@") -> string :

    result = "";
    
    resized_image = _resize_image_for_ascii(image,max_width,max_height)
   
    intensity_range = _get_intensity_range(resized_image)
    
    for y_position in range(0, resized_image.size[1]):
        for x_position in range(0, resized_image.size[0]) :
           
            pixel_band = resized_image.getpixel((x_position , y_position,))
            pixel_intensity = _get_band_luminance(pixel_band)
            #pixel_intensity = _get_band_average(pixel_band)
            
            pixel_intensity = _maximize_pixel_contrast(pixel_intensity, intensity_range, 0.05)
          
            result += _select_character(pixel_intensity, character_set);
            #result += _select_character(pixel_intensity, intensity_range[0], intensity_range[1], character_set);
        
        result += "\n";
        
    return result;

def _resize_image_for_ascii(image : Image , max_width : int = -1, max_height : int = -1, char_aspect : float = 2.0) -> Image :
    if max_width <= -1 and max_height <= -1:
        max_width = image.size[0]
        max_height = image.size[1]
    
    elif max_width <= -1 and max_height > -1:
        max_width = int(_safe_divied(image.size[0] , image.size[1]) * max_height * 2) #Possible div by zero, handled by _safe_divide
    elif max_height <= -1 and max_width > -1:
        max_height = int(_safe_divied(image.size[1] , image.size[0]) * max_width * 0.5) #Possible div by zero, handled by _safe_divide
    
    if max_height == 0 or max_width == 0:
        return "";
        
    return image.resize((max_width,max_height),0)
    
def _get_intensity_range(image : Image) -> tuple:
    minumum_intensity = 255.0;
    maximum_intensity = 0.00001;
    
    for y_position in range(0, image.size[1]):
        for x_position in range(0,image.size[0]) :

            pixel_band = image.getpixel((x_position , y_position,))
            pixel_intensity = _get_band_luminance(pixel_band)
            #pixel_intensity = _get_band_average(pixel_band)
            
            minumum_intensity = min(minumum_intensity, pixel_intensity)
            maximum_intensity = max(maximum_intensity, pixel_intensity)
                
    return (minumum_intensity, maximum_intensity);
    
# def _get_band_average(band : tuple) -> float:
    # return (band[0] + band[1] + band[2]) / 3
    
def _get_band_luminance(band : tuple) -> float:
    #return 0.299 * band[0] + 0.587 * band[1] + 0.114 * band[2] #SDTV
    #return 0.212 * band[0] + 0.701 * band[1] + 0.087 * band[2] #Adobe
    
    #return 0.2627 * band[0] + 0.6780 * band[1] + 0.0593 * band[2] #UHDTV 
    return 0.2126 * band[0] + 0.7152 * band[1] + 0.0722 * band[2] #HDTV

def _maximize_pixel_contrast(intensity , intensity_range : tuple, intensity_offset_percentage : float = 0.0):
    total_intensity = (intensity_range[0] - intensity_range[1])
    offseted_max_insenity = intensity_range[1] + total_intensity * intensity_offset_percentage
    offseted_min_intensity = intensity_range[0] - total_intensity * intensity_offset_percentage
    
    return _clamp( 255 * ((intensity - offseted_min_intensity) / (offseted_max_insenity - offseted_min_intensity)), 0, 255)
	
def _select_character(pixel_intensity : float , character_set : string) -> chr:
    index = int(((len(character_set)-1) / 255) * pixel_intensity) #Maps value uniformly to an index within range of the char_set
    return character_set[index]
   
#Utility Functions, Could separate into another module but it is one function and wont be used across modules.
def _safe_divied(x,y, default = 0):
    try:
        return x / y
    except ZeroDivisionError:
        return default;
        
def _clamp(value, min_value, max_value) :
    return min(max( value, min_value), max_value)