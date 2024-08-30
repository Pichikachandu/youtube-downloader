import yt_dlp
import os

def download_video(url, output_path):
    """Download a single video from YouTube using yt-dlp."""
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': True,  # Ensure only the single video is downloaded
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded video from URL: {url}")
    except Exception as e:
        print(f"An error occurred while downloading video: {e}")

def download_playlist(url, output_path):
    """Download all videos from a YouTube playlist using yt-dlp."""
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': False,  # Ensure playlist videos are downloaded
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded playlist from URL: {url}")
    except Exception as e:
        print(f"An error occurred while downloading playlist: {e}")

def download_channel(url, output_path):
    """Download all videos from a YouTube channel using yt-dlp."""
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'best',
        'noplaylist': False,  # Ensure all channel videos are downloaded
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded channel from URL: {url}")
    except Exception as e:
        print(f"An error occurred while downloading channel videos: {e}")

def main():
    link = input("Enter the YouTube link (channel, playlist, or video): ").strip()
    output_path = input("Enter the output directory path: ").strip()
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    if 'playlist' in link:
        download_playlist(link, output_path)
    elif 'channel' in link:
        download_channel(link, output_path)
    else:
        download_video(link, output_path)

if __name__ == "__main__":
    main()
