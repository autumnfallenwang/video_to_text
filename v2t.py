import os
import moviepy.editor as mp
import argparse
from whisper import load_model, transcribe, available_models
from whisper.utils import get_writer
from whisper.tokenizer import LANGUAGES, TO_LANGUAGE_CODE


def extract_audio_from_video(video_path, audio_path='temp_audio.wav'):
    """Extract audio from video."""
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')
    return audio_path


def transcribe_audio_with_whisper(
    audio_file: str, 
    model: str, 
    output_dir: str, 
    output_format: str, 
    language: str, 
    task: str, 
    verbose: bool):
    """
    Transcribes an audio file using the Whisper model.
    
    Parameters:
    - audio_file: Path to the audio file to transcribe.
    - model: Name of the Whisper model to use.
    - output_dir: Directory to save the outputs.
    - output_format: Format of the output file.
    - language: Language spoken in the audio.
    - task: Task to perform ("transcribe" or "translate").
    - verbose: Whether to print the transcription result.
    
    Returns:
    - Path to the saved transcription file.
    """

    # Load the Whisper model
    model_instance = load_model(model)
    
    # Perform transcription
    transcription_result = transcribe(
        model_instance,
        audio_file,
        language=language,
        task=task,
        verbose=verbose
    )
    
    # Write the transcription to the specified format and save in the designated output directory
    writer = get_writer(output_format, output_dir)
    writer(transcription_result, audio_file)


def main():
    parser = argparse.ArgumentParser(description="Transcribe audio or video using Whisper.")

    # Define arguments
    parser.add_argument("--task", choices=["video", "audio"], default="video",
                        help="Main task to perform, either 'video' or 'audio'. Default is 'video'.")
    parser.add_argument("--video", type=str, default=None,
                        help="Path to the video file if the task is 'video'.")
    parser.add_argument("--audio", type=str, default=None,
                        help="Path to the audio file if the task is 'audio'.")
    parser.add_argument("--model", type=str, default="small", choices=available_models(),
                        help="Name of the Whisper model to use. Default is 'small'.")
    parser.add_argument("--output_dir", type=str, default="./output",
                        help="Directory to save the outputs. Default is 'output'.")
    parser.add_argument("--output_format", type=str, default="all", choices=["txt", "vtt", "srt", "tsv", "json", "all"],
                        help="Format of the output file. Default is 'all'.")
    parser.add_argument("--language", type=str, default="en", choices=sorted(LANGUAGES.keys()) + sorted([k.title() for k in TO_LANGUAGE_CODE.keys()]),
                        help="Language spoken in the audio. Default is 'en'.")
    parser.add_argument("--translate", action="store_true", default=False,
                        help="Whether to perform translation into English. Default is False.")
    parser.add_argument("--verbose", action="store_true", default=True,
                        help="Whether to print the transcription result. Default is True.")

    args = parser.parse_args()

    # Validate inputs
    if args.task == "video" and not args.video:
        parser.error("--video is required when task is 'video'.")
    if args.task == "audio" and not args.audio:
        parser.error("--audio is required when task is 'audio'.")

    # Make sure the output directory exists
    os.makedirs(args.output_dir, exist_ok=True)

    # Extract audio from video if needed
    if args.task == "video":
        audio_path = extract_audio_from_video(args.video, os.path.join(args.output_dir, "temp_audio.wav"))
    else:
        audio_path = args.audio

    task = "translate" if args.translate else "transcribe"
    # Perform transcription
    transcribe_audio_with_whisper(
        audio_file=audio_path,
        model=args.model,
        output_dir=args.output_dir,
        output_format=args.output_format,
        language=args.language,
        task=task,
        verbose=args.verbose
    )

if __name__ == "__main__":
    main()


