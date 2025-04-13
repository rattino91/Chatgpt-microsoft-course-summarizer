
Microsoft Course Summarizer with OpenAI
=====================================

[![Python](https://img.shields.io/badge/Python-3.8+-blue)] 
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)] 
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT-purple)]

A Flask web application that generates customized summaries for Microsoft certification courses using OpenAI's API.

🛠️ Why I Built This
------------
As someone preparing for Microsoft certifications, I noticed two key problems:

Time Waste: 40% of study time was spent condensing course materials into summaries

Inconsistency: Manual notes often missed key concepts or had uneven formatting

This tool solves both by:

Automating the most tedious part of exam prep

Standardizing output with AI-generated structures

Adapting to different learning styles (visual/concise/detailed)

The technical motivation was to:
------------
✅ Learn API integration with OpenAI
✅ Build a practical Flask application
✅ Create something useful for other learners

Key Features
------------
• Dynamic prompt generation from user inputs
• Easy in-code course customization
• Configurable summary formats
• Downloadable text results
• Responsive web interface

Customization Options
---------------------
To add new courses, edit the CORSI_MICROSOFT dictionary in deepseek.py:

```python
CORSI_MICROSOFT = {
    "NEW-900": {
        "nome": "New Course Name",
        "url": "https://learn.microsoft.com/course-url" 
    },
    # ... existing courses ...
}
```

To modify summary formats, update TIPI_RIASSUNTO:

```python 
TIPI_RIASSUNTO = [
    {
        "id": "new_format",
        "nome": "Custom Format Name"
    },
    # ... existing formats ... 
}
```

How It Works
------------
1. User selects course and summary format
2. System builds optimized prompt
3. Prompt sent to OpenAI API
4. Generated summary displayed
5. Option to download results

Setup Instructions
-----------------
1. Clone repository:
   git clone https://github.com/yourusername/repo.git
   
2. Create .env file:
   echo "OPENAI_API_KEY=your_key" > .env

3. Install requirements:
   pip install -r requirements.txt

4. Run application:
   run the script

Notes
-----
• Keep your .env file private
• Monitor OpenAI API usage
• MIT Licensed
```
