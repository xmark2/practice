from gtts import gTTS
import os
tts = gTTS(text='idő előtt', lang='hu')
tts.save("ie.mp3")
os.system("mpg321 regelt.mp3")
