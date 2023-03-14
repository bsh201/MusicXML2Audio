# MusicXML to audio
Can change musicxml in audio *(mp3, wav...)*
It can be use in **LINUX**

## MusicXML
MusicXML is a digital sheet music interchange and distribution format. The goal is to create a universal format for common Western music notation, similar to the role that the MP3 format serves for recorded music. The musical information is designed to be usable by notation programs, sequencers and other performance programs, music education programs, and music databases.
[https://www.w3.org/2021/06/musicxml40/tutorial/introduction/]
<div></div>

## File Structure
        MusicXML to Audio
            |_ converter
                |_ midi2wav.py
                |_ MXL2midi.py
                |_ wav2sound.py
            |_ data
                |_ .fluidsynth
                |_ .mxl
                |_ output
            |_ install_packages.sh
            |_ main.py
            |_ midi2audio.py
            |_ README.md
            |_ requirements.txt


## How to use
    #clone git repo
    git clone https://github.com/byj9402/MusicXML2Audio.git

<div></div>

    #install packages for use converter
    sh install_packages.sh
    pip install -r requirements.txt

<div></div>

    #put musicxml in .\data\.xml

<div></div>

    #run converter
    python main.py

<div></div>
