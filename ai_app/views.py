from django.shortcuts import render
from .services import SentimentAnalyzer

# REST imports for the API endpoint
from textblob import TextBlob
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def index(request):
    """Render main page with sentiment analysis form.
    
    This function handles GET requests to the root URL and displays
    the main sentiment analysis page to the user.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered HTML template (index.html) for the main page
    """
    return render(request, 'index.html')


def analyze_sentiment(request):
    """Handle form POST from the web UI and render results on the same page.

    Expects a POST field named 'text_input'. Uses SentimentAnalyzer service
    if available, otherwise falls back to TextBlob.
    """
    if request.method != 'POST':
        return render(request, 'index.html')

    text = request.POST.get('text_input', '').strip()
    if not text:
        return render(request, 'index.html', {'error': 'Please enter the text.'})
    if len(text) > 1000:
        return render(request, 'index.html', {'error': 'Text is too long. Please limit to 1000 characters.'})

    # Prefer using custom service if available
    try:
        result = SentimentAnalyzer.analyze_sentiment(text)
        explanations = SentimentAnalyzer.get_sentiment_explanation(
            result.get('polarity', 0), result.get('subjectivity', 0)
        )
        result['explanations'] = explanations
    except Exception:
        # Fallback to TextBlob
        tb = TextBlob(text)
        polarity = tb.sentiment.polarity
        subjectivity = tb.sentiment.subjectivity
        if polarity > 0:
            sentiment = 'Positive'
            emoji = '😊'
        elif polarity < 0:
            sentiment = 'Negative'
            emoji = '😞'
        else:
            sentiment = 'Neutral'
            emoji = '😐'
        result = {
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'emoji': emoji,
            'explanations': []
        }

    return render(request, 'index.html', {
        'text': text,
        'sentiment': result.get('sentiment'),
        'emoji': result.get('emoji')
    })


@api_view(['POST'])
def sentiment_analysis(request):
    """API endpoint (JSON) to return sentiment analysis using TextBlob.

    POST JSON: {"text": "..."}
    Returns JSON with sentiment, polarity, subjectivity and emoji.
    """
    text = request.data.get('text', '')
    if not isinstance(text, str) or not text.strip():
        return Response({'error': 'No text provided.'}, status=status.HTTP_400_BAD_REQUEST)

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    if polarity > 0:
        sentiment = 'Positive'
        emoji = '😊'
    elif polarity < 0:
        sentiment = 'Negative'
        emoji = '😞'
    else:
        sentiment = 'Neutral'
        emoji = '😐'

    return Response({
        'sentiment': sentiment,
        'polarity': polarity,
        'subjectivity': subjectivity,
        'emoji': emoji
    }, status=status.HTTP_200_OK)