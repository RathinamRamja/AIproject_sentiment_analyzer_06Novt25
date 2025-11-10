from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from .services import SentimentAnalyzer

def index(request):
    """Main page with sentiment analysis form"""
    return render(request, 'index.html')

def analyze_sentiment(request):
    """API endpoint to analyze sentiment"""
    if request.method == 'POST':
        text = request.POST.get('text_input', '').strip()
        print("text",text)
        
        if not text:
            print("fdg")
            return render(request, 'index.html', {'error': 'Please enter the text.'})
        print("fdg1")
        if len(text) > 1000:
            return render(request, 'index.html', {'error': 'Text is too long. Please limit to 1000 characters.'})

        # Analyze sentiment
        result1 = SentimentAnalyzer.analyze_sentiment(text)
        print('result1',result1)
        
        explanations = SentimentAnalyzer.get_sentiment_explanation(
            result1['polarity'], 
            result1['subjectivity']
        )
        
        result1['explanations'] = explanations
        print('result',result1)
        print('explanations',explanations)
        print("hiihhhhh")
        
        # Render the result in the same template
        return render(request, 'index.html', {
            'text': text,
            'sentiment': result1['sentiment'],
            'emoji': result1['emoji']
        })
        
        
   

    # If it's a GET request, just show the form
    return render(request, 'index.html')

        
        
    #     return JsonResponse(result)
    
    # return JsonResponse({'error': 'Only POST method allowed'})