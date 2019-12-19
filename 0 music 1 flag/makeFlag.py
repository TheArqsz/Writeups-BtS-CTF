from itertools import chain
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq
import binascii

#Można utrudniać np. dać speed, który uniemożliwi odsłuchanie,
#wyciszyć wszystkie nuty (żeby nic nie było słychać przy odtwarzaniu)
#itd


#prędkość odtwarzania pliku
SPEED = 900

#Nie zmieniać, bo wtedy zmienią się litery w pliku do odkodowania
#TODO Żeby nie trzeba było zmieniać
SHIFT1 = 3
SHIFT2 = 12
SHIFT3 = 43

#linijki tekstu

#TODO
#Można dodać więcej jeśli chcecie xD

LINE1 = 'aaaahdjnfrdrdsngpemfmsdvveofmgkrufbwosainvgsfluhmcaaaxdxdaa'
LINE2 = 'BtS-CTF{WHY_ARE_YOU_WASTING_TIME_LISTENING_TO_THIS_SHIT_XD}'
LINE3 = 'sdssainvgsfluhmcaaaaachjhdjnfhehedupahehemsdvveofmgkrufbwxd'

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


seqLine1 = text_to_bits(LINE1)
seqLine2 = text_to_bits(LINE2)
seqLine3 = text_to_bits(LINE3)

seq1 = list(seqLine1)
seq2 = list(seqLine2)
seq3 = list(seqLine3)

for i in range(len(seq1)):
    seq1[i] = int(seq1[i])
    seq2[i] = int(seq2[i])
    seq3[i] = int(seq3[i])

for i in range(len(seq1)):
    seq1[i] += SHIFT1
    seq2[i] += SHIFT2
    seq3[i] += SHIFT3


finalSequence = []


for i in range(len(seq1)):
    finalSequence.append(seq1[i])
    finalSequence.append(seq2[i])
    finalSequence.append(seq3[i])

midi = Midi(tempo=SPEED)

midi.seq_notes(NoteSeq([Note(value=x, octave=4, dur=1/16, volume=127) for x in finalSequence]))
midi.write("file.mid")
