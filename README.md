# youtube-downloader
YouTube Downloader: A Python tool using yt-dlp to download YouTube videos, playlists, and channels. It supports single video downloads, playlist retrievals, and channel content extraction. Simple CLI interface. Requires Python 3.6+ and yt-dlp. See README for setup and usage.

# YouTube Downloader

A Python-based tool to download YouTube videos, playlists, and channels using `yt-dlp`. This script allows you to easily save content from YouTube for offline use.

## Features

- **Download Single Videos**: Fetch individual videos by providing their URL.
- **Download Playlists**: Retrieve all videos from a specified YouTube playlist.
- **Download Channels**: Download all videos from a YouTube channel.

## Requirements

- **Python**: Version 3.6 or higher
- **yt-dlp**: Python module for downloading videos from YouTube

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Pichikachandu/youtube-downloader.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd youtube-downloader
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Follow the prompts** to enter the YouTube link (video, playlist, or channel) and specify the output directory where the files will be saved.

## Configuration

The script allows you to specify:

- **`outtmpl`**: Template for output file names. Default is set to the video title and extension.
- **`format`**: Video quality. Default is set to the best available quality.
- **`noplaylist`**: Boolean to specify whether to include playlists in the download.

## Example

To download a single video:

```bash
python main.py
```
Enter the video URL when prompted and specify the output directory.

To download an entire playlist or channel, simply provide the URL of the playlist or channel when prompted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests to improve this project. Contributions are welcome!

## Contact

For any questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).

```

### Additional Files

1. **`requirements.txt`**: This file should list `yt-dlp` as a dependency.
   
   ```text
   yt-dlp
   ```

2. **`LICENSE`**: If you’re using an open-source license like MIT, include a `LICENSE` file with the following content:

   ```text
   MIT License

   Copyright (c) [year] [your-name]

   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.
   ```
