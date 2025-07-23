import os

# file paths
METRICS_DIR = os.path.join(os.path.dirname(__file__), '../csv/metrics/')
QUESTIONAIRES_DIR = os.path.join(os.path.dirname(__file__), '../csv/questionaires/')


#constants for metrics
SELECTED_METRICS = ['Total_duration_of_fixations', 
                    'Number_of_whole_fixations', 
                    'Number_of_saccades', 
                    # 'age', 
                    'Total_duration_of_whole_fixations', 
                    'Total_amplitude_of_saccades', 
                    'Recording',
                    'Average_duration_of_fixations', 
                    'Average_duration_of_whole_fixations', 
                    'Average_amplitude_of_saccades', 
                    'Number_of_fixations']
