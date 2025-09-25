# High-Bandwidth Proxies for Video Download
[![Oxylabs promo code](/assets/High-Bandwidth-Proxies-V2.png)](https://oxylabs.io/products/high-bandwidth-proxies?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=high-bandwidth-proxies-github&transaction_id=102c8d36f7f0d0e5797b8f26152160)

[![](https://dcbadge.limes.pink/api/server/Pds3gBmKMH?style=for-the-badge&theme=discord)](https://discord.gg/Pds3gBmKMH) [![YouTube](https://img.shields.io/badge/YouTube-Oxylabs-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@oxylabs)

[High-Bandwidth Proxies](https://oxylabs.io/products/high-bandwidth-proxies) are optimized servers designed for scraping **video and audio data at scale**. They provide the speed and stability needed to download multimedia content from popular platforms without interruptions,  timeouts, or slow speeds. Ideal for AI training data collection, media archiving, content analysis, or other large-scale data projects.

## 💡 Key features and benefits

### ⚡ Features

- **High performance:** 200+ Gbps bandwidth with traffic load balancing across multiple servers
- **Diverse IP network:** Millions of IPs from various subnets with rotation and cooldown mechanisms
- **High throughput and success:** Optimized IP pool management with automatic error detection
- **Easy integration:** Works with `yt-dlp` and other popular open-source libraries


### ✅ Benefits

- **High success rates at scale:** Distribute requests accross multiple proxies to overcome anti-bot systems
- **Stable connections:** Avoid blocks, timeouts, and failed downloads during long sessions
- **Handle millions of requests:** Process massive video datasets efficiently without bottlenecks
- **Competitive pricing:** Cost-effective for high-volume operations


## 🚀 Integration examples

After acquiring High-Bandwidth Proxies, you'll get the following proxy configuration details:
- A dedicated **proxy endpoint**
- Proxy **username** and **password**
- Proxy **port number** (default is `60000`)

### 🧪 Testing your connection
---
You can test your proxy connection by appending `-test` to your username.

```python
# pip install requests
import random
import requests


username = 'PROXY_USERNAME'
password = 'PROXY_PASSWORD'
proxy = 'proxy-endpoint:60000'

if not username.endswith('-test'):
    username += '-test'

proxies = {
    'http': f'http://{username}:{password}@{proxy}',
    'https': f'http://{username}:{password}@{proxy}'
}

response = requests.get(
    'https://ip.oxylabs.io/location',
    proxies=proxies
)
print(response.json())
```

### 🎬 Integrating with yt_dlp
---
Make sure to **generate a unique session ID** for each request to get the best performance, as shown below. This configuration ensures that each download request is made with a new IP address.

> [!NOTE]
> Find more code samples in our [documentation](https://developers.oxylabs.io/video-data/high-bandwidth-proxies).

```python
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
```

## ☎️ Contacts

Have questions or need assistance? Don't hesitate to get in touch with us:

- 📩 Email: hello@oxylabs.io
- 💬 [Live chat support](https://oxylabs.drift.click/oxybot)
