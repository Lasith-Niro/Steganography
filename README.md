# Steganography



## Prerequisite
* Linux / Windows OS
* PIL (Python Image Library)
* Python 2.7
* PIP


## Run project

### Hide text in image
```
$ python hideText.py -e <image name>
```

### Get text from image
```
$ python hideText.py -d <image name>
```

### Hide image in image
```
$ python hideImage.py hide <image1> <image2>
```
hidden.png file created.It contains both images.

### Unhide image
```
$ python hideImage.py show hidden.png
```


