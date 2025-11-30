import argparse
from .core import process_video, get_transcript_text, extract_wisdom

def main():
    parser = argparse.ArgumentParser(
        description="Extract wisdom from YouTube videos using AI",
        prog="youtube-wisdom"
    )
    parser.add_argument("url", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "-c", "--comprehensive", 
        action="store_true", 
        help="Enable comprehensive detailed extraction"
    )
    parser.add_argument(
        "-t", "--type", 
        choices=["standard", "comprehensive"], 
        default="standard", 
        help="Extraction type (default: standard)"
    )
    parser.add_argument(
        "--version", 
        action="version", 
        version="%(prog)s 1.0.0"
    )
    
    args = parser.parse_args()
    
    # Determine extraction type
    extraction_type = "comprehensive" if args.comprehensive or args.type == "comprehensive" else "standard"
    
    # Get video URL
    video_url = args.url or input("Enter YouTube video URL: ")
    
    print(f"🚀 Starting {extraction_type} wisdom extraction...")
    transcript_text = get_transcript_text(video_url)
    
    if transcript_text:
        wisdom = extract_wisdom(transcript_text, extraction_type)
        print("\n" + "="*80)
        print(f"📖 EXTRACTED WISDOM ({extraction_type.upper()})")
        print("="*80)
        print(wisdom)
        print("\n" + "="*80)
    else:
        print("❌ Failed to get transcript from video.")

if __name__ == "__main__":
    main()