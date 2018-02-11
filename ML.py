from sklearn.metrics import f1_score, precision_score, recall_score, make_scorer
from sklearn.model_selection import cross_val_score

def run_cv(data, model_type, params, folds=5):
    classifier = model_type(**params)
    data_x = [d[:-1] for d in data]
    data_y = [d[-1] for d in data]

    scores = cross_val_score(classifier, data_x, data_y, cv=folds, scoring=make_scorer(f1_score))
    return (sum(scores)/folds)


def build_model(data, model_type, params):
    data_x = [d[:-1] for d in data]
    data_y = [d[-1] for d in data]

    return model_type(**params).fit(data_x, data_y)

def evaluate(model, test):
    test_x = [v[:-1] for v in test]
    test_y = [v[-1] for v in test]

    predictions = model.predict(test_x)
    return (f1_score(predictions, test_y), precision_score(predictions, test_y), recall_score(predictions, test_y))


def tune(data, model_type, params, percent=.8):
    classifier = model_type(**params)
    data_x = [d[:-1] for d in data]
    data_y = [d[-1] for d in data]

    train_x = data_x[:int(len(data_x)*percent)]
    train_y = data_y[:int(len(data_x)*percent)]
    test_x = data_x[int(len(data_x)*percent):]
    test_y = data_y[int(len(data_x)*percent):]

    classifier.fit(train_x, train_y)
    return evaluate(classifier, test_x, test_y)