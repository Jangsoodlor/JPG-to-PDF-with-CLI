# Disclaimer
** This project have a mild case of being discontinued (at least for the forseeable future). As it's currently inhabited by a lot of bugs. I strongly advice you to use version 3.3.0 because 3.4.0 is just a mess as far as I can recall.

Does your teacher requires you to submit your assignment in PDF but you have to work with pen and paper? Well, this tool is made for YOU!

This is a simple Python script to convert images to PDF and combine them into one single PDF file. Based on [praneetk2704's JPG-to-PDF](https://github.com/praneetk2704/JPG-to-PDF)
<br /><br />
![screenshot_1](/pic/demonstration-new.png)

## OK Cool, But how do I use it?

First, you download the executable file in the release tab on the right to your computer. Open it and then follow the instructions on the screen.

### Demonstrations

![demo](/pic/how1.png)
![demo](/pic/how2.png)
![demo](/pic/how3.png)
![demo](/pic/how4.png)

## Building

You're required to install 2 dependencies from pip. Which are:

```bash
fpdf
pillow -- for Pillow-ver
imageio -- for iio-ver
```

WHY? Read below

## Known Problem(s)

Some pictures' orientation may be incorrect. This is because of the EXIF data associated with the pictures is incorrect. I'm currently trying to fix it by experimenting with different photo-processing libraries. But documentations regarding this are A HUGE F\*\*\*ING MESS.
