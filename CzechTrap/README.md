Title:<br>
<b>Czech Trap</b><br>
Description:<br>
<b>The mole is digging deep depp inside his picture, straight to the bottom of his binary world.</b>

In this challenge you are given an image. There is really nothing strange about it...unless you use `binwalk chall.jpg`<br>
In the output you can see `Zip archive data`. Just use `dd if=chall.jpg of=solve bs=1 skip=57056` and unzip created file. What you get is an image of flag.  
