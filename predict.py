import streamlit as st
import pickle
import pandas as pd
import random
import string


#third time
'''MODEL_DIR = os.environ.get('MODEL_DIR', 'D:\College_project\FBmodel.pkl')
MODEL_FILE = os.path.join(MODEL_DIR, 'model.pkl')

with open(MODEL_FILE, 'rb') as f:
    load_model = pickle.load(f)'''

load_model = pickle.load(open('https://github.com/satyajit2000/Fetal_health_classifier/blob/master/FBmodel.pkl','rb'))
def main():

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        baseline_value = st.text_input("baseline_value", value=df.loc[0, 'baseline value'])
        accelerations = st.text_input("accelerations", value=df.loc[0, 'accelerations'])
        fetal_movement = st.text_input("fetal_movement", value=df.loc[0, 'fetal_movement'])
        uterine_contractions = st.text_input("uterine_contractions", value=df.loc[0, 'uterine_contractions'])
        light_decelerations = st.text_input("light_decelerations", value=df.loc[0, 'light_decelerations'])
        prolongued_decelerations = st.text_input("prolongued_deceleration", value=df.loc[0, 'prolongued_decelerations'])
        abnormal_short_term_variability = st.text_input("abnormal_short_term_variability",
                                                        value=df.loc[0, 'abnormal_short_term_variability'])
        mean_value_of_short_term_variability = st.text_input("mean_value_of_short_term_variability",
                                                             value=df.loc[0, 'mean_value_of_short_term_variability'])
        percentage_of_time_with_abnormal_long_term_variability = st.text_input(
            "percentage_of_time_with_abnormal_long_term_variability", value=df.loc[0, 'percentage_of_time_with_abnormal_long_term_variability'])
        mean_value_of_long_term_variability = st.text_input("mean_value_of_long_term_variability",
                                                            value=df.loc[0, 'mean_value_of_long_term_variability'])
        histogram_width = st.text_input("histogram_width", value=df.loc[0, 'histogram_width'])
        histogram_min = st.text_input("histogram_min", value=df.loc[0, 'histogram_min'])
        histogram_max = st.text_input("histogram_max", value=df.loc[0, 'histogram_max'])
        histogram_number_of_peaks = st.text_input("histogram_number_of_peaks", value=df.loc[0, 'histogram_number_of_peaks'])
        histogram_number_of_zeroes = st.text_input("histogram_number_of_zeroes", value=df.loc[0, 'histogram_number_of_zeroes'])
        histogram_mode = st.text_input("histogram_mode", value=df.loc[0, 'histogram_mode'])
        histogram_mean = st.text_input("histogram_mean", value=df.loc[0, 'histogram_mean'])
        histogram_median = st.text_input("histogram_median", value=df.loc[0, 'histogram_median'])
        histogram_variance = st.text_input("histogram_variance", value=df.loc[0, 'histogram_variance'])
        histogram_tendency = st.text_input("histogram_tendency", value=df.loc[0, 'histogram_tendency'])
        if st.button("predict"):

            makeprediction=load_model.predict([[baseline_value,accelerations,fetal_movement,uterine_contractions,light_decelerations,prolongued_decelerations,abnormal_short_term_variability,mean_value_of_short_term_variability,percentage_of_time_with_abnormal_long_term_variability,mean_value_of_long_term_variability,histogram_width,histogram_min,histogram_max,histogram_number_of_peaks,histogram_number_of_zeroes,histogram_mode,histogram_mean,histogram_median,histogram_variance,histogram_tendency]])
            a = makeprediction
            if a==1:
                st.write('Normal')
            elif a==2:
                st.write('Suspect')
            else:
                st.write('Pathological')

            if makeprediction!=(df.loc[0, 'fetal_health']):

                # Create a new file with the original CSV data
                new_file_path = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + ".csv"
                df.to_csv(new_file_path, index=False)


if __name__ == '__main__':
    main()



