from music21 import converter,instrument
import binascii

LINE1 = []
LINE2 = []
LINE3 = []

#Otwarcie pliku w parserze
file = converter.parse('file.mid')

components = []


for element in file.recurse():
    components.append(element)

#Obcięcie informacji odnośnie instrumentów, tempa itd.
#Żeby zostały same nuty
components = components[3:] 
#print(components[3].midi)
#Wyciągnięcie samych nazw nut
for i in range(len(components)):
    components[i] = str(components[i].name)



#Dodawanie do tablic zgodnie z wysokością dźwięku
for note in components:
    if note == 'E-':
        LINE1.append('0')
    elif note == 'E':
        LINE1.append('1')
    elif note == 'C':
        LINE2.append('0')
    elif note == 'C#':
        LINE2.append('1')
    elif note == 'A':
        LINE3.append('0')
    elif note == 'G#':
        LINE3.append('1')

LINE1 = ''.join(LINE1)
LINE2 = ''.join(LINE2)
LINE3 = ''.join(LINE3)


#powrót z bitów na tekst
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

#wyniki
print(text_from_bits(LINE1))
print(text_from_bits(LINE2))
print(text_from_bits(LINE3))


        
