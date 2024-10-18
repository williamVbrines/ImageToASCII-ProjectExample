# ToASKII a Project Example
*This project is for an example to show what a decent layout of a project could be.*
## Short Description
 A python program and module to convert an image to ASKII.
 
## Mian contributors
William VB

## Project Status
WORK IN PROGRESS
Deadline **18-10-2024 (DD-MM-YYYY)**   

## ToASKII Useage Requirements
This project uses Python and thus you need to have it installed on your computer, to use this.
The project also uses some external libraries that may need to be installed. See bellow.
- [Python Installation Guide](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Pilliow](https://python-pillow.org/) for importing images and some processing. [Pillow Intallation Guide](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

## Useage

### AS a Module 
```python
from Pillow import image
import To_ASKII
file_path = "path_to_file"
my_image = new image.open(file_path)
text = To_ASKII.convert_image_to_string(my_image, 180, 180)
```
### AS Program
```python 
import ToASKII PATH_TO_IMAGE MAX_WITH_IN_CHARACTERS MAX_HEIGHT_CHARACTERS EPORT_PATH
```

## TECHNICAL DOC
Goes in depth in to aspects of the project. This is due to the README is more of a landing page for users not developers of the project.  
[LINK TO TECHNICAL DOC](./TECHNICALDOC.md)
