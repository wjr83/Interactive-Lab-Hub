#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say " Welcome to the 20 Questions game!"
say " I will think of a household appliance, and you'll try to guess it."
say " You can ask yes/no questions to guess."
say " Press Ctrl+C to stop the game."