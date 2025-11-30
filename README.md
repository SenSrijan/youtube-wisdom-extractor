# YouTube Wisdom Extractor

🚀 **AI-Powered YouTube Video Analysis Tool** | Extract insights, summaries, and actionable takeaways from any YouTube video using advanced LLM technology. Transform video content into structured markdown reports with smart caching and cross-platform CLI support.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](https://github.com/SenSrijan/youtube-wisdom-extractor)

> **Keywords:** YouTube transcript analysis, AI video summarization, content extraction tool, educational video insights, productivity automation, CLI video analyzer, YouTube API alternative, video content mining, knowledge extraction, markdown report generator

## Features

- 📹 **Direct YouTube URL Processing** - Just paste the URL and get insights
- 🧠 **AI-Powered Analysis** - Uses advanced LLM for deep content understanding
- 📊 **Two Analysis Modes**:
  - **Standard**: Quick, focused insights
  - **Comprehensive**: Deep, detailed analysis with implementation roadmaps
- 💾 **Smart Caching** - Avoids re-processing the same videos
- 🔄 **Fallback Mechanisms** - Multiple transcript sources for reliability
- 🎯 **Beautiful Markdown Output** - Professional, readable formatting

## Installation

### Install from Source
```bash
git clone https://github.com/SenSrijan/youtube-wisdom-extractor.git
cd youtube-wisdom-extractor
pip install -e .
```

## Configuration

1. Create a `.env` file in your project directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TRANSCRIPT_API_KEY=your_transcript_api_key_here  # Optional fallback
```

2. Get your API keys:
   - **Groq API Key**: Sign up at [console.groq.com](https://console.groq.com)
   - **Transcript API Key**: Sign up at [transcriptapi.com](https://transcriptapi.com) (optional)

## Usage

### Command Line Interface

```bash
# Standard analysis
youtube-wisdom "https://www.youtube.com/watch?v=VIDEO_ID"

# Comprehensive analysis
youtube-wisdom -c "https://www.youtube.com/watch?v=VIDEO_ID"
youtube-wisdom --comprehensive "https://www.youtube.com/watch?v=VIDEO_ID"

# Specify analysis type
youtube-wisdom --type comprehensive "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Interactive Mode
```bash
youtube-wisdom
# Then enter the YouTube URL when prompted
```

### Python API
```python
from youtube_wisdom_extractor import process_video

# Standard analysis
result = process_video("https://www.youtube.com/watch?v=VIDEO_ID")

# Comprehensive analysis
result = process_video("https://www.youtube.com/watch?v=VIDEO_ID", "comprehensive")
print(result)
```

## Output Examples

### Standard Mode
- 📹 Video Title/Topic
- ⚡ Executive Summary
- 🔑 Key Insights
- 🛠 Actionable Takeaways
- 🏁 Conclusion

### Comprehensive Mode
- 🎯 Comprehensive Analysis Header
- 📊 Content Overview
- 🧠 Core Concepts & Frameworks
- 🔍 Deep Insights Analysis
- 🛠 Implementation Roadmap
- 📚 Knowledge Connections
- ⚠️ Critical Considerations
- 🎯 Value Proposition
- 🏁 Synthesis & Next Steps

## Requirements

- Python 3.8+
- Groq API Key (for AI analysis)
- Internet connection

## Cross-Platform Support

✅ **Windows** - Full support  
✅ **macOS** - Full support  
✅ **Linux** - Full support  

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Credits

This project uses the excellent [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) by [@jdepoix](https://github.com/jdepoix) for YouTube transcript extraction. Special thanks for making YouTube transcript access simple and reliable.

## License

MIT License - see LICENSE file for details.

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/SenSrijan/youtube-wisdom-extractor/issues)
- 📧 **Email**: srijanstacks@gmail.com
- 💬 **Discussions**: [GitHub Discussions](https://github.com/SenSrijan/youtube-wisdom-extractor/discussions)