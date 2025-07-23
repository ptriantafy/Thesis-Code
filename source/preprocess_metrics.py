import pandas as pd
import matplotlib.pyplot as plt
import constants
from sklearn.preprocessing import MinMaxScaler

if __name__ == "__main__":
    sentence_df = pd.read_csv(constants.METRICS_DIR + 'sentences.tsv', sep='\t')
    scores_df = pd.read_csv(constants.QUESTIONAIRES_DIR + 'participant_percent_score.csv')
    # print(sentence_df.columns.tolist())
    selected_metrics_df = pd.DataFrame()
    for col in sentence_df.columns:
        for metric in constants.SELECTED_METRICS:
            if metric in col:
                selected_metrics_df = pd.concat([selected_metrics_df, sentence_df[[col]]], axis=1)
    selected_metrics_df.rename(columns={'Recording': 'Participant ID:'}, inplace=True)
    merged_df = pd.merge(selected_metrics_df, scores_df[['Participant ID:', 'Total score']], on='Participant ID:', how='inner')
    # normalise all columns except 'Participant ID:' and 'Total score'
    for row in merged_df['Total score']:
        if row >= 0.5:
            merged_df.loc[merged_df['Total score'] == row, 'Total score'] = 1
        else:
            merged_df.loc[merged_df['Total score'] == row, 'Total score'] = 0
    for col in merged_df.columns:
        if col not in ['Participant ID:', 'Total score']:
            scaler = MinMaxScaler()
            merged_df[col] = scaler.fit_transform(merged_df[[col]])
    merged_df.fillna(0, inplace=True)
    merged_df.to_csv(constants.METRICS_DIR + 'normalised_metrics.csv', index=False)
    