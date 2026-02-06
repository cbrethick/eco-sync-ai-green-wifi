import numpy as np
from sklearn.linear_model import LinearRegression

class Predictor:
    def __init__(self):
        self.history = []
        self.model = LinearRegression()

    def update(self, value):
        self.history.append(value)
        if len(self.history) > 12:
            self.history.pop(0)

    def predict(self):
        if len(self.history) < 5:
            return None

        X = np.arange(len(self.history)).reshape(-1, 1)
        y = np.array(self.history)
        self.model.fit(X, y)

        next_step = [[len(self.history)]]
        return float(self.model.predict(next_step)[0])
