from micromlgen import port_wifi_indoor_positioning

def featureVectorConverter():
    with open('scanSamples.txt', 'r') as file:
        data = file.read()
    
    samples = f'''
        {data}
    '''

    X, y, classmap, converter_code = port_wifi_indoor_positioning(samples)
    
    with open("Converter.h", "w") as f:
        print(converter_code, file=f)
    
    print("Features Vector Generated")