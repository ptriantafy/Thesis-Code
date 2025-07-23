import constants
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

if __name__ == "__main__":
    data = pd.read_csv(constants.METRICS_DIR + 'normalised_metrics.csv')
    unique_participants = data['Participant ID:'].unique() # 45 total participants
    selected_participants = np.random.choice(unique_participants, 15, replace=False)
    test_data = data[data['Participant ID:'].isin(selected_participants)]
    train_data = data[~data['Participant ID:'].isin(selected_participants)]
    # train an svm
    X_train = train_data.drop(columns=['Participant ID:', 'Total score'])
    y_train = train_data['Total score']
    X_test = test_data.drop(columns=['Participant ID:', 'Total score'])
    y_test = test_data['Total score']
    clf = svm.SVC(kernel='linear', C=1.0, random_state=42)
    clf.fit(X_train, y_train)
    # predict on test data
    y_pred = clf.predict(X_test)
    # calculate accuracy
    accuracy = np.mean(y_pred == y_test)
    print(f'Accuracy: {accuracy * 100:.2f}%')