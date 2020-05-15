# ("/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.mp3"

# [START speech_transcribe_async]
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
from pydub import AudioSegment
import subprocess

# def convert_mp3_wav(local_file_path):
#     sound = AudioSegment.from_mp3(local_file_path)
#     return sound.export(local_file_path.strip("mp3") + "wav", format="wav")

# import subprocess

#   subprocess.call(['ffmpeg', '-i', '/input/file.mp3',
#                    '/output/file.wav'])


def sample_long_running_recognize(local_file_path):
    # print("inside our function")
    """
    Transcribe a long audio file using asynchronous speech recognition
    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """
    # convert_mp3_wav(local_file_path)
    client = speech_v1.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"
    enable_word_time_offsets = True


    # Sample rate in Hertz of the audio data sent
    # sample_rate_hertz = 32000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "enable_word_time_offsets": enable_word_time_offsets,
        # "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))
    # [END speech_transcribe_async]

    # Print the start and end time of each word
    for word in alternative.words:
        print(u"Word: {}".format(word.word))
        print(
            u"Start time: {} seconds {} nanos".format(
                word.start_time.seconds, word.start_time.nanos
            )
        )
        print(
            u"End time: {} seconds {} nanos".format(
                word.end_time.seconds, word.end_time.nanos
            )
        )
    # End of timeoff 



# def main():
#     import argparse

#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         "--local_file_path", type=str, default="/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.mp3"
#     )
#     args = parser.parse_args()

#     sample_long_running_recognize(args.local_file_path)


# if __name__ == "__main__":
#     main()

# wav_path = convert_mp3_wav("/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.mp3")
# print(type(wav_path))


############################################################################################################
############################################################################################################
############################################################################################################


src = "/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.mp3"
dst = "/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.wav"
# sample_long_running_recognize("/home/malkaiv/project/Datasets/common-voice/cv-other-train/cv-other-train/sample-120949.mp3")
# subprocess.call(['ffmpeg', '-i', src, dst])
sample_long_running_recognize(dst)