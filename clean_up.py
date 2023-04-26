import os

def delete_assets():
    assets_dir = 'assets'
    print('Deleting assets...')
    for file_name in os.listdir(assets_dir):
        if file_name.endswith('.mp3') or file_name.endswith('.png'):
            file_path = os.path.join(assets_dir, file_name)
            os.remove(file_path)