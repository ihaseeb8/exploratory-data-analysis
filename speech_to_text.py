import os
import openai

openai.api_key = "Put your api key here"

# Define the list of emotion folders
emotion_folders = ['Merged_Angry', 'Merged_Happy', 'Merged_Neutral', 'Merged_Sad']

# Make sure the directory exists
if not os.path.exists('./Speech To Text'):
    os.makedirs('./Speech To Text')

# Iterate over each emotion folder
for emotion_folder in emotion_folders:
    # Define the corresponding text folder
    text_folder = emotion_folder + "_Text"
    
    # Create the text folder if it doesn't exist
    if not os.path.exists(f'Speech To Text/{text_folder}'):
        os.makedirs(f'Speech To Text/{text_folder}')

    # Iterate over each audio file in the current emotion folder
    for audio_file_name in os.listdir(f'Merged Audios Based On Emotions/{emotion_folder}'):
        # Open the audio file
        with open(os.path.join(f'Merged Audios Based On Emotions/{emotion_folder}', audio_file_name), "rb") as audio_file:
            # Transcribe the audio file
            transcript = openai.Audio.transcribe("whisper-1", audio_file, language='ur')

        # Extract the base name of the audio file (without extension)
        base_name = os.path.splitext(audio_file_name)[0]

        # Define the transcript file name
        transcript_file_name = os.path.join(f'Speech To Text/{text_folder}', base_name + ".txt")

        # Open a new text file to save the transcript
        with open(transcript_file_name, "w", encoding='utf-8') as text_file:
            # Write the transcript to the text file
            text_file.write(transcript.text)
