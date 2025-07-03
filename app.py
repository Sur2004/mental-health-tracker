from flask import Flask, render_template, request

app = Flask(__name__)

mental_fitness_tips = {
    "1": {
        "a": [
            "Great job maintaining your calmness! Keep practicing mindful breathing for 5 minutes daily.",
            "Try gratitude journaling each morning to start your day positively."
        ],
        "b": [
            "Try journaling in the evening to track stress triggers.",
            "Use 10 minutes of guided meditation daily with apps like Calm or Headspace."
        ],
        "c": [
            "Practice deep breathing techniques like 4-7-8 breathing when feeling anxious.",
            "Limit caffeine intake and avoid screens 1 hour before bed."
        ],
        "d": [
            "Create a calming night routine with warm showers and relaxing music.",
            "Consider speaking to a mental health counselor if anxiety feels overwhelming."
        ],
    },
    "2": {
        "a": [
            "Maintain your positive routines and social connections.",
            "Try a daily outdoor walk for 15 minutes to boost mood."
        ],
        "b": [
            "Get 15–20 minutes of sunlight exposure daily for natural mood lift.",
            "Set 3 small daily goals and celebrate each achievement."
        ],
        "c": [
            "Use gratitude journaling to interrupt negative thought cycles.",
            "Try short 10-15 minute walks when feeling down."
        ],
        "d": [
            "Reach out to a trusted friend or a mental health professional.",
            "Establish gentle routines: consistent wake/sleep times and hydration."
        ],
    },
    "3": {
        "a": [
            "Keep a consistent sleep and meal schedule for emotional stability.",
            "Engage in creative hobbies weekly to reduce stress."
        ],
        "b": [
            "Track habits to identify stress triggers.",
            "Replace one unhealthy habit with a positive one daily (e.g., stretching instead of phone scrolling)."
        ],
        "c": [
            "Join support groups or find accountability partners.",
            "Remove environmental triggers where possible, like late-night snacks or excessive device use."
        ],
        "d": [
            "Professional support can guide you towards recovery.",
            "Practice self-compassion and focus on building one healthy habit at a time."
        ],
    },
    "4": {
        "a": [
            "You show resilience. Keep journaling to process your thoughts.",
            "Try mindfulness exercises to enhance your focus."
        ],
        "b": [
            "Challenge negative self-talk with positive affirmations.",
            "Incorporate regular physical activity to improve mood."
        ],
        "c": [
            "Set boundaries to manage stress and prevent burnout.",
            "Practice relaxation techniques like progressive muscle relaxation."
        ],
        "d": [
            "Consider talking with a therapist for deeper emotional support.",
            "Join a support group for shared experiences and encouragement."
        ],
    },
    "5": {
        "a": [
            "Your stress management is effective; maintain these strategies.",
            "Use breathing exercises during stressful moments."
        ],
        "b": [
            "Try to break tasks into smaller steps to reduce overwhelm.",
            "Take regular breaks and practice self-care."
        ],
        "c": [
            "Explore cognitive behavioral techniques to address stress triggers.",
            "Avoid multitasking to focus better and lower stress."
        ],
        "d": [
            "Seek professional counseling to develop personalized coping skills.",
            "Consider mindfulness-based stress reduction programs."
        ],
    },
    "6": {
        "a": [
            "You're attentive to your mental health—keep up regular self-check-ins.",
            "Continue building social support and positive connections."
        ],
        "b": [
            "Practice grounding techniques when feeling overwhelmed.",
            "Engage in hobbies that bring you joy regularly."
        ],
        "c": [
            "Develop a routine for relaxation and stress management.",
            "Limit exposure to distressing media or news."
        ],
        "d": [
            "Professional mental health support is recommended for sustained well-being.",
            "Consider therapy or counseling to address persistent challenges."
        ],
    }
}

# Questions and options for rendering
questions = {
    "1": "How often do you feel calm and relaxed?",
    "2": "How connected do you feel to others?",
    "3": "How consistent is your daily routine?",
    "4": "How do you handle negative thoughts?",
    "5": "How well do you manage stress?",
    "6": "How often do you check in on your mental health?"
}

options = {
    "a": "Almost Always",
    "b": "Often",
    "c": "Sometimes",
    "d": "Rarely"
}

@app.route('/')
def home():
    return render_template('questionnaire.html', questions=questions, options=options)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = {}
    for qnum in questions.keys():
        ans = request.form.get(f"q{qnum}")
        if ans and ans in options.keys():
            user_answers[qnum] = ans

    # Aggregate suggestions
    suggestions = []
    for qnum, ans_key in user_answers.items():
        tips = mental_fitness_tips.get(qnum, {}).get(ans_key, [])
        suggestions.extend(tips)

    helpful_links = [
        {"title": "Mental Health America", "url": "https://mhanational.org/"},
        {"title": "National Institute of Mental Health", "url": "https://www.nimh.nih.gov/"},
        {"title": "Calm Meditation App", "url": "https://www.calm.com/"},
        {"title": "Headspace Meditation App", "url": "https://www.headspace.com/"},
    ]

    return render_template('suggestions.html', suggestions=suggestions, questions=questions, user_answers=user_answers, options=options, helpful_links=helpful_links)

if __name__ == '__main__':
    app.run(debug=True)
