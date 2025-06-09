# pip install yt-dlp
import random
import yt_dlp


def download_with_new_ip(url, username, password):
    session_id = random.randint(1, 100000)
    proxy = f'http://{username}-{session_id}:{password}@your-endpoint:60000'

    ydl_opts = {
        'proxy': proxy
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f'Downloading {url} with new IP ({username}-{session_id})...')
            ydl.download([url])
            print(f'Successfully downloaded {url}')
        except Exception as e:
            print(f'Error downloading {url}: {str(e)}')


def main():
    username = 'PROXY_USERNAME'
    password = 'PROXY_PASSWORD'
    
    videos = [
        'https://www.youtube.com/watch?v=6stlCkUDG_s',
        'https://www.youtube.com/watch?v=gsnqXt7d1mU'
    ]
    
    for video in videos:
        download_with_new_ip(video, username, password)


if __name__ == '__main__':
    main()