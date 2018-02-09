
NLP Group Project: Golden GLobes info extractor

How to run:

install the spacy parser:
-make sure you have python's pip installed
-pip3 install spacy
-python3 -m spacy download en

python3 main.py





Basic source code overview:

We've got a corpus of Tweets. Each Tweet is just a string containing the text of that Tweet.

The Corpus object is a wrapper around a list of Tweet objects.

The basic idea behind this project is filtering and counting. By filtering, I mean that
we can get a pretty good idea of the kind of tweets we want to look at for a particular
piece of info. Say we want to find out who won the "Best Actor in Motion Picture" award.
Well, we can start of by getting a set of tweets that only contain the words "best" and
"actor". It's really fast to filter this list. if you've worked with databases before,
it's basically like doing a database query. Filtering in this way gives us two benefits.
One, the resulting subset is smaller, and thus is is quicker to process. Two, we filter
out a lot of the "noise" from other tweets that are not relevant to our current query.


Now that we've got a smaller list to work with, we can perform more computationally
complex tasks. We can run complex regex queries, and even run the tweets through
parsers.

It's at this point where statistics come into the picture (mostly in Wizard.py). 
Given good pre-filtering, whats left should be the "meat" of what we care about. The 
person or thing that we want to extract should occur in most of the filtered tweets. 
If we have a basic heuristic that extracts proper nouns, then the thing we care about 
should be the most frequent. This is the power of having tons of data to work with. 
You can do inference without actually having to reason about anything. (Getting into the
foundations of associative learning!).

Of course it's not as easy as it sounds. We need to engineer filtering solutions
that are robust to the vagaries in our data. That's why this project is interesting.