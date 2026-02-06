# ChronoLog: Context-Aware Memory Augmentation

A privacy-first personal knowledge assistant that runs entirely on-device. It captures screen context, meeting audio, and browsing history to build a searchable vector database of your digital life. Users can query a local LLM to retrieve specific information, such as 'What file was I editing when I received the email from Sarah?' or 'Summarize the technical constraints discussed in yesterday's standup.' It acts as an external hard drive for your brain, focusing on data sovereignty and total recall.

## Tech Stack

- Rust
- Tauri
- React
- SQLite (Vector Extension)
- OpenAI Whisper (Local)
- Llama 3 (Quantized Local Model)
- FFmpeg

## Features

- Semantic Search: Query past actions using natural language.
- Timeline Scrubber: Visual slider to rewind screen states and activity.
- Meeting Intelligence: Auto-transcribe and summarize audio from system output.
- Privacy Vault: All data stored locally with AES-256 encryption; no cloud upload.
- Context Linking: Correlate active applications with web history and communications.

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd chronolog:-context-aware-memory-augmentation
make install

# Run the application
make run
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
make install && make run
```

## Development

```bash
make install  # Create venv and install dependencies
make run      # Run the application
make test     # Run tests
make clean    # Remove cache files
```

## Testing

```bash
pytest tests/ -v
```
