import logging

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)


def eval_metrics(actual, pred):
    lag1_actual = actual[1:]
    lag0_actual = actual[:-1]
    return_ = np.abs(lag1_actual - lag0_actual)

    rmse = np.sqrt(mean_squared_error(lag1_actual, pred))
    mae = mean_absolute_error(lag1_actual, pred)
    r2 = r2_score(lag1_actual, pred)

    profit_down = np.sum(return_[(pred < lag0_actual) & (lag1_actual < lag0_actual)])
    profit_up = np.sum(return_[(pred > lag0_actual) & (lag1_actual > lag0_actual)])
    profit = profit_down + profit_up
    accuracy = np.sum((pred > lag0_actual) & (lag1_actual > lag0_actual)) + np.sum(
        (pred < lag0_actual) & (lag1_actual < lag0_actual))
    return rmse, mae, r2, profit, accuracy


def calculate_profit(actual, pred):
    lag1_actual = actual[1:]
    lag0_actual = actual[:-1]
    profit = np.abs(lag1_actual - pred)
    # print(lag0_actual)
    # print(lag1_actual)
    # print(pred)
    # print(profit)
    # print(pred <= lag0_actual)
    # print(lag1_actual <= lag0_actual)
    # print((pred < lag0_actual) & (lag1_actual < lag0_actual))
    profit_down = np.sum(profit[(pred < lag0_actual) & (lag1_actual < lag0_actual)])
    profit_up = np.sum(profit[(pred > lag0_actual) & (lag1_actual > lag0_actual)])

    return profit_down + profit_up


def run_test(data):
    y = np.array(data)[:, np.newaxis]
    N = len(y)
    X = np.linspace(-2, 8, N)[:, np.newaxis]

    tscv = TimeSeriesSplit(n_splits=N - 1)
    model = LinearRegression()
    print("Starting model %s" % str(model))
    predictions = []
    predictors = []
    for train_index, test_index in tscv.split(y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        fitted = model.fit(X_train, y_train)
        prediction = fitted.predict(X_test)
        predictions.append(prediction[0][0])
        predictors.append(X_test[0][0])

        if len(train_index) % 100 == 0:
            print(" #%s" % len(train_index))
        #     print(train_index)
        #     print(test_index)
        #     sys.exit(0)

    # plt.figure(figsize=(12, 6))
    # plt.plot(X, y, label='Training data')
    # plt.grid(True)
    # plt.xlabel('Input $x$')
    # plt.ylabel('Response $y$')
    # plt.legend()
    # plt.plot(predictors, predictions, label='Predictions data')
    # fig_path = f"figures/{uuid.uuid4().hex}.png"
    # plt.savefig(fig_path)
    # plt.show()
    rmse, mae, r2, profit, accuracy = eval_metrics(y.flatten(), np.array(predictions))

    print("  Profit: %s" % profit)
    print("  Accuracy: %s" % accuracy)
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
    parameters = {'normalize': model.normalize, 'fit_intercept': model.fit_intercept}
    return rmse, mae, r2, profit, accuracy, parameters


def predict(X, y, predictor):
    y = np.array(y)[:, np.newaxis]
    X = np.array(X)[:, np.newaxis]

    model = LinearRegression()
    fitted = model.fit(X, y)
    print(np.array(predictor))
    prediction = fitted.predict(np.array(predictor).reshape(1, -1))
    parameters = {'normalize': model.normalize, 'fit_intercept': model.fit_intercept}

    return prediction, parameters
