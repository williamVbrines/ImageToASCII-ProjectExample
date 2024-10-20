# Technical doc
This document goes in depth into the technical aspects of 
## Deadline
**18-10-2024 (DD-MM-YYYY)**   
On the above date we will reevaluate the deadline and determine if we will continue the project.
### Determining continuation of project 
- Is the project complete if so project ends.
- Is there other ways to accomplish the same task or goal that would spend less time?
- Has the original purpose of the project changed.
- Is our time better spent elsewhere.
## Determining project completeness.
- All test images are converted to ASKII into the terminal via standard out, in which must be visual similar to the original test image.
> We will manually and subjectively verify that the standard out is similar to the test image.
- The project is fully documented and checked for spelling errors.
- The test images will come from the the [Image Compression Benchmark By Rawzor](https://imagecompression.info/test_images/) from the RGB 8 bit set. The images are excluded from this project. This is to have a standard image set, in case others want to test the program.
- The test images will be converted using [GIMP](https://www.gimp.org/) to the most common formats (JPEG, PNG) for that is what we are concerned with.
## Example Output
Below is an image of some ASKII art that this project wants to attempt to construct similar too.

![ASSKII IMAGE](https://upload.wikimedia.org/wikipedia/commons/2/24/Le%C3%B3n_ASCII.JPG)
## Coding language 
We will be using [python](https://www.python.org/) to construct this program.
### Why Python
- The person that I am making the example for is learning python, may be good for them to see code from another to learn from.
- I need to bush up on my python skills.
- Ease of Use, it be a simple programming language with garbage collection.
- Wide platform support, Linx, MacOS, and Windows.
- Don't really need an IDE for it.
- Does not need compilation thus easier to use with Notepad++.

## Version Control
Eh I don't really need Version Control for this project but that is the last words of many people who lost their project. I am NOT willing to take that bet this time around.
Thus I will be using GIT.
### Branching
- I will branch once the initial documentation is made.
- Each branch will represent a signal task which it will be named after.
>- Once the branch is complete it looked over and will be merged.
- Once the project is in working order aka complete a branch will be made as a release named with the project title then a version number. 
- There is no other contributors so no other precautions or complications will be made to the GIT structure. 
## GITHUB
A place online to collaborate and share git repositories
### WHY GITHUB
- The person I am initially making this example for is known to use it.
- For a save file not on my PC. AKA redundancy.
- Interfaces with Git for version control.
- Gives availability to the project. People cant access this project if it is just on my computer.
- Familiarity, people are familiar with it and so am I.
- User experience. 

### GITHUB Desktop
I will use [GitHub desktop](https://desktop.github.com/download/) as my interface with the GITHUB website and version control.
#### WHY GITHUB Desktop
- It is a bother for me and takes time to context switch each time I want to commit something to github.
- The alternative is to use git in the terminal and that user experience is not great.
- My well being and my user experience matters.

## IDE
I am going to use [Notepad++](https://notepad-plus-plus.org/) and the Windows Terminal
### WHY Notepad++
- Syntax highlighting
- Some auto complete
- Easily modifiable with use of plugins.
- Super light weight 
- Under the GNU GENERAL PUBLIC LICENSE
- Supports multiple languages
>- Supports python nativity 
>- And lots more.
- Offline

### Notepad++ Plugins  
#### Markdown Panel
> Allows you to preview your mark down. WHY Because the docs I make are in markdown for the use on GITHUB and I need a way to view it before I commit.  

#### DSpellchek
> Gives spellchecking functionality to notepad++. WHY I am not the best at spelling and in order to communicate well via docs this is a must have.

### Why Windows Terminal
- It is what my machine runs on.
- Supports python
- Has great utility like most terminals
- Has good documentation 
- For the terminal is where the end user will most likely use this program.

## Coding Guidelines  
I would add this if I was doing a larger project. But some simple ones could be.
- Use docstings to explain your modules classes and functions.
```python  
"""Description.

Keyword arguments:
argument (type , default value) -- description
argument (type , default value) -- description
    
Return (type) -- description 
    
Throws:
ERRORCODE
ERRORCODE
    
NOTES: loraipsum loraipsum
loraipsum loraipsum
"""
```
- Do not abbreviate names at all.
> If you need a comment for a variable you did not name it well.
- When you can use a standard library.
- Tabs should be two spaces in length.
- All caps for constants.
- Use Snake Case (Underscore Notation or Lowercase With Underscores) for variable and function names.
- Use the [PEP-8 Guidelines](https://peps.python.org/pep-0008/)

## External Libraries 

### Pillow:
For initial image processing such as file file assess and resizing the [Pilliow](https://python-pillow.org/) module will be used.
#### Why Pillow 
- PIL Pythons imaging library is no longer maintained and available for use, Thus a replacement is wanted.
- Pillow, is open source and free fork of PIL.
- Pillow can read JPEG and PNG files 
- It is commonly used and available.  

### SYS:
Sys is a command line argument reader.[SYS reference](https://docs.python.org/3/library/sys.html)

#### Why SYS
- There is need to gain command line argument information, for the path, max_width, max_height, and export_path.
- Sys is a trusted standard library for python.

#### Alternatives 
- argparse 

## Technical Objectives

### Terminal 
Have the user be able to input a source path to an image of (PNG or JPEG), The convert that image into an ASKII art representation in standard out.

#### Terminal Input:
- Using terminal arguments 
- SOURCE_PATH a required argument to the source image.
- MAX_WIDTH an optional argument can be set to -k or keep to keep aspect ratio or an integer value representing the output width.
- MAX_HEIGHT an optional argument can be set to -k or keep to keep aspect ratio or an integer value representing the output height.
- EXPORT_PATH a optional argument to the export path.
- If the user ever input bad input they should be notified and the USAGE DOC should pop up if applicable.
- TIMES when this is not applicable is in which should inform the user:
>- Pillow not installed.
>- Cant read or write file.
>- File does not exist.
>- Overwriting existing file. ASK if they relay want to.
- CHARACTER_SET the set of characters from white -> black
#### Terminal Input Examples:
```CMD
python TOASKII SOURCE_PATH MAX_WIDTH MAX_HEIGHT EXPORT_PATH
```
```CMD
python TOASKII c:/users/USER/document/apple.png 180 keep c:/users/USER/document/apple.txt
```
Resizes to 180 pixels keeping aspect ratio and exporting to a text file call apple.txt
```CMD
python TOASCII apple.png -1 -1 apple
```
KEEPs the original width and height 
```CMD
python TOASCII apple.png 
```
Displays to Standard out the full image, should warn the user if the image is large.
```CMD
python TOASCII c:/users/USER/document/apple.png 
```
Displays to Standard out the full image, should warn the user if the image is large.
```CMD
python TOASCII
```
Should display a manual of sorts see [USAGE MANUAL](./USAGEMANUAL.md)

### Module 
- A function that takes in a image returns a string separated by newlines. 

## Character Brightness
In search to find the answer to the question to what order and character set should I use to construct the image I found Paul Bourke's notes on it.
[Character representation of grey scale images](https://paulbourke.net/dataformats/asciiart/)
```
Standard" character ramp for grey scale pictures, black -> white.
	"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. "
A more convincing but shorter sequence for representing 10 levels of grey is
   " .:-=+*#%@"
```
Notable the user may want to have their own character set or want to reverse the order of the characters to White -> black. Thus I will add a feature to do so as a parameter in the module and an optional argument in the terminal.
 
## Pixel Value Conversion
I knew from the start the I would need to convert the pixel's RGB value to a single gray-scale value.
My original process was to convert to RGB value by an average.  
```python  
 average_pixel_vlaue = (pixel_band[0] + pixel_band[1] + pixel_band[2]) / 3
```
See the quality of the ASCII representation made me want to find ways to improve a pone it.  
[Wiki Article on lightness](https://en.wikipedia.org/wiki/HSL_and_HSV#Lightness)
What is notable is that Luma weighted value which tries to better represent the pixels perceived lightness.
```
Y = 0.299 * R + 0.587 * G + 0.114 * B #SDTV
Y = 0.212 * R + 0.701 * G + 0.087 * B #Adobe
Y = 0.2126 * R + 0.7152 * G + 0.0722 * B #HDTV
Y = 0.2627 * R + 0.6780 * G + 0.0593 * B #UHDTV 
``` 
Unsure as to which equation to use but I can test to see which is better.

## Contrast and Value Range
I know that not all images will give use the full character set range that can be used, thus decreasing the detail and visibility of shapes in an image.
I attempted to rectify this by adjusting the gray-scale value a pone character selection by uniformly distributing the character set by the min and max gray-scale values of the image.
```python
 index = int( ( (len(character_set)-1) / (max - min)) * (value - min)) #Maps value uniformly to an index within range of the char_set
```
This does uniformly select an index however I suspect doing so would provide a decreased contrast. For if there are pixels that are outliers the min and max value will suffer. Tests and reasoning seem to conclude this by artificially adding a single high value pixel this decreased the overall contrast of the ASCII image. 

A solution to this after some reasoning is to maximize the contrast of the image such that the difference between gray-scale value equals ( 255 / character_set_length ).

I found maximize contrast one can simple stretch the values. See Aryaman Sharda article on [Image Processing Algorithms](https://hackernoon.com/image-processing-algorithms-adjusting-contrast-and-image-brightness-0y4y318a)
```python 
 newIntensity = 255 * ((intensity - minIntensity) / (maxInsenity - minIntensity))
```
A way to help with the outliers was suggested to pick min and max values 5% from them. probably ending in some code similar to the bellow.
```python 
	totalInsenity = (maxInsenity - minIntensity)
	maxInsenity += totalInsenity * 0.05
	minInsenity -= totalInsenity * 0.05
	newIntensity = 255 * ((intensity - minIntensity) / (maxInsenity - minIntensity))
	newIntensity = max(0, min(newIntensity, 255))
```
## Character Aspect Ratio
One of the biggest hampers to the similarity of the original image and the out put image is the stretching that happens due to the aspect ratio of a character being different than that of a pixel.  
![Image of character measurements](./DocImages/WindowsDefaultCharcterAspectRatio.png)  
Sadly there is not a elegant simple solution to this problem that captures all character set aspect ratios. The best I can do is get close to most terminal window character aspect ratios, which is 1:2.

However, I could prioritize the default Windows terminal.. 

The plan is to while resizing the image to divide the height by 2 if not specified or multiply the width by 2 if not not specified. 

## Real test input and output
![test input](./DocImages/lion_input.png)
![test output](./DocImages/lion_output.png)