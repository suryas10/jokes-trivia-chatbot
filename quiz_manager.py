from groq import Groq
import json


class QuizManager:
    def __init__(self):
        # Replace with your actual Groq API key
        self.client = Groq(
            api_key="gsk_YOUR_API_KEY_HERE"  # Replace with your actual Groq API key
        )

    def create_quiz(self, topic):
        prompt = f"""Create a quiz with 5 questions about {topic}. 
        Return the response in the following JSON format:
        [
            {{"question": "Question 1", "options": ["A) option1", "B) option2", "C) option3", "D) option4"], "correct_answer": "A"}},
            ... (repeat for all 5 questions)
        ]
        """

        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )

        try:
            quiz_data = json.loads(response.choices[0].message.content)
            return quiz_data
        except json.JSONDecodeError:
            return self._get_fallback_quiz(topic)

    def _get_fallback_quiz(self, topic):
        # Fallback quiz in case the API response isn't properly formatted
        return [
            {
                "question": f"Basic question about {topic}?",
                "options": [
                    "A) Option 1",
                    "B) Option 2",
                    "C) Option 3",
                    "D) Option 4"
                ],
                "correct_answer": "A"
            }
        ] * 5