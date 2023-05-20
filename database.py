from deta import Deta


DETA_KEY = "a0gvexc1bqy_h5pJLaWjTz7ZTHztZGBUkfU7EfrZXafq"

# Initialize with the key 
deta = Deta(DETA_KEY)

#create/connect db
db = deta.Base("DiagnoAI_DB")

def insert_data (user_name, Mean_Radius,Mean_Perimeter,Mean_Area,Mean_Concavity,Mean_Concavity_Points,Worst_Radius,Worst_Perimeter
                ,Worst_Area,Worst_Concavity,Worst_Concavity_Points):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db.put({"User_name":user_name, "mean_Radius":Mean_Radius, "mean_Perimeter":Mean_Perimeter, "mean_Area":Mean_Area, "mean_Concavity":Mean_Concavity,
                   "mean_Concavity_Points":Mean_Concavity_Points, "worst_Radius":Worst_Radius, "worst_Perimeter":Worst_Perimeter,
                   "worst_Area":Worst_Area, "worst_Concavity":Worst_Concavity, "worst_Concavity_Points":Worst_Concavity_Points})


def fetch_all_data():
    """Returns a dict of all data"""
    res = db.fetch()
    return res.items
