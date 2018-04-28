maxStepDistance = 10
chanceToChangeUsage = 10 # this is a percent(0-100)

maxStepsPerHill = 10000

buyT = [0, 0, 0, 0, 0, 0, 0, 0]
sellT = [0, 0, 0, 0, 0, 0, 0, 0]
buyU = [0, 0, 0, 0, 0, 0, 0, 0]
sellU = [0, 0, 0, 0, 0, 0, 0, 0]

class parameterSet:

    buyT = [0, 0, 0, 0, 0, 0, 0, 0]
    buyU = [0, 0, 0, 0, 0, 0, 0, 0]
    sellT = [0, 0, 0, 0, 0, 0, 0, 0]
    sellU = [0, 0, 0, 0, 0, 0, 0, 0]
    minValues = [0, 0, 0, 0, 0, 0, 0, 0]
    maxValues = [0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, bT, bU, sT, sU,minV,maxV):
        self.buyT = bT
        self.buyU = bU
        self.sellT = sT
        self.sellU = sU
        self.minValues = minV
        self.maxValues = maxV

    def getBuyT(self):
        return self.buyT

    def getBuyU(self):
        return self.buyU

    def getSellT(self):
        return self.sellT

    def getSellU(self):
        return self.sellU


    def mutate(self, stepdistance, chancetochangeusage):
        import random
        for i in range(0, 8):
            buyTDir = random.randint(0, 1)
            sellTDir = random.randint(0, 1)
            chgBuyURoll = random.randint(0, 100)
            chgSellURoll = random.randint(0, 100)

            if (buyTDir == 1):
                self.buyT[i] += random.randint(0, stepdistance)
            elif (buyTDir == 0):
                self.buyT[i] -= random.randint(0, stepdistance)
            if (sellTDir == 1):
                self.sellT[i] += random.randint(0, stepdistance)
            elif (sellTDir == 0):
                self.sellT[i] -= random.randint(0, stepdistance)

            if(self.buyT[i] >= self.maxValues[i]):
                self.buyT[i]=self.maxValues[i]-1
            if (self.sellT[i] >= self.maxValues[i]):
                self.sellT[i] = self.maxValues[i] - 1

            if (self.buyT[i] <= self.minValues[i]):
                self.buyT[i] = self.minValues[i] + 1
            if (self.sellT[i] <= self.minValues[i]):
                self.sellT[i] = self.minValues[i] + 1

            if (chgBuyURoll <= chancetochangeusage):
                self.buyU[i] = random.randint(0, 2)
            if (chgSellURoll <= chancetochangeusage):
                self.sellU[i] = random.randint(0, 2)

    def getBalance(self,file,startingBalance,feeBuy,feeSell):
        import backtest
        return backtest.testStrategy(file, False, False, feeBuy, feeSell, startingBalance, self.buyT, self.buyU, self.sellT, self.sellU)


