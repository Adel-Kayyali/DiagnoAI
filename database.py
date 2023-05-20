from deta import Deta


DETA_KEY = "a0gvexc1bqy_h5pJLaWjTz7ZTHztZGBUkfU7EfrZXafq"

# Initialize with the key 
deta = Deta(DETA_KEY)

#create/connect db
db = deta.Base("DiagnoAI_DB")

def insert_data (user_name, Mean_Radius,Mean_Perimeter,Mean_Area,Mean_Concavity,Mean_Concavity_Points,Worst_Radius,Worst_Perimeter
                ,Worst_Area,Worst_Concavity,Worst_Concavity_Points):
    """Returns the report on a succesful creation, otherwise raises an error"""
    return db.put({"User Name (Key)":user_name, "Mean_Radius":Mean_Radius, "Mean_Perimeter":Mean_Perimeter, "Mean_Area":Mean_Area, "Mean_Concavity":Mean_Concavity,
                   "Mean_Concavity_Points":Mean_Concavity_Points, "Worst_Radius":Worst_Radius, "Worst_Perimeter":Worst_Perimeter,
                   "Worst_Area":Worst_Area, "Worst_Concavity":Worst_Concavity, "Worst_Concavity_Points":Worst_Concavity_Points})


def fetch_all_data():
    """Returns a dict of all data"""
    res = db.fetch()
    return res.items
