from sys import argv
import os.path
import numpy as np
import pandas as pd

def isFile(fileName):
    if(not os.path.isfile(fileName)):
        raise ValueError("You must provide a valid filename as parameter")
    print("File: ",fileName)

def calculate_error():
   
    df_pred = pd.read_csv(predictFile)
    df_actual = pd.read_csv(actualFile)

    if(df_pred.shape[0] != df_actual.shape[0]):
        print('Prediction count: ', df_pred.shape[0])
        print('Actual count: ', df_actual.shape[0])
        raise ValueError("The file does not have same rows")

    # Merge by Member key
    df = df_pred.merge(df_actual, left_on = 'MemberID', right_on = 'MemberID')#.drop(['ClaimsTruncated'],axis=1)
    print(df.head())

    # Print top K error
    K = 10
    print('---------------------------------------------')
    print('Top error')
    df['Error'] = abs(df['DaysInHospital_x'] - df['DaysInHospital_y'])
    print(df.nlargest(K, 'Error'))
    print('---------------------------------------------')

    # Largest error count
    count = df.loc[(df['DaysInHospital_x'] == 0 ) & (df['DaysInHospital_y'] == 15), 'MemberID'].count()
    print('Largest error count: ', count)

    # Precision
    true_pos = df.loc[(df['DaysInHospital_x'] > 0) & (df['DaysInHospital_y'] > 0), 'MemberID'].count()
    false_pos = df.loc[(df['DaysInHospital_x'] > 0) & (df['DaysInHospital_y'] == 0), 'MemberID'].count()
    precision = true_pos / (true_pos + false_pos)

    # Recall
    #true_neg = df.loc[(df['DaysInHospital_x'] == 0) & (df['DaysInHospital_y'] == 0), 'MemberID'].count()
    false_neg = df.loc[(df['DaysInHospital_x'] == 0) & (df['DaysInHospital_y'] > 0), 'MemberID'].count()
    recall = true_pos / (true_pos + false_neg)

    # F1 Score
    f1_score = 2 * precision * recall / (precision + recall)
    print('True pos: ', true_pos)
    print('---------------------------------------------')
    print('Precison: ', precision)
    print('Recall: ', recall)
    print()
    print('F1 Score: ', f1_score)
    

    # Evaluation metric : Root Mean Square Logarithmic Error (RMSLE)
    # https://www.kaggle.com/c/hhp#evaluation
    n = df_pred.shape[0]
    err = np.sqrt(((np.log(df['DaysInHospital_x'] + 1) - np.log(df['DaysInHospital_y'] + 1)) ** 2).sum() / n)

    return err

predictFile = None
actualFile = None

if __name__ == "__main__":
    try:
        predictFile = argv[1]   # Load from first argument
        isFile(predictFile)

        actualFile = argv[2]    # Load from second argument
        isFile(actualFile)

        err = calculate_error() # Calculate
        
        # Print top 5 error
        print('---------------------------------------------')
        print("Error:",err)

        pass
    except Exception as e:
        print(e)
        raise
