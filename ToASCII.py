"""A module used to convert an Pillow Image into an ASCII art representation.

Functions:
    convert_image_to_ascii
    
Author:
    By William VB 
    
See Project On GITHUB: 
    https://github.com/williamVbrines/ImageToASKII-ProjectExample
    
NOTES / LICENSE: Did you know the default license is all rights reserved in the 
United States and is given on the time of creation, with no need to state it. 
Neat isn't it. However it is nice to give it to people as fluff or deterrent.
See the project license on GITHUB or that file that strangely was removed. ;)
"""

import string
from PIL import Image

##Public

def convert_image_to_ascii(
    image : Image , 
    output_width : int = 80 , 
    output_height : int = -1 ,
    character_set : string = " `:;+#@" , 
    delimiter : chr = '\n'
    ) -> string :
    """Converts a Pillow(PIL) Image into a string of characters that represent 
    the intensity of the pixels in the image.
    In less technical terms, this function turns an image into ASCII art.
    
    Keyword arguments: 
        image (Pillow Image) -- The image you want to convert. 
    
        output_width (int , default 80) -- The output width in characters. 
        Set to -1 to adjust width to keep aspect ratio.
    
        output_height (int , default -1) -- The output height in characters. 
        Set to -1 to adjust height to keep aspect ratio.
    
        character_set (string , default "`:;+#@") -- The characters ordered 
        from Dark -> Light that are selected to form the ASCII image.
    
        delimiter (chr , default '/n') -- The separator for each line of 
        characters.  
    
    Return (string) -- A string separated by newlines that represents the image
    in ASCII.
    
    Notes:
        !!Issues may arise if you set an output height or output width to zero!!
        !!Be warred an large output width and height takes a lot of processing!!
        Another common character_set you may want to try is:
        $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'.
        or 
        @#+:;' 
    """
    result = ""
    
    resized_image = _resize_image_for_ascii(image,output_width,output_height)
   
    intensity_range = _get_intensity_range(resized_image)
    
    for y_position in range(0, resized_image.size[1]):
        for x_position in range(0, resized_image.size[0]) :
           
            pixel_band = resized_image.getpixel((x_position , y_position,))
            pixel_intensity = _get_band_luminance(pixel_band)
            
            pixel_intensity = _maximize_pixel_contrast(
                              pixel_intensity, 
                              intensity_range, 
                              0.05)
          
            result += _select_character(pixel_intensity, character_set)
        
        result += delimiter
        
    return result

##Private

def _resize_image_for_ascii(
    image : Image ,
    output_width : int = -1,
    output_height : int = -1,
    char_aspect : float = 2.0
    ) -> Image :
    """Resizes the image such that each pixel represents 1 character. 

    Keyword arguments:
        image (Pillow (PIL) Image) -- The image to resize
        
        output_width (int , default -1) -- The output width in characters. 
        Set to -1 to adjust width to keep aspect ratio. 
        
        output_height (int , default -1) -- The output height in characters. 
        Set to -1 to adjust height to keep aspect ratio.
        
        char_aspect (float , default = 2.0) -- The ratio between each the height 
        and width of a character.
        
    Return (Pillow (PIL) Image) -- The resized image 
    
    NOTES: output_width and output_height should not be zero
    Setting both output_width and output_height may stretch the image it is 
    Strongly suggest to keep the aspect ratio in some way.
    An char_aspect ratio of 2.0 approximates most mono-space fonts
    """
    if output_width <= -1 and output_height <= -1:
        output_width = image.size[0]
        output_height = image.size[1]
    
    elif output_width <= -1 and output_height > -1:
        #Possible div by zero, which will be handled by _safe_divide
        #Man I really don't like how I had to format the below
        output_width = int(
                       _safe_divied( image.size[0], image.size[1]) * 
                       output_height * 2) 
   
    elif output_height <= -1 and output_width > -1:
        #Possible div by zero, which will be handled by _safe_divide
        output_height = int(
                        _safe_divied( image.size[1], image.size[0]) * 
                        output_width * 0.5) 
    
    if output_height == 0 or output_width == 0:
        return ""
        
    return image.resize((output_width,output_height),0)
    
