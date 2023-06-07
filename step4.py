import glob
file = glob.glob("/root/wen/13.wav")
ans=eval(decoder.decode_wav(file))
print(ans["nbest"][0]["sentence"])
