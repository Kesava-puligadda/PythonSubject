import pandas as pd
train_T= pd.read_csv('./train.csv')
test_T= pd.read_csv('./test.csv')
combine = [train_T, test_T]

print(train_T[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))