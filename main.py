import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import database as db


#Page Configs
page_title="DiagnoAI"
page_icon="🩺"

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon)

st.title(page_title + " " + page_icon)


#Loading the Models
BreastCancerModel=joblib.load(open('BreastCancer_Model.sav','rb'))
DiabetesModel=joblib.load(open('diabetes_model.sav','rb'))
HeartModel=joblib.load(open('heart_disease_model.sav','rb'))
ParkinsonsModel=joblib.load(open('parkinsons.sav','rb'))


#Option Menu - Sidebar
with st.sidebar:

    Menu = option_menu('DiagnoAI System',
                       options=['Breast Cancer App','Diabetes App','Heart Health App','Parkinsons App'],
                       icons=['gender-female','moisture','activity','person exclamation'],
                       menu_icon='journal-medical',
                       default_index=0)


# DataBase Interface
def get_all_data():
    items = db.fetch_all_data()
    data = [item["key"] for item in items]
    return data


#Hide Streamlit Style
hide_st_style= """
        <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """    
st.markdown(hide_st_style, unsafe_allow_html=True)
    




#Breast Cancer Page
if (Menu == 'Breast Cancer App'):
    st.title('Breast Cancer App')
    
    st.markdown('''---''')
    st.markdown('''### This app classifies breast tumors as either malignant or benign.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')


    # Create a form
    with st.form("entry_form", clear_on_submit=True):

        # Get the values of the input fields
        user_name = st.text_input("Enter Your Name")
        mean_radius = st.text_input("Radius Mean")
        mean_perimeter = st.text_input("Perimeter Mean")
        mean_area = st.text_input("Area Mean")
        mean_concavity = st.text_input("Concavity Mean")
        mean_concave_points = st.text_input("Concave Points Mean")
        worst_radius = st.text_input("Worst Radius")
        worst_perimeter = st.text_input("Worst Perimeter")
        worst_area = st.text_input("Worst Area")
        worst_concavity = st.text_input("Worst Concavity")
        worst_concave_points = st.text_input("Worst Concave points")

        # Prediction and Data Insertion button
        if st.form_submit_button('Predict and Save Data'):
            # Perform breast cancer prediction
            breastCancer_pred = BreastCancerModel.predict([[mean_radius, mean_perimeter, mean_area, mean_concavity, mean_concave_points, worst_radius, worst_perimeter, worst_area, worst_concavity, worst_concave_points]])

            if breastCancer_pred[0] == 1:
                breastCancer_result = 'The Tumor is Malignant.'
            else:
                breastCancer_result = 'The Tumor is Benign.'

            # Save the data to the database
            db.insert_BreastCancer_data(user_name, mean_radius, mean_perimeter, mean_area, mean_concavity, mean_concave_points, worst_radius, worst_perimeter, worst_area, worst_concavity, worst_concave_points, breastCancer_result)

            # Display prediction result and success message
            st.success(breastCancer_result)




    st.markdown(
    """
    ---
    ### **About Breast Cancer**\n
    Breast cancer is a type of cancer that develops in the breast cells. It is the most common cancer among women worldwide, with an estimated 2.3 million new cases diagnosed in 2020. Early detection of breast cancer is crucial for successful treatment and improved outcomes. Screening methods such as mammography, clinical breast exam, and breast self-exam can help detect breast cancer in its early stages. Treatment options for breast cancer include surgery, radiation therapy, chemotherapy, targeted therapy, and hormone therapy. However, the type of treatment will depend on several factors such as the stage of cancer, the type of breast cancer, and the patient's overall health.
    """
    """
    ---
    ### **Inputs Clarification**\n
    - **Radius Mean:** Mean of distances from the center to points on the perimeter cell
    - **Perimeter Mean:** Perimeter of cell
    - **Area Mean:** Area of cell
    - **Concavity Mean:** The severity of concave portions of the contour
    - **Concave Points Mean:** Number of concave portions of the contour
    - **Worst Radius:** Worst distance from centre point on the perimeter
    - **Worst Perimeter:** Worst perimeter of cell
    - **Worst Area:** Worst area of cell
    - **Worst Concavity:** The worst concave portions of the contour
    - **Worst Concave points:** The worst Number of concave portions of the contour
    ---
        
    ### **Model Performance:**
    - **The Accuracy of the Model: 96%**        
    """
    )




# Diabetes Page
if Menu == 'Diabetes App':
    st.title('Diabetes App')

    st.markdown('''---''')
    st.markdown('''### This app classifies whether an individual is diabetic or not.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    # Create a form
    with st.form("diabetes_form", clear_on_submit=True):
        # Get the values of the input fields
        user_name = st.text_input("Enter Your Name")
        Pregnancies = st.text_input('Pregnancies')
        Glucose = st.text_input('Glucose Level')
        BloodPressure = st.text_input('Blood Pressure Value (mm Hg)')
        SkinThickness = st.text_input('Skin Thickness')
        Insulin = st.text_input('Insulin Level (mu U/ml)')
        BMI = st.text_input('BMI Value')
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function Value')
        Age_diabetes = st.text_input('Age')

        # Diabetes Prediction
        diab_result = ''
        if st.form_submit_button('Diabetes Test Result'):
            diab_pred = DiabetesModel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age_diabetes]])

            if diab_pred[0] == 1:
                diab_result = 'This Person is Diabetic'
            else:
                diab_result = 'This Person is Not Diabetic'

            # Save the data to the database
            db.insert_Diabetes_data(user_name, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age_diabetes, diab_result)

        st.success(diab_result)


    st.markdown(
    """
    ---
    ### **About Diabetes**\n
    Diabetes is a chronic medical condition that affects the body's ability to produce or use insulin, which is a hormone that regulates blood sugar levels. It can lead to serious health complications such as heart disease, kidney damage, nerve damage, and blindness. Proper management of diabetes involves monitoring blood sugar levels, taking medications as prescribed, and making lifestyle changes such as maintaining a healthy diet and exercising regularly.
    """
    """
    ---
    ### **Inputs Clarification**\n
    - **Pregnancies:** Number of times being Pregnant
    - **Glucose Level:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test
    - **Blood Pressure Value:** Diastolic blood pressure (mm Hg)
    - **Skin Thickness:** Triceps skin fold thickness (mm)
    - **Insulin Level:** 2-Hour serum insulin (mu U/ml)
    - **BMI Value:** Body mass index (weight in kg/(height in m)^2)
    - **Diabetes pedigree function Value:** Diabetes pedigree function test
    - **Age:** Age (years)
    ---
        
    ### **Model Performance:**
    - **The Accuracy of the Model: 78%**        
    """
    )





