# voice-ai-whisper-demo

Tiny standalone Python demo: transcribe an audio file with OpenAI's open-source Whisper model running locally. Single file, single dependency.

## Why

Voice AI starts with reliable transcription. Whisper runs offline on Apple Silicon, no cloud needed. This is the smallest useful starting point.

## Install

    pip install openai-whisper

(Requires ffmpeg installed on the system.)

## Run

    python transcribe.py path/to/audio.wav

## Output

Prints the transcription to stdout. Writes a `<filename>.txt` next to the input audio.

## Notes

- Uses the `base` model by default (fast, ~140 MB, English-accurate enough for most demos).
- Swap to `small`, `medium`, or `large-v3` in the code for higher accuracy.
- CPU works, Apple Silicon GPU (mps) faster, NVIDIA GPU (cuda) fastest.

## Part of

The Nexus AI stack: https://github.com/tphilips43east-stack/nexus-ai-stack
