# Video to Text Transcription

This project provides a tool for transcribing audio and video content using the OpenAI Whisper model.

## Setup

### 1. Install Dependencies

#### Install Whisper

```bash
pip install -U openai-whisper
```

#### Install FFmpeg

`ffmpeg` is a powerful tool to handle multimedia data. It's required for extracting audio from video.

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

#### Install Rust (if needed)

In some cases, you might need Rust to be installed, especially if some dependencies don't provide pre-built binaries.

Follow the [Getting started page](https://www.rust-lang.org/learn/get-started) to install Rust. You might need to set up your `PATH`:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

If you encounter the error `No module named 'setuptools_rust'`, install `setuptools_rust`:

```bash
pip install setuptools-rust
```

#### Install MoviePy

MoviePy is a Python module for video editing, which can also be used for opening and modifying video files.

```bash
pip install moviepy
```

### 2. Clone the Repository

```bash
git clone [REPOSITORY LINK]
cd [REPOSITORY NAME]
```

## Usage

### Display Help
```bash
python v2t.py --help
```

### Transcribe Video
```bash
python v2t.py --task video --video path_to_video_file.mp4 --output_dir desired_output_directory
```

### Transcribe Audio
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --output_dir desired_output_directory
```

### Specify Model
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --model model_name
```

### Output Format
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --output_format txt
```

### Language Specification
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --language es
```

### Translate to English
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --translate
```

### Silence Output
```bash
python v2t.py --task audio --audio path_to_audio_file.wav --verbose false
```

### Combine arguments as needed. For example, to transcribe a Spanish video, save the results as a txt file, and translate it to English:
```bash
python v2t.py --task video --video path_to_video_file.mp4 --language es --output_format txt --translate
```