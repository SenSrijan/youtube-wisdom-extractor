# Deployment Guide

## Step-by-Step Guide to Deploy Your CLI Tool

### 1. Prepare Your Repository

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Create GitHub repository and push
git remote add origin https://github.com/yourusername/youtube-wisdom-extractor.git
git branch -M main
git push -u origin main
```

### 2. Update Package Information

Edit `setup.py` and update:
- `author="Your Name"`
- `author_email="your.email@example.com"`
- `url="https://github.com/yourusername/youtube-wisdom-extractor"`

### 3. Test Locally

```bash
# Install in development mode
pip install -e .

# Test the CLI
youtube-wisdom "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 4. Build and Upload to PyPI

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to TestPyPI first (optional)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

### 5. Cross-Platform Testing

#### Windows
```cmd
pip install youtube-wisdom-extractor
youtube-wisdom --help
```

#### macOS/Linux
```bash
pip install youtube-wisdom-extractor
youtube-wisdom --help
```

### 6. Create Releases

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `YouTube Wisdom Extractor v1.0.0`
5. Describe the features and attach built files

### 7. Documentation

Update README.md with:
- Installation instructions
- Usage examples
- API documentation
- Contributing guidelines

### 8. Continuous Integration (Optional)

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        python-version: [3.8, 3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .
    - name: Test CLI
      run: |
        youtube-wisdom --help
```

## Installation Methods for Users

### Method 1: PyPI (Recommended)
```bash
pip install youtube-wisdom-extractor
```

### Method 2: GitHub
```bash
pip install git+https://github.com/yourusername/youtube-wisdom-extractor.git
```

### Method 3: Local Development
```bash
git clone https://github.com/yourusername/youtube-wisdom-extractor.git
cd youtube-wisdom-extractor
pip install -e .
```

## Cross-Platform Compatibility

✅ **Windows**: Full support with cmd, PowerShell, Git Bash  
✅ **macOS**: Full support with Terminal, iTerm2  
✅ **Linux**: Full support with bash, zsh, fish shells  

## Distribution Checklist

- [ ] Update version numbers
- [ ] Test on all platforms
- [ ] Update documentation
- [ ] Create GitHub release
- [ ] Upload to PyPI
- [ ] Test installation from PyPI
- [ ] Update social media/announcements