from textblob import TextBlob

class SentimentAnalyzer:
    @staticmethod
    def analyze_sentiment(text):
        """
        Analyze the sentiment of the given text
        Returns: sentiment (str), polarity (float), subjectivity (float)
        """
        blob = TextBlob(text)
        print("blob",blob)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        print("polarity",polarity)
        # Determine sentiment based on polarity
        if polarity > 0.5:
            sentiment = "Positive"                                      
            emoji = "🤩"
        elif polarity > 0.1:
            sentiment = "Positive"
            emoji = "😊"
        elif polarity < -0.1:
            sentiment = "Negative"
            emoji = "😔"
        elif polarity < -0.5:
            sentiment = "Negative"
            emoji = "😠"
        else:
            sentiment = "Neutral"
            emoji = "😐"
            
        return {
            'sentiment': sentiment,
            'emoji': emoji,
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            # 'text': text
        }
    
    @staticmethod
    def get_sentiment_explanation(polarity, subjectivity):
        """Provide explanation based on sentiment scores"""
        explanations = []
        
        # Polarity explanations
        if polarity > 0.6:
            explanations.append("Very positive sentiment")
        elif polarity > 0.2:
            explanations.append("Moderately positive sentiment")
        elif polarity > -0.2:
            explanations.append("Neutral or mixed sentiment")
        elif polarity > -0.6:
            explanations.append("Moderately negative sentiment")
        else:
            explanations.append("Very negative sentiment")
            
        # Subjectivity explanations
        if subjectivity > 0.7:
            explanations.append("Highly subjective (personal opinions)")
        elif subjectivity > 0.4:
            explanations.append("Moderately subjective")
        else:
            explanations.append("Fairly objective (fact-based)")
            
        return explanations