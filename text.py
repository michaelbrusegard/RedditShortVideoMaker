def get_text(post):
    print('Retrieving text from reddit post...')
    text = []
    text.append(post.title)
    text.extend(post.selftext.split('\n\n'))
    return text