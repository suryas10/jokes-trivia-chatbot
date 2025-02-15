from textblob import TextBlob
import re


class NLPProcessor:
    def __init__(self):
        pass

    def get_intent(self, text):
        # Convert to lowercase
        text = text.lower()

        # Basic intent classification using keyword matching
        if any(word in text for word in ['joke', 'funny', 'laugh']):
            return 'joke'
        elif any(word in text for word in ['trivia', 'fact', 'tell me about']):
            return 'trivia'
        elif any(word in text for word in ['quiz', 'test', 'questions']):
            return 'quiz'
        return 'unknown'

    def extract_topic(self, text):
        # Look for topic after specific keywords
        keywords = ['about', 'on', 'regarding', 'concerning']
        text_lower = text.lower()

        for keyword in keywords:
            if keyword in text_lower:
                # Find the position of the keyword
                pos = text_lower.find(keyword)
                # Get the text after the keyword
                topic_text = text[pos + len(keyword):].strip()
                if topic_text:
                    # Remove any punctuation at the end
                    topic_text = re.sub(r'[?.!,]$', '', topic_text)
                    return topic_text

        # If no topic found, return None
        return None

    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity