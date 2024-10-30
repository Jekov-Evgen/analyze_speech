import speech_recognition as sr
from pydub import AudioSegment

def convert_m4a_to_wav(path):
    original_sound = path
    wav_copy = 'output.wav'
    
    sound = AudioSegment.from_file(original_sound, format='mp4')
    sound.export(wav_copy, format='wav')
    
    return wav_copy

def taking_out(path):
    copy_read = convert_m4a_to_wav(path)
    read = sr.Recognizer()
    result = ''
    
    with sr.AudioFile(copy_read) as read_audio:
        data = read.record(read_audio)
        result += read.recognize_google(data)
        
    return result