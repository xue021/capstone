#read csv

#get params

#test strat with params


#####
import numpy as np
import pandas as pd



def testStrategy(file,verbose_mode,loggingEnabled,feeBuy,feeSell, starting_balance,thresholds_buy,thresholds_buy_usage, thresholds_sell,thresholds_sell_usage):
    
    
    data = pd.read_csv(file)

    moneySpentOnAsset = 0
    logData = pd.DataFrame(columns=["row", "date","type","price","shares","balance","lastAmountSpent","fee","profit"])
    logDataIndex = 1
    

    if(verbose_mode):
        print("FILENAME:",file)
        print("starting bal: ",starting_balance)
        print("thresholds buy :  ",thresholds_buy)
        print("thresholds buy usage:  ",thresholds_buy_usage)
        print("thresholds sell : ",thresholds_sell)
        print("thresholds sell usage: ",thresholds_sell_usage)
        print("Buy Fee:  ", feeBuy)
        print("Sell Fee: ", feeSell)
    
    isHolding = False
    sharesHolding = 0
    balance = starting_balance
    
    for i in  range(0,len(data)):
        if(isHolding==False):
            if(ShouldTrade(data.loc[i,:],thresholds_buy,thresholds_buy_usage)):
                if(verbose_mode == True):
                    print("BUYING")
                    print(data.loc[i,:])
                isHolding = True
                moneySpentOnAsset = balance
                #subtract fee
                feeBuyValue = round(balance*feeBuy,2)
                balance = balance-feeBuyValue
                sharesHolding = balance/data.loc[i,"close"]
                balance = round(balance - sharesHolding*data.loc[i,"close"],2)
                #START LOGGING
                logData.loc[logDataIndex]=[i,data.loc[i,"date"],"buy",data.loc[i,"close"],sharesHolding,balance,moneySpentOnAsset,feeBuyValue,0]
                logDataIndex +=1
                #END LOGGING
                if(verbose_mode == True):
                    print("Buy: ",sharesHolding," shares. New balance is: ",balance)
                    print("Buy fee taken out: ",feeBuyValue)
        elif(isHolding==True):
            if(ShouldTrade(data.loc[i,:],thresholds_sell,thresholds_sell_usage)):
                if(verbose_mode == True):
                    print("SELLING")
                    print(data.loc[i,:])
                isHolding = False
        
                
                balance = balance + sharesHolding*data.loc[i,"close"]
                #subtract fee
                feeSellValue = round(balance*feeSell,2)
                balance = round(balance-feeSellValue,2)
                if(verbose_mode == True):
                    print("Sell: ",sharesHolding,"shares. New balance is: ",balance)
                    print("Sell fee taken out: ",feeSellValue)
                sharesHolding = 0

                #START LOGGING
                logData.loc[logDataIndex]=[i,data.loc[i,"date"],"sell",data.loc[i,"close"],sharesHolding,balance,moneySpentOnAsset,feeSellValue,balance-moneySpentOnAsset]
                logDataIndex +=1
                #END LOGGING

    
    if(isHolding==True):
                if(verbose_mode == True):
                    print("Exit Sell: ",sharesHolding,"shares. New balance is: ",balance)
                isHolding = False
        
                
                balance = balance + sharesHolding*data.loc[i,"close"]
                #subtract fee
                feeSellValue = round(balance*feeSell,2)
                balance = round(balance-feeSellValue,2)
                if(verbose_mode == True):
                    print("Sell: ",sharesHolding,"shares. New balance is: ",balance)
                    print("Sell fee taken out: ",feeSellValue)
                sharesHolding = 0

                #START LOGGING
                logData.loc[logDataIndex]=[i,data.loc[i,"date"],"sell",data.loc[i,"close"],sharesHolding,balance,moneySpentOnAsset,feeSellValue,balance-moneySpentOnAsset]
                logDataIndex +=1

                #END LOGGING

    if(loggingEnabled and (len(logData)>0)):
        #print("Log Len: ",len(logData))
        import datetime
        dt = str(datetime.datetime.now())
        symb = file[11:14]
        logName = "LOG "+dt[0:19]+" "+symb+".csv"
        logName = logName.replace(":","-")
        #print("Saving log with name: ",logName)
        logData.to_csv("trade logs/"+logName,index=False)
    return balance


def ShouldTrade(values, thresholds,thresholds_usage):
    vals = values.as_matrix()[2:]
    usageCount = 0
    for i in range(0,len(vals)):
        if(thresholds_usage[i]==1):
            usageCount+=1
            if(thresholds[i]<vals.item(i)):
                return False        
        elif(thresholds_usage[i]==2):
            usageCount+=1
            if(thresholds[i]>vals.item(i)):
                return False
    #this will only trigger if every value in the usage array is 0 (ignore code)
    if(usageCount==0):
        return False
    return True    
    
def getStartPrice(filename):
    data = pd.read_csv(filename)
    return data.loc[0,"close"]

def getEndPrice(filename):
    data = pd.read_csv(filename)
    return data.loc[len(data)-1,"close"]
def getStartDate(filename):
    data = pd.read_csv(filename)
    return data.loc[0,"date"]
def getEndDate(filename):
    data = pd.read_csv(filename)
    return data.loc[len(data)-1,"date"]
def getNumberOfRows(filename):
    return len(pd.read_csv(filename))
