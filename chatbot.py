from groq import Groq


class Chatbot:
    def __init__(self):
        # Replace with your actual Groq API key
        self.client = Groq(
            api_key="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"  # Replace with your actual Groq API key
        )

    def tell_joke(self):
        prompt = "Generate a random funny joke"
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )
        return response.choices[0].message.content

    def tell_trivia(self, topic):
        prompt = f"Give me an interesting trivia fact about {topic}"
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="mixtral-8x7b-32768",
            temperature=0.7,
        )
        return response.choices[0].message.content
