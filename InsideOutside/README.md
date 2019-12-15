Title:<br>
<b>Inside Outside</b><br>
Description:<br>
<b>I just got strange file and I am not sure what to do with it. I need to Zip my hacking jacket on and see what it is.</b>

In this challenge you are given a file which happens to be Zip archive. When you unzip it you get a PDF file.
You need to open it with text editor to see its content. Go to `EmbeddedFile` object part you can see a hex dump of something. What you have to do is:
- `echo <hex_dump> > text_dump`
- `xxd -r -p text_dump > binary_dump`

What you get is another PDF file. You have to know that PDF filetype considers `%` as a comment. When you exclude all comments you are left with an URL transformed to hex. Just go to decoded website and copy the flag.
