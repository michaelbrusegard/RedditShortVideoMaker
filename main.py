import configparser

from background_video import get_background_video
from post import retrieve_post
from text import get_text
from clean_text import clean_strings
from screenshots import take_screenshots
from text_to_speech import text_to_speech
from create_video import edit_video
from clean_up import delete_assets


config = configparser.ConfigParser()
config.read('config.ini')

background_video = get_background_video(config['Preferences']['background_youtube_url'])
post = retrieve_post(config['Preferences']['subreddit'], config['Reddit']['client_id'], config['Reddit']['client_secret'], config['Reddit']['user_agent'])
text = get_text(post)
clean_text = clean_strings(text)
screenshots = take_screenshots(post.url, config['Reddit']['username'], config['Reddit']['password'])
speech_files = text_to_speech(clean_text, config['Google Cloud']['tts_service_account_key_path'], config['Preferences']['tts_voice'])
edited_video = edit_video(background_video, screenshots, speech_files)
delete_assets()

print('Done!')