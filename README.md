# MelodyWriter

Writes functional melody in [Lilypond Format](http://lilypond.org/)

## Dependencies

Linux ubuntu
```
sudo apt install python3 lilypond
```

Windows
```
???
install python and lilypond somehow, i guess
```

## Usage

create 100 notes of Cmaj melody
```
python3 MelodyWriter.py
```

create 300 notes of Dmaj melody and export to pdf image

```
python3 MelodyWriter.py -l 300 -s "cis' d' e' fis' g' a' b'"
```

create 500 notes of Amin melody and export to png image
```
python3 MelodyWriter.py -l 500 -s "g' a' b' c'' d'' e'' f''" --export
``` 

`'` - means octave number

## Sharps and flats
for sharp use "ais"
for flat use "aes" 