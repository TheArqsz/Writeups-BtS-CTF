# requirements

python 3.x

```
pip3 install -r requirements.txt
```
or
```
pip install -r requirements.txt
```

# Description
All you have to do is to convert pack of files (10 404 of them which is 102 squared [102^2 = 10404] ) to an image.
Image is in square form and it is QR Code. But instead of '0' and '1' as black and white pixels we have... '0' and '1' in form of pictures. All have to be done is to make image classificator (using neural networks and MNIST dataset), classify each one image to be 0 or 1 and then write 0,1 as black and white pixels into image file.

The exact code is in ```readflag.py```
Data generator is in ```makeflag.py```

flag: ```bts-ctf{SKYNET_WILL__TAKE_CONTROL_OVER_THE_WORLD__SOON}```

#Author
Żarek Mytko