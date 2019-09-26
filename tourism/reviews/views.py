from django.shortcuts import render
from django.http import HttpResponseRedirect
from reviews.models import Place, Review
from .forms import AddReview
from django.urls import reverse
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
# from datetime import datetime

def add_review(request):
    if request.method == 'POST':
        form = AddReview(request.POST)
        if form.is_valid():
           name = request.POST.get('reviewer','')
           place_name = request.POST.get('place_name','')
           image = request.POST.get('image','')
           review = request.POST.get('review','')
           r = Review(reviewer=name, place_name=place_name, image=image, review=review)
           r.save()
           return HttpResponseRedirect('add_new_data')
    else:
        form = AddReview()

    return render(request, 'add_review.html', {'form': form,})

# def add_new_data(request): 
  
#     if request.method == 'GET': 
  
        
#         result = Review.objects.all()
#         context = {'result':result}  
#         return render(request, 'show_result.html', context)

def get_review(request):
  if request.method == 'POST':
        form = AddReview(request.POST, request.FILES)
        if form.is_valid():
           name = request.POST.get('reviewer','')
           place_name = request.POST.get('place_name','')
           print("---------------",place_name)
           image = request.FILES.get('image','')
           print("_____image_____",image)
           review = request.POST.get('review','')



           r = Review(reviewer=name, place_name=place_name, image=image, review=review)
           r.save()
           def word_feats(words):
            return dict([(word, True) for word in words])
           positive_vocab = [ 'amazing', 'outstanding', 'fantastic', 'excited', 'good', 'nice', 'great', 'love' ]
           negative_vocab = [ 'bad', 'terrible','useless', 'hate', 'not' ]
           neutral_vocab = [ 'trip','the','was','is','actors','did','know','words', ]
           positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
           negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
           neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

           train_set = negative_features + positive_features + neutral_features

           classifier = NaiveBayesClassifier.train(train_set) 

            # Predict
           neg = 1
           pos = 1
           sentence = review
           sentence = sentence.lower()
           words = sentence.split(' ')
           for word in words:
                classResult = classifier.classify( word_feats(word))
                if classResult == 'neg':
                    neg = neg + 1
                if classResult == 'pos':
                    pos = pos + 1

           print('Positive: ' + str(float(pos)/len(words)))
           print('Negative: ' + str(float(neg)/len(words)))
           positive=str(float(pos)/len(words))
           negative=str(float(neg)/len(words))
           print(positive)
           print(negative)



           # return HttpResponseRedirect('add_new_data')
           result = Review.objects.all()
           context={}
           context['result'] = result
           context['positive'] = positive
           context['negative'] = negative



           return render(request, 'show_result.html', context)



def place_index(request):

    reviews = Place.objects.all()

    context = {

        'reviews': reviews

    }

    return render(request, 'place_index.html', context)

def place_detail(request, pk):

    review = Place.objects.get(pk=pk)

    context = {

        'review': review

    }

    return render(request, 'place_detail.html', context)