def climbRandomHill(self,minValues,maxValues):

    #print("Generating random hills")
    file = "marketdata/"+self.builder.get_object("dropdownData").get()
    #print("File: ",file)

    try:
        startingBalance = float(self.builder.get_object("txtBalance").get())
        feeBuy = float(self.builder.get_object("txtSetBuyFee").get())
        feeSell = float(self.builder.get_object("txtSetSellFee").get())
        if(startingBalance < 0):
            startingBalance = 1000
            self.builder.get_object("txtBalance").delete(0, 1000)
            self.builder.get_object("txtBalance").insert(0, "1000")
            #print("starting balance cant be negative")
        if (feeBuy < 0):
            self.builder.get_object("txtSetBuyFee").delete(0, 1000)
            self.builder.get_object("txtSetBuyFee").insert(0, ".30")
            feeBuy = .3
            #print("FEE CANNOT BE A NEGATIVE VALUE")
        if (feeSell < 0):
            self.builder.get_object("txtSetSellFee").insert(0, ".30")
            self.builder.get_object("txtSetSellFee").insert(0, ".30")
            feeSell = .3
            #print("FEE CANNOT BE A NEGATIVE VALUE")
    except:
        feeBuy = .3
        feeSell = .3
        startingBalance = 1000
        # print("invalid value entered for balance, buy fee, and/or sell fee")
        self.builder.get_object("txtBalance").delete(0, 1000)
        self.builder.get_object("txtSetBuyFee").delete(0, 1000)
        self.builder.get_object("txtSetSellFee").delete(0, 1000)
        self.builder.get_object("txtBalance").insert(0, "1000")
        self.builder.get_object("txtSetBuyFee").insert(0, ".30")
        self.builder.get_object("txtSetSellFee").insert(0, ".30")

    newBalance = 1000
    import random
    #create a random strategy that makes a profit
    timeoutCounter = 0
    while (newBalance <= startingBalance):

        dataset = self.builder.get_object("dropdownData").get()
        buyT = [0, 0, 0, 0, 0, 0, 0, 0]
        sellT = [0, 0, 0, 0, 0, 0, 0, 0]
        buyU = [0, 0, 0, 0, 0, 0, 0, 0]
        sellU = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(0, len(minValues)):
            buyT[i] = random.randint(minValues[i], maxValues[i])
            buyU[i] = random.randint(0, 2)
            sellT[i] = random.randint(minValues[i], maxValues[i])
            sellU[i] = random.randint(0, 2)
        # print(dataset)
        # print(buyT)
        # print(buyU)
        # print(sellT)
        # print(sellU)

        # process necessary data complete
        timeoutCounter+=1
        if(timeoutCounter>20):
            break

        import backtest
        newBalance = backtest.testStrategy(file,False,False,feeBuy,feeSell,startingBalance,buyT,buyU,sellT,sellU)[0]
        #print("in hill climber, new balance: ",str(newBalance))

    # print("starting with random strategy that made: ",newBalance)
    # print("Iniitial Strategy Paremeters: ")
    # print(buyT)
    # print(buyU)
    # print(sellT)
    # print(sellU)


    #print("Ascending hill.. (this could take a bit)")


    p_init = parameterSet(buyT, buyU, sellT, sellU,minValues,maxValues)
    p_optimal = p_init
    currentHigh = p_optimal.getBalance(file,startingBalance,feeBuy,feeSell)[0]
    stepsSinceNewOptimal = 0

    for j in range(0, maxStepsPerHill):

        tbt = list(map(int, p_optimal.getBuyT()))
        tbu = list(map(int, p_optimal.getBuyU()))
        tst = list(map(int, p_optimal.getSellT()))
        tsu = list(map(int, p_optimal.getSellU()))
        p_temp = parameterSet(tbt, tbu, tst, tsu,minValues,maxValues)
        p_temp.mutate(maxStepDistance, chanceToChangeUsage)

        temp_bal = p_temp.getBalance(file,startingBalance,feeBuy,feeSell)[0]

        if (temp_bal > currentHigh):
            # print("--- *** OPTIMAL PARAMS FOUND *** ---")
            p_optimal = parameterSet(p_temp.getBuyT(), p_temp.getBuyU(), p_temp.getSellT(), p_temp.getSellU(),minValues,maxValues)
            currentHigh = temp_bal
            # print("new currentHigh: ",currentHigh)
            stepsSinceNewOptimal = 0

            #print("new local profit high: $", round(currentHigh, 2))
        else:
            stepsSinceNewOptimal += 1

        #if(stepsSinceNewOptimal % 5 == 0):
           #print("number of steps since last optimal: ",stepsSinceNewOptimal)
        if (stepsSinceNewOptimal >= 50):

            #print("assuming local maxima found")
            break

    # report
    #print("=========================")
    #print("Current Hill Best Strategy:")
    #print("With final balance of: ", p_optimal.getBalance(file,startingBalance,feeBuy,feeSell)[0])
    #print("# trades = ",p_optimal.getBalance(file,startingBalance,feeBuy,feeSell)[1])

    #print("=========================")


    buyT = p_optimal.getBuyT()
    sellT = p_optimal.getSellT()
    buyU = p_optimal.getBuyU()
    sellU = p_optimal.getSellU()

    return [buyT,buyU,sellT,sellU,currentHigh]
