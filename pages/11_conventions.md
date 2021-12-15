# Conventions on the confusion matrix

Confusion matrices are usually used to evaluate the performance of a classification algorithm. It can be used for classifying any number of labels, but usually the labels are binary.
* Cancer prediction:
* Dropout prediction:
* COVID19 prediction:
* Buying decision prediction:
* Fraud prediction:
The positive and negative labels are the states to be predicted.

To create a confusion matrix, there area some arbitrarily decision regarding order and orientation. There are 4 options, as shown on the picture:

IMAGE

As you can see, the differences are essencially if rows should be the true labels or predicted labels, and if values should be in order positive-negative, or negative-positive. As in any arbitrary choice, not everyone will agree and use the same. Be careful when reading and interpreting the results!

The "convention A" is the most common. It is as defined on wikipedia and scikit learn.
https://en.wikipedia.org/wiki/Confusion_matrix
https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
Nice discusion:
https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed

The "convention D" is the convention taken by Andrew Ng's on the course on Machine Learning:
https://medium.com/@aiii/machine-learning-diagnostics-b2256d78d51e

Conventions B and C are so frequently used. 

Despite our highest regards to Andrew, we will take the convention A as the most common one, and use
that convention on the rest of this content.
