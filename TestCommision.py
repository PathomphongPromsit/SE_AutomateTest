from commission import commission_cal
task = []
with open("DataTestCommission.txt", "r") as f:
    correct = 0
    notcorrect = 0
    for line in f:
        task=line.strip()

        data  = task.split(" ")

        L = data[0]
        S = data[1]
        B = data[2]
        testResult = data[3]
        
        if commission_cal(L,S,B) == testResult :
            print (L,S,B,"correct!!")
            correct = correct+1
        else :
            print (L,S,B,"fail!!")
            ans_cal = commission_cal(L, S, B)
            print("Test:", testResult, "Cal:", ans_cal)
            notcorrect = notcorrect+1
    print("Total Correct Test Case:", correct)
    print("Total Fail Test Case:", notcorrect)