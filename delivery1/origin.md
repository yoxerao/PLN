ref: https://aclanthology.org/D18-1404.pdf

Objective: Have a good understanding of the data provenance and characteristics: when and from where it was collected, which text
genre(s) and language(s) it covers, how it has been annotated, etc.

---

The data was collected via the Twitter API in 2018 (possibly also 2017) as a total of 416809 tweets.
The tweets were collected from two separate datasets using the Twitter API: subjective
tweets (obtained through hashtags as weak labels) and objective tweets (obtained from Twitter feeds of news accounts).
All tweets are in English and are annotated with one of the following emotions: anger, fear, joy, love, sadness and surprise.
The normalization process consisted of tokenizing the tweets by white-spaces and then preprocessed by applying lower case and replacing user mentions and URLs with a <usermention> and <url> placeholders.
The tweets contained hashtags (339 in total) that were used as noisy labels, which allowed annotation via distant supervision.
---
