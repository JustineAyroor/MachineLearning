import sys,subprocess

Ber_Dataset = []

Dataset = ["climate","micromass","qsar","hill_valley","breast_cancer","ionosphere"]
for i in range(0,len(Dataset),1):
    print("Running for least_squares_adaptive "+ Dataset[i])
    average = 0
    for j in range(0,10,1):
        ber = subprocess.check_output([sys.executable,"least_squares_adaptive.py",Dataset[i]+".data",Dataset[i]+".trainlabels."+str(j),Dataset[i]+".labels"])
        print("BER of label "+ str(j) + " = " + str(float(ber.decode('utf-8'))))
        # Ber_Dataset.append(float(ber.decode('utf-8')))
        average+=float(ber.decode('utf-8'))
    # print(Ber_Dataset)
    print("Average Error Test for "+ Dataset[i] + ": "+ str((average/10)))
    print("Running for hinge_loss_adaptive "+ Dataset[i])
    average = 0
    for j in range(0,10,1):
        ber = subprocess.check_output([sys.executable,"hinge_loss_adaptive.py",Dataset[i]+".data",Dataset[i]+".trainlabels."+str(j),Dataset[i]+".labels"])
        print("BER of label "+ str(j) + " = " + str(float(ber.decode('utf-8'))))
        # Ber_Dataset.append(float(ber.decode('utf-8')))
        average+=float(ber.decode('utf-8'))
    # print(Ber_Dataset)
    print("Average Error Test for "+ Dataset[i] + ": "+ str((average/10)))
    