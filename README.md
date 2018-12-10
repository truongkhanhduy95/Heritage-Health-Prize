# Heritage-Health-Prize

## Introduction to HHP

The [Heritage Health Prize](https://www.kaggle.com/c/hhp) is a $3 million reward for the team which can best
“identify patients who will be admitted to a hospital within the next year, using
historical claims data.” The purpose of this competition is apparent when
considering that over $30 billion was spent on unnecessary hospital admissions
alone in 2006. An accurate model would allow health care providers to administer
more personalized care, thereby decreasing both these unnecessary hospital
admissions and medical spending as a whole.

The prize is hosted by Kaggle, a website where teams of researchers tackle
machine learning problems in a competitive environment. Kaggle provides relevant
datasets as well as quantitative feedback for predictions made. The team
that produces the most accurate model within the time frame wins the competition
and is typically compensated in return for a description of their method.

### Dataset
https://foreverdata.org/1015/index.html

### Evaluation metric

To measure the performance of model, we use a score called <b>RMSLE (Root Mean Squared Logarithmic Error)</b>:

<img src="https://github.com/truongkhanhduy95/Heritage-Health-Prize/blob/master/img/eval.PNG"/>

Where:

1. i is a member;
2. n is the total number of members;
3. p is the predicted number of days spent in hospital for member i in the test period;
4. a is the actual number of days spent in hospital for member i in the test period.

## Task Lists

### 1. Data preparation
- [x] Importing data
- [x] Data cleaning (Hanlding missing value, hanlding categorical and continuous data,..)
- [ ] Merging files
- [ ] Handling outliners
### 2. Feature extraction
- [ ] Exploring data (Visualizations, Distribution of features,...)
### 3. Predictive modelling
- [ ] Training model (Linear Regression, Support Vector Regression, Random Forests, Logistic Regression, Neural Networks, Gradient Boosting Machines)
- [ ] Model cross-validation
- [ ] Hyperparameter tuning
### 4. Ensemble methods
- [ ] Models selection (Observation models correlations)
- [ ] Ensembling

## Summary of Individual Predictors

Predictors | Score
------------ | -------------
Linear Regression | 0.00
Support Vector Regression | 0.00
Random Forests | 0.00
Logistic Regression | 0.00
Neural Networks | 0.00
Gradient Boosting Machines | 0.00

## Ensemble
> Ensemble result: 0.00

