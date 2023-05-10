import pickle
import pandas as pd
import streamlit as st
import os
import time



load_model = pickle.load(open('FinalModel2.pkl', 'rb'))
def main():
    menu = ["Manual data uplaod", "File data upload"]
    choice = st.sidebar.selectbox("menu", menu)
    if choice == "Manual data uplaod":
        st.title("Fetal Health Detection")
        col1, col2 = st.columns(2)
        with col1:
            baseline_value = st.text_input("baseline_value")
        with col2:
            accelerations = st.text_input("accelerations")
        col1, col2 = st.columns(2)
        with col1:
            fetal_movement = st.text_input("fetal_movement")
        with col2:
            uterine_contractions = st.text_input("uterine_contractions")
        col1, col2 = st.columns(2)
        with col1:
            light_decelerations = st.text_input("light_decelerations")
        with col2:
            prolongued_decelerations = st.text_input("prolongued_deceleration")
        col1, col2 = st.columns(2)
        with col1:
            abnormal_short_term_variability = st.text_input("abnormal_short_term_variability")
        with col2:
            mean_value_of_short_term_variability = st.text_input("mean_value_of_short_term_variability")
        col1, col2 = st.columns(2)
        with col1:
            percentage_of_time_with_abnormal_long_term_variability = st.text_input(
                "percentage_of_time_with_abnormal_long_term_variability")
        with col2:
            mean_value_of_long_term_variability = st.text_input("mean_value_of_long_term_variability")
        col1, col2 = st.columns(2)
        with col1:
            histogram_width = st.text_input("histogram_width")
        with col2:
            histogram_min = st.text_input("histogram_min")
        col1, col2 = st.columns(2)
        with col1:
            histogram_max = st.text_input("histogram_max")
        with col2:
            histogram_number_of_peaks = st.text_input("histogram_number_of_peaks")
        col1, col2 = st.columns(2)
        with col1:
            histogram_number_of_zeroes = st.text_input("histogram_number_of_zeroes")
        with col2:
            histogram_mode = st.text_input("histogram_mode")
        col1, col2 = st.columns(2)
        with col1:
            histogram_mean = st.text_input("histogram_mean")
        with col2:
            histogram_median = st.text_input("histogram_median")
        col1, col2 = st.columns(2)
        with col1:
            histogram_variance = st.text_input("histogram_variance")
        with col2:
            histogram_tendency = st.text_input("histogram_tendency")
        if st.button("predict"):
            makeprediction = load_model.predict([[baseline_value, accelerations, fetal_movement, uterine_contractions,
                                                  light_decelerations, prolongued_decelerations,
                                                  abnormal_short_term_variability, mean_value_of_short_term_variability,
                                                  percentage_of_time_with_abnormal_long_term_variability,
                                                  mean_value_of_long_term_variability, histogram_width, histogram_min,
                                                  histogram_max, histogram_number_of_peaks, histogram_number_of_zeroes,
                                                  histogram_mode, histogram_mean, histogram_median, histogram_variance,
                                                  histogram_tendency]])
            with st.spinner('Wait for it...'):
                time.sleep(2)
            a = makeprediction

            if a == 1:
                st.success('Normal', icon="✅")
            elif a == 2:
                st.warning('Suspect', icon="⚠️")
            elif a == 3:
                st.error('Pathological', icon="🚨")




    elif choice == "File data upload":
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
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                a = makeprediction
                if a==1:
                    st.success('Normal', icon="✅")
                elif a==2:
                    st.warning('Suspect', icon="⚠️")
                elif a==3:
                    st.error('Pathological', icon="🚨")





if __name__ == '__main__':
    main()



