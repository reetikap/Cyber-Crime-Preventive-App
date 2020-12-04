from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob 


       
#def clean_tweet(self,tweet):
    #return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())  
 
@api_view(["POST"])
def get_tweet_sentiment(tweet):
       
        # create TextBlob object of passed tweet text
    tweet  = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(tweet.read())).split())
    analysis = TextBlob(tweet)
        # set sentiment
    if analysis.sentiment.polarity > 0:
        return Response({"sentiment":"positive"}, status=status.HTTP_200_OK)
    elif analysis.sentiment.polarity == 0:
        return Response({"sentiment":"neutral"}, status=status.HTTP_200_OK)
    else:
        return Response({"sentiment":"negative"}, status=status.HTTP_200_OK)