# Heart Health App Page
if Menu == 'Heart Health App':
    st.title('Heart Health App')

    st.markdown('''---''')
    st.markdown('''### This app classifies whether you have a healthy heart or any heart diseases.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    # Create a form
    with st.form("heart_health_form", clear_on_submit=True):
        # Get the values of the input fields
        user_name = st.text_input("Enter Your Name")
        Age_heart = st.text_input('Age')
        gender = st.text_input('Gender(Male:1, Female:0)')
        cp = st.text_input('Chest Pain Degree')
        trestbps = st.text_input('Blood Pressure')
        chol = st.text_input('Cholesterol (mg/dl)')
        restecg = st.text_input('Electrocardiographic')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        exang = st.text_input('Exercise Induced Angina (1: yes, 0: no)')
        oldpeak = st.text_input('ST Depression (induced by exercise relative to rest)')
        slope = st.text_input('The Slope of the Peak Exercise ST Segment')
        ca = st.text_input('Number of Major Vessels (0-3) colored by Flourosopy')
        thal = st.text_input('THAL (1= Normal, 2= Fixed Defect, 3= Reversible Defect)')

        # Heart Disease Prediction
        heart_result = ''
        if st.form_submit_button('Heart Disease Test Result'):
            heart_pred = HeartModel.predict([[Age_heart, gender, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if heart_pred[0] == 1:
                heart_result = 'This Person Has a Heart Disease'
            else:
                heart_result = 'This Person Has a Healthy Heart'

            # Save the data to the database
            db.insert_HeartHealth_data(user_name, Age_heart, gender, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal, heart_result)

        st.success(heart_result)


    st.markdown(
    """
    ---
    ### **About Heart Disease**\n
    Heart disease refers to a range of conditions that can affect the heart, including coronary artery disease, heart rhythm problems, and heart defects. These conditions can lead to serious health problems, including heart attack, stroke, and heart failure. Risk factors for heart disease include high blood pressure, high cholesterol, smoking, diabetes, and a family history of heart disease. Treatment for heart disease may involve lifestyle changes, medications, and in some cases, surgery.
    """
    """
    ---
    ### **Inputs Clarification**\n
    - **Age:** Age (years)
    - **Gender:** Gender(Male:1, Female:0)
    - **Chest Pain Degree:** chest pain type (4 values), By a medical heart-test you can know the degree of your chest pain
    - **Blood Pressure:** Resting blood pressure
    - **Cholestoral:** Serum cholestoral in mg/dl
    - **Electrocardiographic:** resting electrocardiographic results (values 0,1,2)
    - **Maximum Heart Rate Achieved:** The Maximum Heart Rate Achieved in this month
    - **Exercise Induced Angina:** Exercise Induced Angina (1: yes, 0: no)
    - **ST Depression:** ST Depression (induced by exercise relative to rest)
    - **The Slope of the Peak Exercise ST Segment:** The Slope of the Peak Exercise ST Segment (Can be calculated by a specialized doctor)
    - **Number of Major Vessels (0-3) colored by Flourosopy:** Number of Major Vessels (0-3) colored by Flourosopy (you need to do Major Vessels Test)
    - **thal Degree:** thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
    ---
        
    ### **Model Performance:**
    - **The Accuracy of the Model: 83%**        
    """
    )





# Parkinsons App Page
if Menu == 'Parkinsons App':
    st.title('Parkinsons App')

    st.markdown('''---''')
    st.markdown('''### This app predicts whether an individual is affected by Parkinson's Disease.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    # Create a form
    with st.form("parkinsons_form", clear_on_submit=True):
        # Get the values of the input fields
        user_name = st.text_input("Enter Your Name")
        MDVPfo = st.text_input('Average vocal Fundamental Frequency')
        MDVPflo = st.text_input('Minimum vocal Fundamental Frequency')
        ppe = st.text_input('PPE (fundamental frequency variation)')
        MDVPshimmer = st.text_input('Shimmer')
        MDVPShimmerDB = st.text_input('Shimmer - dB')
        ShimmerQ3 = st.text_input('Shimmer - APQ3')
        ShimmerQ5 = st.text_input('Shimmer - APQ5')
        MDVPapq = st.text_input('MDVP - APQ')
        ShimmerDDA = st.text_input('Shimmer - DDA')
        HNR = st.text_input('HNR (ratio of noise to tonal components in the voice)')
        spread1 = st.text_input('Spread1 (fundamental frequency variation)')
        spread2 = st.text_input('Spread2 (fundamental frequency variation)')
        d2 = st.text_input('D2 (Nonlinear Dynamical Complexity)')
        MDVPjitter = st.text_input('MDVP:Jitter%')

        # Parkinson's Disease Prediction
        parkinsons_result = ''
        if st.form_submit_button("Parkinson's Test Result"):
            parkinsons_pred = ParkinsonsModel.predict([[MDVPfo, MDVPflo, MDVPjitter, MDVPshimmer, MDVPShimmerDB, ShimmerQ3, ShimmerQ5, MDVPapq, ShimmerDDA, HNR, spread1,
                                                        spread2, d2, ppe]])

            if parkinsons_pred[0] == 1:
                parkinsons_result = "The Result of The Test is Positive. This person is affected by Parkinson's Disease."
            else:
                parkinsons_result = "The Result of The Test is Negative. This person is not affected by Parkinson's Disease."

            # Save the data to the database
            db.insert_Parkinsons_data(user_name, MDVPfo, MDVPflo, MDVPjitter, MDVPshimmer, MDVPShimmerDB, ShimmerQ3, ShimmerQ5, MDVPapq, ShimmerDDA, HNR, spread1, spread2, d2, ppe, parkinsons_result)

        st.success(parkinsons_result)

    st.markdown(
    """
    ---
    ### **About Parkinson's Disease**\n
    Parkinson's Disease is a neurodegenerative disorder that affects movement. Symptoms include tremors, stiffness, and difficulty with balance and coordination. It occurs when there is a loss of dopamine-producing cells in the brain. Parkinson's Disease has no known cure, but treatments such as medication and therapy can help manage symptoms and improve quality of life. Early detection and diagnosis are crucial for effective treatment.
    """
    """
    ---
    ### **Inputs Clarification**\n
    - **Average vocal Fundamental Frequency:** MDVP-Fo(Hz) Average vocal Fundamental Frequency
    - **Minimum vocal Fundamental Frequency:** MDVP-Flo(Hz) Minimum vocal fundamental frequency
    - **MDVP-Jitter%:** Measure of variation in fundamental frequency in Jitter %
    - **Shimmer:** Measure of variation in amplitude as Normal Shimmer
    - **Shimmer - dB:** Measure of variation in amplitude in dB
    - **Shimmer - APQ3:** Measure of variation in amplitude in APQ3
    - **Shimmer - APQ5:** Measure of variation in amplitude in APQ5
    - **MDVP - APQ:** Measure of variation in amplitude in APQ
    - **Shimmer - DDA:** Measure of variation in amplitude of DDA
    - **HNR:** Measure of ratio of noise to tonal components in the voice
    - **Spread1:** A Nonlinear measure of fundamental frequency variation type 1
    - **Spread2:** A Nonlinear measure of fundamental frequency variation type 2
    - **D2:** A Nonlinear dynamical complexity measures
    - **PPE:** A Nonlinear measures of fundamental frequency variation
    ---
        
    ### **Model Performance:**
    - **The Accuracy of the Model: 92%**        
    """
    )
