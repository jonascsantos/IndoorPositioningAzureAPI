from sklearn.tree import DecisionTreeClassifier
from micromlgen import port_wifi_indoor_positioning, port

def classifierGenerator():
    with open('scanSamples.txt', 'r') as file:
        data = file.read()
    
    samples = f'''
        {data}
    '''

    X, y, classmap, converter_code = port_wifi_indoor_positioning(samples)
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    with open("Classifier.h", "w") as f:
        print(port(clf, classmap=classmap), file=f)

    print("Classifier Generated")