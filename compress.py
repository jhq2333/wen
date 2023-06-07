import wave
with wave.open(wav_file, 'rb') as fin:
    assert fin.getnchannels() == 1
    assert fin.getsampwidth() == 2
    assert fin.getframerate() == 16000
