from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, error
from mutagen.mp3 import MP3
import requests


def tag_mp3(file_path, title, artist, album, album_art_url):
    try:

        audio = ID3(file_path)


        audio.add(TIT2(encoding=3, text=title))   # title
        audio.add(TPE1(encoding=3, text=artist))  # artist
        audio.add(TALB(encoding=3, text=album))   # album


        if album_art_url:
            response = requests.get(album_art_url)
            if response.status_code == 200:
                img_data = response.content
                audio.add(
                    APIC(
                        encoding=3,
                        mime='image/jpeg',  # or image/png if needed
                        type=3,  #front cover
                        desc='Cover',
                        data=img_data
                    )
                )
                print("Album art embedded")
            else:
                print("Failed to download album art")

        audio.save()
        print(f"Tags written to {file_path}")

    except error as e:
        print(f"Tagging error for {file_path}: {e}")