def _get_intensity_range(image : Image) -> tuple:
    """Gets the lowest intensity and the highest intensity value in the image.

    Keyword arguments:
        image (Pillow (PIL) IMAGE) 

    Return (tuple) -- (minimum intensity , maximum intensity) 
    """
    
    #I don't want to add the math module just for INF so float("inf") it is
    minimum_intensity = float("inf") 
    maximum_intensity = -float("inf")
    
    for y_position in range(0, image.size[1]):
        for x_position in range(0,image.size[0]) :

            pixel_band = image.getpixel((x_position , y_position,))
            
            pixel_intensity = _get_band_luminance(pixel_band)
            
            minimum_intensity = min(minimum_intensity, pixel_intensity)
            maximum_intensity = max(maximum_intensity, pixel_intensity)
                
    return (minimum_intensity, maximum_intensity)
    
def _get_band_luminance(band : tuple) -> float:
    """Gets the luminance generated by the weighted sums of the band 

    Keyword arguments:
        band (tuple) -- (RED, GREEN, BLUE) The color values ranging from 0 - 255
    
    Return (float) -- description 
    NOTE: May ERROR out if unexpected bands come from the image
    """
    #Alternative luminance formulas 
    #return 0.299 * band[0] + 0.587 * band[1] + 0.114 * band[2] #SDTV
    #return 0.212 * band[0] + 0.701 * band[1] + 0.087 * band[2] #Adobe
    #return 0.2627 * band[0] + 0.6780 * band[1] + 0.0593 * band[2] #UHDTV 
    
    return 0.2126 * band[0] + 0.7152 * band[1] + 0.0722 * band[2] #HDTV

def _maximize_pixel_contrast(
    intensity : float, 
    intensity_range : tuple, 
    intensity_offset_percentage : float = 0.0
    ) -> float:
    """Changes the intensity such that it has a high difference between 
    intensities, by stretching the min and max values to 0 - 255 and reassigning
    the intensity relatively to the new minimum and maximum.

    Keyword arguments:
        intensity (float) -- The initial intensity within the intensity_range
        
        intensity_range (tuple) -- 
        ( miniumum_intensity : float  , maximum_intensity : float) 
        
        intensity_offset_percentage (float , default 0) -- How fare the 
        intensity_range is stretched beyond the 0 and 255. This helps if 
        intensity_range contains an outlier, such as  minimum intensity not
        being indicative of whole images minimum. 
        
    Return (float) -- The corrected intensity 
    
    NOTES: lintensity_offset_percentage is suggested to be at 0.5.
    """
    
    total_intensity = (intensity_range[0] - intensity_range[1])
    
    offseted_max_insenity = intensity_range[1] 
    offseted_max_insenity += total_intensity * intensity_offset_percentage
    
    offseted_min_intensity = intensity_range[0] 
    offseted_min_intensity -= total_intensity * intensity_offset_percentage
    
    new__intensity = intensity - offseted_min_intensity
    new__intensity /= offseted_max_insenity - offseted_min_intensity
    new__intensity = _clamp( 255 * new__intensity, 0, 255)
    
    return new__intensity
	
def _select_character(pixel_intensity : float , character_set : string) -> chr:
    """Selects a character from the a sting ordered from Dark -> Light based off
    the an intensity. which will will be mapped uniformly to the character_set

    Keyword arguments:
        pixel_intensity (float)- ranges from 0 - 255
        
        character_set (string , default \"`:;+#@\") -- The characters ordered 
        from Dark -> Light. 
    
    Return (chr) -- A character from the character_set
    """
    #Maps value uniformly to an index within range of the char_set
    index = int(((len(character_set)-1) / 255) * pixel_intensity) 
    return character_set[index]
   
##Utility Functions

#NOTE: Would normally separate these into another module, however there is no
#need to, for these functions wont be used across multiple modules nor need to  
#be logically separated as like a class.

def _safe_divied(x,y, default = 0):
    """Safely divides two numbers and if would divide by 0 return a default
     
    Keyword arguments:
        x -- number
        y -- number
        default (default 0) -- what will be returned on divide by zero
        
    Return : result or default
    
    NOTE : Be careful, great errors comes with great responsibility.
    """
    try:
        return x / y
    except ZeroDivisionError:
        return default
        
def _clamp(value, min_value, max_value) :
    """Returns the value clamped between the min and a max values"""
    return min(max( value, min_value), max_value)
    
#Deprecated Functions

#def _get_band_average(band : tuple) -> float:
#'''Use to generate a gray-scale value from a color band, returns a float
#Deprecated for _get_band_luminance which better represents the intensity.
#'''
#    return (band[0] + band[1] + band[2]) / 3
    