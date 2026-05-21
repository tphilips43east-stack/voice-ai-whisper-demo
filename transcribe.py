"""Transcribe an audio file with OpenAI's open-source Whisper model. Minimal demo."""
import sys
from pathlib import Path
import whisper


def transcribe(audio_path: str, model_name: str = "base") -> str:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result["text"].strip()


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file>")
        sys.exit(1)

    audio = sys.argv[1]
    if not Path(audio).exists():
        print(f"File not found: {audio}")
        sys.exit(1)

    text = transcribe(audio)
    print(text)

    out = Path(audio).with_suffix(".txt")
    out.write_text(text, encoding="utf-8")
    print(f"\nSaved transcript to: {out}")


if __name__ == "__main__":
    main()
