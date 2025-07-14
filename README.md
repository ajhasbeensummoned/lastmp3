# LastMP3 - Last.fm Music Downloader

A user-friendly Python tool that downloads your most recent Last.fm tracks as high-quality MP3s with automatic metadata tagging.

## Features

- **Download Recent Tracks**: Automatically fetches your most recent Last.fm track
- **Full Album Support**: Option to download entire albums
- **Auto-Tagging**: Adds metadata (title, artist, album, artwork) to downloaded MP3s

## Quick Start

### Prerequisites
- Python 3.7+
- Last.fm account
- You can find the other requirements in requirements.txt

### Installation through PyPi
1. **Run the Pip Install Command**

   On Windows:
   ```bash
   py -m pip install lastmp3
   ```
   On most Unix-like platforms:
   ```bash
   pip3 install lastmp3
      ```
   On other platforms, you may try:
   ```bash
   pip install lastmp3
   ```

### Installation if you don't wanna do it through PyPi

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lastfm_mp3_with_tags.git
   cd lastfm_mp3_with_tags
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Last.fm API key**
   - Visit [Last.fm API](https://www.last.fm/api/account/create)
   - Create a free account if you don't have one
   - Generate an API key (you'll need this for first run)

### Usage (If installed through PyPI)

```bash
lastmp3 [username]
```

**Examples:**
```bash
lastmp3 johndoe          # Download recent track for user with the username 'johndoe'
lastmp3 --help or -h     # Show help information
lastmp3 --version or -v  # Show version information
```

### Usage (If running manually)

```bash
python -m lastmp3 [username]
```

**Examples:**
```bash
python -m lastmp3 johndoe          # Download recent track for user with the username 'johndoe'
python -m lastmp3 --help or -h     # Show help information
python -m lastmp3 --version or -v  # Show version information
```

### First Time Setup
1. Run the command with a Last.fm username
2. Enter your API key when prompted (one-time setup)
3. Choose to download track (t) or album (a)
4. The files will be downloaded to your current working directory

## File Structure

```
Your-Directory/
├── .github/
│   └── workflows/
│       └── lastmp3.yaml    # GitHub Actions workflow
├── lastmp3/
│   ├── __init__.py
│   ├── __main__.py         # Main application
│   ├── api.py              # Last.fm API integration
│   └── metadata.py         # MP3 tagging functionality
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project configuration
├── README.md               # Documentation
└── License.md              # MIT License
```

## Configuration

The tool automatically creates a `config.json` file in `LastMP3 Downloads/` containing:
- Your Last.fm API key
- FFmpeg executable paths
- Other settings

## Dependencies

- **mutagen**: MP3 metadata manipulation
- **requests**: HTTP requests for Last.fm API
- **static_ffmpeg**: Audio processing
- **yt-dlp**: YouTube audio downloading

## License

This project is licensed under the MIT License.

## Legal Notice

This tool is for personal use only.

## Troubleshooting

### Common Issues

**"yt-dlp not found"**
```bash
pip install yt-dlp
```

**"Invalid API key"**
- Check your API key at [Last.fm API](https://www.last.fm/api/account/create)
- Make sure you're using the API key, not your password

**"No recent tracks found"**
- Ensure the username is correct
- Check if the user's profile is public
- Verify the user has scrobbled at least one track

### Getting Help

If you encounter issues:
1. Check the error message carefully
2. Verify your internet connection
3. Ensure all dependencies are installed
4. Check if your Last.fm username and API key are correct

Contributions are always welcome!!
