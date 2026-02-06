"""
ChronoLog Entry Point.

Handles command-line arguments to start the capture service or query the local knowledge base.
"""

import argparse
import sys
import time
from src.core.app import ChronoLogApp

def main() -> int:
    parser = argparse.ArgumentParser(
        description="ChronoLog: Context-Aware Memory Augmentation"
    )
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0-mvp")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: start
    start_parser = subparsers.add_parser("start", help="Start the background capture service")
    start_parser.add_argument("--interval", type=int, default=5, help="Capture interval in seconds")

    # Command: query
    query_parser = subparsers.add_parser("query", help="Ask a question to your knowledge base")
    query_parser.add_argument("question", type=str, help="The question to ask")

    # Command: ingest (Manual)
    ingest_parser = subparsers.add_parser("ingest", help="Manually ingest a text entry")
    ingest_parser.add_argument("content", type=str, help="Content to save")

    args = parser.parse_args()
    app = ChronoLogApp()

    if args.command == "start":
        print(f"[*] ChronoLog Capture Service started (Interval: {args.interval}s)...")
        print("[*] Press Ctrl+C to stop.")
        try:
            app.start_capture_loop(interval=args.interval)
        except KeyboardInterrupt:
            print("\n[*] Stopping capture service.")
            return 0

    elif args.command == "query":
        if not args.question:
            print("Error: Question required.")
            return 1
        print(f"[*] Querying: '{args.question}'")
        response = app.query_knowledge_base(args.question)
        print(f"[*] Answer: {response}")

    elif args.command == "ingest":
        app.ingest_data(source="manual", content=args.content)
        print("[*] Data ingested successfully.")

    else:
        parser.print_help()

    return 0

if __name__ == "__main__":
    sys.exit(main())