# autoevalimg

This tool is designed to save time evaluating images in a reference image library with the ARCore image evaluator. This will automate the process onto a folder of images and will output the results to a text file. More information can be found [here](https://developers.google.com/ar/develop/java/augmented-images/arcoreimg).

## Installation

Install the package with pip
```
pip install autoevalimg
```

Open a python interpreter in the terminal
```
python
```

Import the package
```
from autoevalimg import AutoEvalImgManager
```

Reference the folder of images to evaluate
```
mng = AutoEvalImgManager("path/to/images/folder")
```

Run the evaluator
```
mng.get_results()
```

Open results.txt for all of the scores of the images