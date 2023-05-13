import os
from pydub import AudioSegment

# defining a list for emotions
emotions = ['Angry' , 'Happy', "Neutral", 'Sad']

# Initializing a dictionary to hold audio data for each speaker
speakers = {}

# iterating through different emotions folders
for emotion in emotions:
    # print(f'\n {emotion} \n')
    
    #   iterating through every file in a dir
    for filename in os.listdir(f'./Urdu Dataset/{emotion}'):
        
        # Extract the speaker id and gender from the filename
        speaker_id = filename.split('_')[0]  # Splits the filename on underscore and takes the first part (e.g., 'SM25')

        # Check if this is the first file for this speaker
        if speaker_id not in speakers:
            # Initialize an empty audio segment for this speaker
            speakers[speaker_id] = AudioSegment.empty()

        # Get the path to the audio file
        file_path = f'./Urdu Dataset/{emotion}/{filename}'

        # Load the audio file
        audio = AudioSegment.from_wav(file_path)

        # Append the audio to this speaker's audio segment
        speakers[speaker_id] += audio

# Make sure the Merged directory exists
if not os.path.exists('./Merged Audios'):
    os.makedirs('./Merged Audios')

# Iterate over the speakers
for speaker_id, audio in speakers.items():
    # Export the speaker's audio to a .wav file
    audio.export(f'./Merged Audios/{speaker_id}_Merged.wav', format='wav')