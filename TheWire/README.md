Title:<br>
<b>The Wire</b><br>
Description:<br>
<b>Most of our tasks must go through wire, but this one...oh this one loves the Wire...</b>

In this task you are given a pcapng file. As you may know, this is the type of file created with wireshark/tshark.
When you open it with Wireshark you may see data coming out and in from a device. These are logs from typing a buttons on keyboard. Great description of this kind of challenges is [here](https://medium.com/@ali.bawazeeer/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4). 

What you have to to is to process this file and retrieve keystrokes. Simple decoder created [here](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser).

With this knowledge you get a lot of dots and dashes. In the description you are said that flag is not case sensitive.

With simple morse decoder (like [this](https://morsecode.world/international/translator.html) e.g.) you get `BTS-CTF#FLAG-0N-TH3-W1RE-AMA21NG)`. As you may or may not know - Morse does not contain '{' and '}'.
If you fix it you get `BTS-CTF{FLAG-0N-TH3-W1RE-AMA21NG}`
