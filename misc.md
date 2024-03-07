5.1 Data
We construct a set of hashtags to collect a separate dataset of English tweets from the Twitter
API. Specifically, we use the eight basic emotions:
anger, anticipation, disgust, fear, joy, sadness,
surprise, and trust. The hashtags (339 total) serve
as noisy labels, which allow annotation via distant
supervision as in (Go et al., 2009). To ensure data
quality, we follow the pre-processing steps proposed by (Abdul-Mageed and Ungar, 2017), and
considered the hashtag appearing in the last position of a tweet as the ground truth. We split
the data into training (90%) and testing (10%)
datasets. The final distribution of the data and
a list of hashtag examples for each emotion are
provided in Table 3. In the following section we
evaluate the effectiveness of the enriched patterns
on several emotion recognition tasks. We use F1-
score as the evaluation metric, which is commonly
used in emotion recognition studies due to the imbalanced nature of the emotion datasets.
