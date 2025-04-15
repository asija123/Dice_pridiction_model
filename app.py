# # app.py
# from flask import Flask, render_template, request
# from predictor import predict_next_sums

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None
#     if request.method == 'POST':
#         last_three = request.form.getlist('sum')
#         if len(last_three) == 3:
#             prediction = predict_next_sums(last_three)
#     return render_template('index.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)




# *******************************************************************************

# app.py
# from flask import Flask, render_template, request
# from predictor import predict_next_sums

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None
#     if request.method == 'POST':
#         last_three = request.form.getlist('sum')
#         actual = request.form.get('actual')
#         if len(last_three) == 3:
#             prediction = predict_next_sums(last_three, actual)
#     return render_template('index.html', prediction=prediction)

# if __name__ == '__main__':
#     app.run(debug=True)

# ***********************************************************************************
import os
from flask import Flask, render_template, request
from predictor import predict_next_sums, save_actual_result

app = Flask(__name__)
last_input = None
last_prediction = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global last_input, last_prediction
    prediction = None
    message = None

    if request.method == 'POST':
        if 'predict' in request.form:
            last_input = request.form.getlist('sum')
            if len(last_input) == 3:
                prediction = predict_next_sums(last_input)
                last_prediction = prediction
        elif 'submit_actual' in request.form:
            actual_value = request.form.get('actual')
            if last_input and last_prediction:
                save_actual_result(last_input, last_prediction, actual_value)
                message = f"✅ Actual value {actual_value} saved successfully!"

    return render_template('index.html', prediction=last_prediction, message=message)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)