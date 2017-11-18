import pandas as pd

filename = 'C:/Users/user/Desktop/Kaggle/en_train.csv'
file = pd.read_csv(filename)

words = file['before'].values
del file
unique_words = list(set(words))
repeated_words = []

for word in words:
    if word not in unique_words:
        repeated_words.append(word)
        
print(len(repeated_words))