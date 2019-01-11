# Heritage Health Prize Competition

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

(Due to Github's limitation, archived dataset have been store in data.zip. Please extract and save it in ./data folder)

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
- [x] Data cleaning (Hanlding missing value, hanlding categorical and continuous data,...)
- [x] Merging files
### 2. Feature extraction
- [x] Handling outliners
- [] Exploring data (Visualizations, Distribution of features,...)
- [x] Feature scaling (Standardisation, Mean Normalisation, Min-Max Scaling,... )
### 3. Predictive modelling
- [x] Linear Regression
- [x] Ridge Regression
- [x] Support Vector Regression
- [x] Random Forests
- [x] Logistic Regression
- [x] Neural Networks
- [x] Gradient Boosting Machines
### 4. Models summary
- [x] Model cross-validation (Stratified K-Fold)
- [x] Hyperparameter tuning
### 5. Ensemble methods
- [ ] Models selection (Observation models correlations)
- [ ] Ensembling

## Summary of Individual Predictors

Predictors | Score
------------ | -------------
Linear Regression |  0.4850
Ridge Regression | 0.4844
Support Vector Regression | 0.4783
Random Forests | 0.4846
Logistic Regression | 0.5065
Neural Networks | 0.48
Gradient Boosting Machines | 0.48

## Ensemble method
> Ensemble result: 0.00

