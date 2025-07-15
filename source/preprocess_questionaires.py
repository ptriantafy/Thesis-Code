import pandas as pd
import matplotlib.pyplot as plt
import constants

if __name__ == "__main__":
    q1_df = pd.read_csv(constants.QUESTIONAIRES_DIR + '001_Questionaire.csv')
    q2_df = pd.read_csv(constants.QUESTIONAIRES_DIR + '002_Questionaire.csv')
    q3_df = pd.read_csv(constants.QUESTIONAIRES_DIR + '003_Questionaire.csv')
    q4_df = pd.read_csv(constants.QUESTIONAIRES_DIR + '004_Questionaire.csv')
    merged_df = pd.concat([
        q1_df[["Participant ID:", "Total score"]],
        q2_df[['Participant ID:', 'Total score']],
        q3_df[['Participant ID:', 'Total score']],
        q4_df[['Participant ID:', 'Total score']]
    ], ignore_index=True, axis=0)
    # merged_df.to_csv(constants.QUESTIONAIRES_DIR + 'merged_questionaires_scores.csv', index=False)
    negative_scores = pd.read_csv(constants.QUESTIONAIRES_DIR + 'negative_scores.csv')
    new_merged_df = pd.DataFrame(columns=['Participant ID:', 'Total score'])
    for index, row in q1_df.iterrows():
        total_score =  0
        for response in negative_scores['response']:
            if response in row.values:
                total_score += float(negative_scores[negative_scores['response'] == response]['markings'].values[0])
        if total_score < 0:
            total_score = 0
        total_score /= 8
        new_merged_df = new_merged_df._append({'Participant ID:': row['Participant ID:'], 'Total score': total_score}, ignore_index=True)
    for index, row in q2_df.iterrows():
        total_score =  0
        for response in negative_scores['response']:
            if response in row.values:
                total_score += float(negative_scores[negative_scores['response'] == response]['markings'].values[0])
        if total_score < 0:
            total_score = 0
        total_score /= 9
        new_merged_df = new_merged_df._append({'Participant ID:': row['Participant ID:'], 'Total score': total_score}, ignore_index=True)
    for index, row in q3_df.iterrows():
        total_score =  0
        for response in negative_scores['response']:
            if response in row.values:
                total_score += float(negative_scores[negative_scores['response'] == response]['markings'].values[0])
        if total_score < 0:
            total_score = 0
        total_score /= 8
        new_merged_df = new_merged_df._append({'Participant ID:': row['Participant ID:'], 'Total score': total_score}, ignore_index=True)        
    for index, row in q4_df.iterrows():
        total_score =  0
        for response in negative_scores['response']:
            if response in row.values:
                total_score += float(negative_scores[negative_scores['response'] == response]['markings'].values[0])
        if total_score < 0:
            total_score = 0
        total_score /= 10
        new_merged_df = new_merged_df._append({'Participant ID:': row['Participant ID:'], 'Total score': total_score}, ignore_index=True)
    # new_merged_df.to_csv(constants.QUESTIONAIRES_DIR + 'new_merged_questionaires_scores.csv', index=False)


    old_scores = pd.read_csv(constants.QUESTIONAIRES_DIR + 'merged_questionaires_scores.csv')
    plt.figure(figsize=(10, 6))
    # plt.hist(old_scores['Total score'], bins=20, alpha=0.5, label='Old Scores', color='blue')
    plt.hist(new_merged_df['Total score'], bins=200, alpha=0.5, label='New Scores', color='orange')
    plt.legend(loc='upper right')
    plt.xlabel('Total Score')
    plt.ylabel('Frequency')
    plt.title('Histogram of Total Scores')
    plt.legend()
    plt.show()


