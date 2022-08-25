from cgi import test
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def getModel():
    train_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/multiple_classification/red_wine_MupYMkf.xlsx?raw=true',sheet_name='train')
    test_df = pd.read_excel('https://github.com/cranberryai/todak_todak_python/blob/master/machine_learning/multiple_classification/red_wine_MupYMkf.xlsx?raw=true',sheet_name='test')

    x_data = train_df.iloc[:,1:-1].to_numpy()
    y_data = train_df['등급'].to_numpy()
    xtest_data = test_df.iloc[:,1:-1].to_numpy()
    ytest_data = test_df['등급'].to_numpy()

    dclf = DecisionTreeClassifier()
    dclf.fit(x_data,y_data)

    return dclf