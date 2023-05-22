from deta import Deta


DETA_KEY = "a0gvexc1bqy_h5pJLaWjTz7ZTHztZGBUkfU7EfrZXafq"

# Initialize with the key 
deta = Deta(DETA_KEY)

#create/connect db
db_breastCancer = deta.Base("DiagnoAIBreastCancer")
db_diabetes = deta.Base("DiagnoAI_Diabetes")
db_heartHealth = deta.Base("DiagnoAI_HeartHealth")
db_parkinsons = deta.Base("db_Parkinsons")



def insert_BreastCancer_data (user_name, Mean_Radius,Mean_Perimeter,Mean_Area,Mean_Concavity,Mean_Concavity_Points,Worst_Radius,Worst_Perimeter
                ,Worst_Area,Worst_Concavity,Worst_Concavity_Points, breastCancer_result):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db_breastCancer.put({"User_name":user_name, "mean_Radius":Mean_Radius, "mean_Perimeter":Mean_Perimeter, "mean_Area":Mean_Area, "mean_Concavity":Mean_Concavity,
                   "mean_Concavity_Points":Mean_Concavity_Points, "worst_Radius":Worst_Radius, "worst_Perimeter":Worst_Perimeter,
                   "worst_Area":Worst_Area, "worst_Concavity":Worst_Concavity, "worst_Concavity_Points":Worst_Concavity_Points, "breastCancer_result":breastCancer_result})



def insert_Diabetes_data (user_name, Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age_diabetes, diab_result):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db_diabetes.put({"user_name":user_name, "Pregnancies":Pregnancies, "Glucose":Glucose, "BloodPressure":BloodPressure, "SkinThickness":SkinThickness,
                   "Insulin":Insulin, "BMI":BMI, "DiabetesPedigreeFunction":DiabetesPedigreeFunction,
                   "Age_diabetes":Age_diabetes, "diab_result":diab_result})



def insert_HeartHealth_data (user_name, Age_heart, gender, cp, trestbps, chol, restecg, thalach, exang, oldpeak, slope, ca, thal, heart_result):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db_heartHealth.put({"user_name":user_name, "Age_heart":Age_heart, "gender":gender, "cp":cp, "trestbps":trestbps,
                   "chol":chol, "restecg":restecg, "thalach":thalach,
                   "exang":exang, "oldpeak":oldpeak,"slope":slope, "ca":ca, "thal":thal, "heart_result":heart_result})



def insert_Parkinsons_data (user_name, MDVPfo, MDVPflo, MDVPjitter, MDVPshimmer, MDVPShimmerDB, ShimmerQ3, ShimmerQ5, MDVPapq, ShimmerDDA, HNR, spread1,
                                                        spread2, d2, ppe, parkinsons_result):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db_parkinsons.put({"user_name":user_name, "MDVPfo":MDVPfo, "MDVPflo":MDVPflo, "MDVPjitter":MDVPjitter, "MDVPshimmer":MDVPshimmer,
                   "MDVPShimmerDB":MDVPShimmerDB, "ShimmerQ3":ShimmerQ3, "ShimmerQ5":ShimmerQ5,
                   "MDVPapq":MDVPapq, "ShimmerDDA":ShimmerDDA,"HNR":HNR, "spread1":spread1, "spread2":spread2, "d2":d2, "ppe":ppe, "parkinsons_result":parkinsons_result})



def fetch_all_data():
    """Returns a dict of all data"""
    res = db_breastCancer.fetch()
    return res.items
