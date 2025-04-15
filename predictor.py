# # predictor.py
# import numpy as np
# import pandas as pd
# import pickle
# import os

# # Load the trained KNN model
# with open("model/knn_model.pkl", "rb") as f:
#     knn = pickle.load(f)

# def predict_next_sums(last_three):
#     recent = list(map(int, last_three))
#     predicted = []

#     for _ in range(4):
#         input_seq = np.array(recent[-3:]).reshape((1, 3))
#         next_sum = knn.predict(input_seq)[0]
#         rounded = round(next_sum)
#         predicted.append(rounded)
#         recent.append(rounded)

#     # Save to CSV
#     df = pd.DataFrame({"input": [str(last_three)], "predicted": [predicted]})
#     os.makedirs("data", exist_ok=True)
#     df.to_csv("data/predictions.csv", mode='a', header=not pd.read_csv("data/predictions.csv").empty if os.path.exists("data/predictions.csv") else True, index=False)

#     return predicted

# *****************************************************************************
# predictor.py
# import numpy as np
# import pandas as pd
# import pickle
# import os

# # Load the trained KNN model
# with open("model/knn_model.pkl", "rb") as f:
#     knn = pickle.load(f)

# def predict_next_sums(last_three, actual=None):
#     recent = list(map(int, last_three))
#     predicted = []

#     for _ in range(4):
#         input_seq = np.array(recent[-3:]).reshape((1, 3))
#         next_sum = knn.predict(input_seq)[0]
#         rounded = round(next_sum)
#         predicted.append(rounded)
#         recent.append(rounded)

#     # Save to CSV
#     os.makedirs("data", exist_ok=True)
#     row = {
#         "input": str(last_three),
#         "predicted": str(predicted),
#         "actual": str(actual) if actual else "N/A"
#     }

#     csv_path = "data/predictions.csv"
#     write_header = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0
#     df = pd.DataFrame([row])
#     df.to_csv(csv_path, mode='a', header=write_header, index=False)

#     return predicted



# *************************************************************************************
import numpy as np
import pandas as pd
import pickle
import os

# Load trained KNN model
with open("model/knn_model.pkl", "rb") as f:
    knn = pickle.load(f)

def predict_next_sums(last_three):
    recent = list(map(int, last_three))
    predicted = []

    for _ in range(4):
        input_seq = np.array(recent[-3:]).reshape((1, 3))
        next_sum = knn.predict(input_seq)[0]
        rounded = round(next_sum)
        predicted.append(rounded)
        recent.append(rounded)

    return predicted

def save_actual_result(input_vals, predicted_vals, actual):
    os.makedirs("data", exist_ok=True)
    row = {
        "input": str(input_vals),
        "predicted": str(predicted_vals),
        "actual": str(actual)
    }

    csv_path = "data/predictions.csv"
    write_header = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0
    df = pd.DataFrame([row])
    df.to_csv(csv_path, mode='a', header=write_header, index=False)
