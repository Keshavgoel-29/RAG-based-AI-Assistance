# RAG Based AI Teaching Assistance

Major Project Phase-I — B.Tech CSE, Graphic Era Hill University.

A Retrieval-Augmented Generation assistant that answers questions from a
library of lecture videos and returns the exact video and timestamp where
the topic is explained.

## Pipeline
- `process_video.py` — extracts audio from videos with ffmpeg
- `stt.py` — transcribes audio with timestamps
- `create_chunks.py` — builds timestamped chunks for embedding

## Note
Video and audio files are excluded from this repository via `.gitignore`.
