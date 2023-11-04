import pickle
import os


def model1predict(data):
    modulepath = os.path.dirname(__file__)
    loaded_model = pickle.load(open(os.path.join(modulepath, 'mlworks/model.sav'), 'rb'))
    pred = loaded_model.predict([[int(data["certificate"]), int(data["data_structure"]),
                                  int(data["operating_system"]), int(data["database_management"]),
                                  int(data["computer_networks"]), int(data["cryptography"]),
                                  int(data["object_oriented_programming"]), int(data["computer_graphics"]),
                                  int(data["digital_electronics"]), int(data["engineering_mathematics"]),
                                  int(data["statistics"]), int(data["communication"]), int(data["skill_english"]),
                                  int(data["skill_programming"]), int(data["skill_creativity"]), int(data["hackathon"]),
                                  int(data["hackathon_role"]), int(data["creative_critical"]),
                                  int(data["self_learning"]), int(data["management_technical"]),
                                  int(data["gaming"]), int(data["art"]), int(data["literature"]),
                                  int(data["business"])]])
    return pred[0]
