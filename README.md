# 🌏 Sarvam AI Tour Planner

A beautiful AI-powered tour planning application using [Sarvam AI](https://www.sarvam.ai/)'s chat completions API. Plan your perfect Northern India tour based on your budget and available days!

## ✨ Features

- **AI-Powered Planning**: Leverages Sarvam AI's language model to create personalized tour itineraries
- **Beautiful Terminal Output**: Uses the `rich` library to render markdown responses with colors and formatting
- **Customizable**: Adjust your budget and duration to get tailored recommendations
- **Interactive**: Simple command-line interface with user-friendly prompts

## 📋 Prerequisites

- Python 3.12 or higher
- Sarvam AI API key ([Get one here](https://www.sarvam.ai/))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/rajib76/sarvam_ai_explore.git
cd sarvam_ai_explore
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
SARVAM_API_KEY=your_api_key_here
```

### 5. Run the Application

```bash
python examples/first_hello_to_sarvam.py
```

## 💡 Usage

When you run the application, you'll be prompted to enter:

1. **Your budget** (in INR)
2. **Number of days** for the tour

The AI will then generate a detailed, day-by-day itinerary including:
- Destinations to visit
- Accommodation recommendations
- Transportation options
- Cost breakdowns
- Local attractions and experiences

### Example Session

```
🌏 Northern India Tour Planner

Enter your budget: 100000
Enter the number of days you want to spend in the tour: 5

Planning your perfect tour...

[Beautiful formatted output with headings, bullet points, and pricing details]
```

## 📦 Dependencies

- **sarvamai** - Official Sarvam AI Python SDK
- **python-dotenv** - Environment variable management
- **rich** - Beautiful terminal formatting and markdown rendering

## 🗂️ Project Structure

```
sarvam_ai_explore/
├── examples/
│   └── first_hello_to_sarvam.py    # Main tour planner application
├── requirements.txt                 # Project dependencies
├── .env                            # API keys (not tracked in git)
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SARVAM_API_KEY` | Your Sarvam AI API subscription key | Yes |

## 🎨 Output Features

The application uses the `rich` library to provide:
- **Colorful headers** with emoji icons
- **Properly rendered markdown** including:
  - Headings and subheadings
  - Bullet points and numbered lists
  - Tables and separators
  - Bold and italic text
- **Clean, readable formatting** in the terminal

## 🛠️ Troubleshooting

### ModuleNotFoundError: No module named 'sarvamai'

Make sure you've:
1. Activated the virtual environment: `source venv/bin/activate`
2. Installed dependencies: `pip install -r requirements.txt`
3. Using the correct Python version (3.12+)

### API Key Issues

Ensure your `.env` file is in the root directory and contains:
```
SARVAM_API_KEY=your_actual_api_key
```

## 📝 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to open issues or submit pull requests for improvements!

## 📧 Contact

For questions or feedback, please reach out through GitHub issues.

---

**Built with ❤️ using [Sarvam AI](https://www.sarvam.ai/)**
