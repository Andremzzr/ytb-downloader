# YouTube Downloader

## Description
This application allows users to download YouTube videos as MP3 files. It features a graphical user interface (GUI) built with Tkinter and utilizes `yt_dlp` for downloading and converting videos.

## Features
- Download YouTube videos as high-quality MP3 files.
- Choose a destination folder for downloads.
- Simple and intuitive graphical user interface.

## Requirements
Ensure you have the following dependencies installed:

- Python 3.x
- `yt-dlp`
- `tkinter`
- `ffmpeg` (for audio conversion)

You can install the necessary Python packages using:
```sh
pip install yt-dlp
```

### Installing FFmpeg
FFmpeg is required for extracting and converting audio. Install it using:

**Windows:** Download from [ffmpeg.org](https://ffmpeg.org/) and add it to your system path.

**Mac (using Homebrew):**
```sh
brew install ffmpeg
```

**Linux:**
```sh
sudo apt install ffmpeg
```

## Usage
Run the application with:
```sh
python main.py
```

### Main Components

#### `Downloader.py`
Handles downloading and converting YouTube videos to MP3.
- **Method:** `download_video_as_mp3(url, download_path=None)`
- Uses `yt-dlp` to extract and download audio.
- Saves the file in the specified directory.

#### `Interface.py`
Manages the graphical interface.
- Provides input fields for YouTube links.
- Allows users to select a download folder.
- Calls `Downloader.py` to start downloads.

## Project Structure
```
📂 YoutubeDownloader
 ├── 📂 service
 │   ├── Downloader.py
 │   ├── Interface.py
 ├── main.py
 ├── README.md
```

## Notes
- Ensure `ffmpeg` is properly installed and accessible in the system path.
- The application does **not** support video downloads, only audio (MP3 format).
- If a file with the same name exists, it will be deleted before downloading.

## License
This project is licensed under the MIT License.
