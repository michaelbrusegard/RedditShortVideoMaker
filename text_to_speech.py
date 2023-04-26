import os
from google.cloud import texttospeech

def text_to_speech(text_list, tts_service_account_key_path, voice_name='en-GB-Wavenet-B'):
    language_code='en-GB'

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = tts_service_account_key_path

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the voice
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )

    # Set the audio encoding
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=1.1,
        pitch=0.0
    )

    # Create a list to store the file paths
    file_names = []

    print('Generating speech files...')
    # Iterate through each text in the list and generate an mp3 file
    for i, text in enumerate(text_list):
        # Set the input text
        synthesis_input = texttospeech.SynthesisInput(text=text)

        # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

        # Set the file name and path
        file_name = f'tts_{i}.mp3'
        file_path = os.path.join(os.getcwd(), 'assets', file_name)

        # Write the binary content to an mp3 file
        with open(file_path, 'wb') as out:
            out.write(response.audio_content)

        # Add the file path to the list
        file_names.append(file_name)

    return file_names