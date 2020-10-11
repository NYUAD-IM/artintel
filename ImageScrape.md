# Image scraping

## Scraping Google Images (2020-10)

Install [google-images-download](https://github.com/hardikvasa/google-images-download) from the source repository

````bash
$ git clone git@github.com:Joeclinton1/google-images-download.git
$ cd google-images-download
$ python setup.py install
````


To download 10 images of "cats"
````bash
$ googleimagesdownload -k cats -l 10
$ ls downloads/cats/
1.5544.jpg
10.c5w6dhx0tciv8to2npiwkaztwjezxr6gycysxc0hklj8g3lpp-eeemliwab28gf37puekpvg=w640-h400-e365-rj-sc0x00ffffff.jpg
2.gettyimages-1199242002-1-scaled.jpg
3.ecab8c7af42a439d9043b0ade6e1f05b_18.jpeg
4.screen_shot_2019_07_18_at_4.16.52_pm.png.jpg
5.1*qyaoepuloa_kvehheiyska.jpeg
6.thumbs_b_c_88bedbc66bb57f0e884555e8250ae5f9.jpg
7.thinking-of-getting-a-cat.png
8.file-20200520-152302-97x8pw.jpg
9.science_cats-84873657.jpg
````

Downloading more than 100 images requires installing Chromedriver to automatically scroll
through the Google image search results.

Download [Chromedriver](https://chromedriver.chromium.org/)

You should have the file `chromedriver`. Pass the path to this file when running the command.

On Mac you need to get `chromedriver` out of quarantine before running it the first time.
````bash
$ xattr -d com.apple.quarantine chromedriver
````


Get 200 images for "cats".
````bash
$ googleimagesdownload -k cats -l 200 --chromedriver ~/Downloads/chromedriver
````