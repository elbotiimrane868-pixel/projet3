# AI Chatbot 🤖

A modern AI-powered conversational chatbot built with Python and Hugging Face Transformers.

## Features
- Natural language understanding
- Conversational responses using state-of-the-art NLP models
- Easy to extend and customize
- Simple command-line interface

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot:
```bash
python main.py
```

Then simply type your messages and the chatbot will respond!

### Example
```
You: Hello! How are you?
Bot: Hello! I'm doing well, thank you for asking. How can I help you today?

You: What's the weather like?
Bot: I don't have access to real-time weather data, but you can check weather websites or apps for current conditions.
```

## Project Structure
```
.
├── main.py           # Entry point
├── chatbot.py        # Core chatbot logic
├── config.py         # Configuration
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

## Configuration
Edit `config.py` to customize:
- Model selection
- Response temperature
- Conversation history limit
- Custom system prompts

## Technologies Used
- **Python 3.8+**
- **Hugging Face Transformers** - State-of-the-art NLP models
- **PyTorch** - Deep learning framework
- **NLTK** - Natural language toolkit

## Future Enhancements
- Web interface with Flask/FastAPI
- Multi-language support
- Sentiment analysis
- Context-aware responses
- Database integration for conversation history
- API endpoints

## License
MIT License

## Author
Created with ❤️
