from sklearn.ensemble import RandomForestClassifier, IsolationForest

def train_isolation_forest(X):
    iso = IsolationForest(contamination=0.1, random_state=42)
    y_pred = iso.fit_predict(X)
    return [1 if x == -1 else 0 for x in y_pred]

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model
