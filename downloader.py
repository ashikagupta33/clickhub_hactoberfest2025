from pytube import YouTube

def download_video(url, choice):
    try:
        yt = YouTube(url)
        print(f"\nTitle: {yt.title}")
        print(f"Channel: {yt.author}")
        print(f"Length: {yt.length // 60} min")

        if choice == "1":
            stream = yt.streams.get_highest_resolution()
            print("Downloading video...")
        elif choice == "2":
            stream = yt.streams.filter(only_audio=True).first()
            print(" Downloading audio...")
        else:
            print("Invalid choice.")
            return

        stream.download()
        print("Download complete!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("YouTube Downloader")
    url = input("Enter YouTube URL: ").strip()
    print("1. Download Video (MP4)\n2. Download Audio (MP3)")
    choice = input("Choose option (1/2): ").strip()
    download_video(url, choice)
