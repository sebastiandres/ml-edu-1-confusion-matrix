# Conventions on the confusion matrix

Confusion matrices are used to evaluate the performance of a classification algorithm. A classification algorithm is any instance where a prediction is made over a finite set of options:
* Cancer prediction: Based on medical data, let's predict whether a person has cancer or not.
* Dropout prediction: Based on the student data and performance, let's predict whether a student is going to drop out or not.
* COVID19 prediction: Based on the person medical data and close contacts, let's predict whether a person is infected with COVID-19 or not.
* Buying decision prediction: Based on the customer data and the price, let's predict whether a customer will buy the product or not.
* Fraud prediction: Based on the customer past behavior, let's predict whether a customer transaction is fraudulent or not.
* Image classification: Based on the image data, let's predict what is on the image: a cat, a dog, a bird, a flower, a car, a house, a tree, etc.

The classification problem can be applied to problems with multiple categories (labels), but in general the problem is binary. The labels are named 0 (negative) and 1 (positive) usually based on what is the base level (no cancer, no dropout, no covid, no buying, no fraud) and the target level (cancer, dropout, covid, buying, fraud) of the problem.

**After** making a prediction with the algoritm, you can contrast the prediction with the ground truth. There are 4 posibilities (for the binary case):
* True positive: The prediction is correct and the prediction is positive.
* True negative: The prediction is correct and the prediction is negative.
* False positive: The prediction is incorrect and the prediction is positive.
* False negative: The prediction is incorrect and the prediction is negative.

A confusion matrix is an arragement of the countings of each of these outcome posibilities. To create a confusion matrix, there are some arbitrarily decision regarding order and orientation. There are 4 options, as shown on the picture:

<img src="https://github.com/sebastiandres/ml_edu_confusion_matrix/blob/main/images/conventions.png?raw=true" alt="Conventions" width="700">

As you can see, the differences are essencially if rows should be the true labels or predicted labels, and if values should be in order positive-negative, or negative-positive. As in any arbitrary choice, not everyone will agree and use the same. Be careful when reading and interpreting the results!

The "convention A" is the most common. It is as defined on 
[wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix) 
and 
[scikit learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html). There is a nice discussion on [stackoverflow](https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed)

The "convention D" is the convention taken by Andrew Ng's on his [courses on Machine Learning](https://medium.com/@aiii/machine-learning-diagnostics-b2256d78d51e).

Conventions B and C are not frequently used, as far as I know.

Despite our highest regards to Andrew, we will take the convention A as the most common one, and use
that convention on the rest of this content.

Next, we will have a interactive widget to play with the confusion matrix!