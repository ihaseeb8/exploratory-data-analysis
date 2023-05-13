import os
from pydub import AudioSegment

# defining a list for emotions
emotions = ['Angry' , 'Happy', "Neutral", 'Sad']

# Make sure the directory exists
if not os.path.exists('./Merged Audios Based On Emotions'):
    os.makedirs('./Merged Audios Based On Emotions')

# iterating through different emotions folders
for emotion in emotions:

    # Initializing a dictionary to hold audio data for each speaker for this emotion
    speakers = {}

    #  iterating through every file in a dir
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

    # Create the directory for this emotion if it doesn't exist
    merged_dir = f'./Merged Audios Based On Emotions/Merged_{emotion}'
    os.makedirs(merged_dir, exist_ok=True)

    # Iterate over the speakers and store their audio for this emotion
    for speaker_id, audio in speakers.items():
        # Export the speaker's audio to a .wav file in the correct directory
        audio.export(f'{merged_dir}/{speaker_id}_{emotion}.wav', format='wav')
