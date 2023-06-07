# 压缩文件
from pydub import AudioSegment
sound = AudioSegment.from_wav("/root/wen/13.wav")
 
 
# 压缩帧率
sound = sound.set_frame_rate(16000)
 
'''
# 长度太长了可能会塞爆，每次取十分之一
musicLen = len(sound) 
unitLen = musicLen / 10
 
for i in range(10):
    _sound = sound[unitLen*i:unitLen*(i+1)]
    _sound.export("/root/wen/13-sub%s.wav" % i, format="wav")
'''
