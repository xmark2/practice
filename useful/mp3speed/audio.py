from pydub import AudioSegment
from pydub import effects

import sys
sys.path.append('/path/to/ffmpeg')

root = r'original/abc.mp3'
velocidad_X = 1.5 # No puede estar por debajo de 1.0

sound = AudioSegment.from_mp3(root)
so = sound.speedup(velocidad_X, 150, 25)
so.export(root[:-4] + '_Out.mp3', format = 'mp3')