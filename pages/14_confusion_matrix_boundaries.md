# Confusion matrix boundaries

A problem is defined by the total of known cases (labels) ($M$) and the total number of positive ($P$) and negative labels ($N$). As we have $M = P + N$, we must have $0 \leq P , N \leq M$.

From this, we get that true positive, true negative, false positive and false negative have specific trivial boundaries:
$ 0 \leq TP, FN \leq P (\leq M)$
$ 0 \leq TN, FP \leq N (\leq M)$
Nevertheless, $TP + FP$ and $FN + TN$ do not have a similar boundary, and at most can be bounded directly by $M$. Indeed, we could end up with the border cases: 
* $TP + FP = P + N = M$ with $FN + TN = 0 + 0 = 0$
* $FP + TN = 0 + 0 = 0$ with $TP + FN = P + N = M$