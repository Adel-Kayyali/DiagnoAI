import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Page Configs
st.set_page_config(
    page_title="DiagnoAI",
    page_icon="🩺",
)


#Loading the Models
BreastCancerModel=pickle.load(open('C:/Users/adool/OneDrive/سطح المكتب/DiagnoAI/Models/BreastCancer_Model.sav','rb'))
DiabetesModel=pickle.load(open('C:/Users/adool/OneDrive/سطح المكتب/DiagnoAI/Models/diabetes_model.sav','rb'))
HeartModel=pickle.load(open('C:/Users/adool/OneDrive/سطح المكتب/DiagnoAI/Models/heart_disease_model.sav','rb'))
ParkinsonsModel=pickle.load(open('C:/Users/adool/OneDrive/سطح المكتب/DiagnoAI/Models/parkinsons.sav','rb'))


#Option Menu - Sidebar
with st.sidebar:
    Menu = option_menu('DiagnoAI System',
                       ['Breast Cancer App','Diabetes App','Heart Health App','Parkinsons App'],
                       icons=['gender-female','moisture','activity','person exclamation'],
                       menu_icon='journal-medical',
                       default_index=0)
    

#Breast Cancer Page
if (Menu == 'Breast Cancer App'):
    st.title('Breast Cancer App')
    
    st.markdown('''---''')
    st.markdown('''### This app classifies breast tumors as either malignant or benign.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    #Inputs
    c1, c2 = st.columns(2)
    mean_radius=c1.text_input('Radius Mean')
    mean_perimeter=c2.text_input('Perimeter Mean')
    mean_area=c1.text_input('Area Mean')
    mean_concavity=c2.text_input('Concavity Mean')
    mean_concave_points=c1.text_input('Concave Points Mean')
    worst_radius=c2.text_input('Worst Radius')
    worst_perimeter=c1.text_input('Worst Perimeter')
    worst_area=c2.text_input('Worst Area')
    worst_concavity=c1.text_input('Worst Concavity')
    worst_concave_points=c2.text_input('Worst Concave points')


    #Breast Cancer Prediction 
    breastCancer_resault=''
    if st.button('Breast Cancer Test Resault'):
        breastCancer_pred = BreastCancerModel.predict([[mean_radius, mean_perimeter, mean_area, mean_concavity, mean_concave_points, worst_radius, worst_perimeter, 
                                                        worst_area, worst_concavity, worst_concave_points]])
        
        if (breastCancer_pred[0] == 1):
            breastCancer_resault='The Tumor is Malignant.'

        else:
           breastCancer_resault='The Tumor is Benign.'

    st.success(breastCancer_resault)


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




#Diabetes Page
if (Menu == 'Diabetes App'):
    st.title('Diabetes App')

    st.markdown('''---''')
    st.markdown('''### This app classifies whether an individual is diabetic or not.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    #Inputs
    c1, c2 = st.columns(2)
    Pregnancies=c1.text_input('Pregnancies')
    Glucose=c2.text_input('Glucose Level')
    BloodPressure=c1.text_input('Blood Pressure Value (mm Hg)')
    SkinThickness=c2.text_input('Skin Thickness)')
    Insulin=c1.text_input('Insulin Level (mu U/ml)')
    BMI=c2.text_input('BMI Value')
    DiabetesPedigreeFunction=c1.text_input('Diabetes pedigree function Value')
    Age_diabetes=c2.text_input('Age')


    #Diabetes Prediction 
    diab_resault=''
    if st.button('Diabetes Test Resault'):
        diab_pred = DiabetesModel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age_diabetes]])

        if (diab_pred[0]==1):
            diab_resault = 'This Person is Diabetic'

        else:
            diab_resault = 'This Person is Not Diabetic'

    st.success(diab_resault)


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





#Heart Health App Page
if (Menu == 'Heart Health App'):
    st.title('Heart Health App')

    st.markdown('''---''')
    st.markdown('''### This app classifies whether you have a healthy heart or any heart diseases.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    #Inputs
    c1, c2 = st.columns(2)
    Age_heart=c1.text_input('Age')
    gender=c2.text_input('Gender(Male:1, Female:0)')
    cp=c1.text_input('Chest Pain Degree')
    trestbps=c2.text_input('Blood Pressure')
    chol=c1.text_input('Cholestoral (mg/dl)')
    restecg=c2.text_input('Electrocardiographic')
    thalach=c1.text_input('Maximum Heart Rate Achieved')
    exang=c2.text_input('Exercise Induced Angina (1: yes, 0: no)')
    oldpeak=c1.text_input('ST Depression (induced by exercise relative to rest)')
    slope=c2.text_input('The Slope of the Peak Exercise ST Segment')
    ca=c1.text_input('Number of Major Vessels (0-3) colored by Flourosopy')
    thal=c2.text_input('THAL (1= Normal, 2= Fixed Defect, 3= Reversable Defect)')


    #Heart Disease Prediction 
    heart_resault=''
    if st.button('Heart Disease Test Resault'):
        heart_pred = HeartModel.predict([[Age_heart, gender, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_pred[0]==1):
            heart_resault = 'This Person Has a Heart Disease'
        
        else :
            heart_resault = 'This Person Has a Healthy Heart'

    st.success(heart_resault)


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





#Parkinsons App Page
if (Menu == 'Parkinsons App'):
    st.title('Parkinsons App')

    st.markdown('''---''')
    st.markdown('''### This app predicts whether an individual is affected by Parkinson's Disease.''')
    st.markdown('''Please note that only **Numeric Inputs** are accepted. Kindly, ensure that your input is only numbers.''')

    #Inputs
    c1, c2, c3 = st.columns(3)
    MDVPfo=c1.text_input('Average vocal Fundamental Frequency')
    MDVPflo=c2.text_input('Minimum vocal Fundamental Frequency')
    ppe=c3.text_input('PPE (fundamental frequency variation)')
    MDVPshimmer=c1.text_input('Shimmer')
    MDVPShimmerDB=c2.text_input('Shimmer - dB')
    ShimmerQ3=c3.text_input('Shimmer - APQ3')
    ShimmerQ5=c1.text_input('Shimmer - APQ5')
    MDVPapq=c2.text_input('MDVP - APQ')
    ShimmerDDA=c3.text_input('Shimmer - DDA')
    HNR=c1.text_input('HNR (ratio of noise to tonal components in the voice)')
    spread1=c2.text_input('Spread1 (fundamental frequency variation)')
    spread2=c3.text_input('Spread2 (fundamental frequency variation)')
    d2=c1.text_input('D2 (Nonlinear Dynamical Complexity)')
    MDVPjitter=c2.text_input('MDVP:Jitter%')



    #Parkinson's Disease Prediction 
    Parkinson_resault=''
    if st.button("Parkinson's Test Resault"):
        parkinsons_pred = ParkinsonsModel.predict([[MDVPfo, MDVPflo, MDVPjitter, MDVPshimmer, MDVPShimmerDB, ShimmerQ3, ShimmerQ5, MDVPapq, ShimmerDDA, HNR, spread1,
                                                    spread2, d2, ppe]])

        if (parkinsons_pred[0]==1):
            Parkinson_resault = "The Resault of The Test is Positive, This person is Affected by Parkinson's Disease."

        else :
            Parkinson_resault = "The Resault of The Test is Negative, This person is not Affected by Parkinson's Disease."

    st.success(Parkinson_resault)


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