

import sys
usingCorrectVer = True
if(sys.version_info[0]!=3):
    #print("Please run this application with python 3, preferably 3.5.2.")
    usingCorrectVer = False


import tkinter as tk  
import pygubu
import pandas as pd

def getMarketDataFileNames():
    #this collects all file names that end with "marketdata.csv" in
    #the marketdata folder
    #print("getting market data")
    import glob
    import os
    os.chdir("marketdata")
    filenames = glob.glob("*marketdata.csv")
    os.chdir("..")
    return filenames
def getMarketDataIndex(self,filename):
    dataFiles = self.builder.get_object("dropdownData")['values']
    for i in range(0,len(dataFiles)):
        if(dataFiles[i]==filename):
            return i
    return -1
def openDirectory(directoryName):
    import os
    workingDirectory = os.getcwd()
    import subprocess
    directoryCommand = str("explorer "+workingDirectory+"\\"+ directoryName)
    subprocess.Popen(directoryCommand)

def saveStrategy(saveString,profPerDay):
    #print("preparing to save to file..")

    #print("Current save string: \n")
    #print(saveString)    

    import datetime
    dt = str(datetime.datetime.now())
    symb = saveString[0:3]
    saveName = "SAVE "+dt[0:19]+" "+symb+" "+profPerDay+" PER DAY.STRAT"
    saveName = saveName.replace(":","-")
    #print("Saving with name: ",saveName," ..")

    saveFile = open("saved strategies/"+saveName, "w")
    saveFile.write(saveString)
    saveFile.close()

def loadStrategy(self,dataset,buyT,buyU,sellT,sellU):
        
        self.builder.get_object("dropdownData").current(getMarketDataIndex(self,dataset))
        #set sliders and dropdowns
        self.builder.get_object("dropdownBuyMACD").current(buyU[0])
        self.builder.get_object("dropdownBuySTF").current(buyU[1])
        self.builder.get_object("dropdownBuySTS").current(buyU[2])
        self.builder.get_object("dropdownBuySTV").current(buyU[3])
        self.builder.get_object("dropdownBuySMI").current(buyU[4])
        self.builder.get_object("dropdownBuyRSI").current(buyU[5])
        self.builder.get_object("dropdownBuyDMI_DX").current(buyU[6])
        self.builder.get_object("dropdownBuyDMI_ADX").current(buyU[7])
        self.builder.get_object("dropdownSellMACD").current(sellU[0])
        self.builder.get_object("dropdownSellSTF").current(sellU[1])
        self.builder.get_object("dropdownSellSTS").current(sellU[2])
        self.builder.get_object("dropdownSellSTV").current(sellU[3])
        self.builder.get_object("dropdownSellSMI").current(sellU[4])
        self.builder.get_object("dropdownSellRSI").current(sellU[5])
        self.builder.get_object("dropdownSellDMI_DX").current(sellU[6])
        self.builder.get_object("dropdownSellDMI_ADX").current(sellU[7])
    
        
        
        self.builder.get_object("sliderBuyMACD").set(buyT[0])
        
        self.builder.get_object("sliderBuySTF").set(buyT[1])
        
        self.builder.get_object("sliderBuySTS").set(buyT[2])
        
        self.builder.get_object("sliderBuySTV").set(buyT[3])
        
        self.builder.get_object("sliderBuySMI").set(buyT[4])
        
        self.builder.get_object("sliderBuyRSI").set(buyT[5])
        
        self.builder.get_object("sliderBuyDMI_DX").set(buyT[6])
        
        self.builder.get_object("sliderBuyDMI_ADX").set(buyT[7])
        
        self.builder.get_object("sliderSellMACD").set(sellT[0])
        
        self.builder.get_object("sliderSellSTF").set(sellT[1])
        
        self.builder.get_object("sliderSellSTS").set(sellT[2])
        
        self.builder.get_object("sliderSellSTV").set(sellT[3])
        
        self.builder.get_object("sliderSellSMI").set(sellT[4])
        
        self.builder.get_object("sliderSellRSI").set(sellT[5])
        
        self.builder.get_object("sliderSellDMI_DX").set(sellT[6])
        
        self.builder.get_object("sliderSellDMI_ADX").set(sellT[7])
        #print("strat loaded")
            
        
        
    
    
def updateSliders(self):    
        selectedMarketdataFile = self.builder.get_object("dropdownData").get()
        selectedMetadataFile = selectedMarketdataFile[0:len(selectedMarketdataFile)-4]+"_metadata.csv"
        metadataDF = pd.read_csv("marketdata/"+selectedMetadataFile)        
        for i in range(0,len(minValues)):
            minValues[i] = int(metadataDF.loc[i+2,"min"])
            maxValues[i] = int(metadataDF.loc[i+2,"max"])
            
        self.builder.get_object("sliderBuyMACD")['from_']=minValues[0]
        self.builder.get_object("sliderBuyMACD")['to']=maxValues[0]
        self.builder.get_object("sliderBuySTF")['from_']=minValues[1]
        self.builder.get_object("sliderBuySTF")['to']=maxValues[1]
        self.builder.get_object("sliderBuySTS")['from_']=minValues[2]
        self.builder.get_object("sliderBuySTS")['to']=maxValues[2]
        self.builder.get_object("sliderBuySTV")['from_']=minValues[3]
        self.builder.get_object("sliderBuySTV")['to']=maxValues[3]
        self.builder.get_object("sliderBuySMI")['from_']=minValues[4]
        self.builder.get_object("sliderBuySMI")['to']=maxValues[4]
        self.builder.get_object("sliderBuyRSI")['from_']=minValues[5]
        self.builder.get_object("sliderBuyRSI")['to']=maxValues[5]
        self.builder.get_object("sliderBuyDMI_DX")['from_']=minValues[6]
        self.builder.get_object("sliderBuyDMI_DX")['to']=maxValues[6]
        self.builder.get_object("sliderBuyDMI_ADX")['from_']=minValues[7]
        self.builder.get_object("sliderBuyDMI_ADX")['to']=maxValues[7]
        self.builder.get_object("sliderSellMACD")['from_']=minValues[0]
        self.builder.get_object("sliderSellMACD")['to']=maxValues[0]
        self.builder.get_object("sliderSellSTF")['from_']=minValues[1]
        self.builder.get_object("sliderSellSTF")['to']=maxValues[1]
        self.builder.get_object("sliderSellSTS")['from_']=minValues[2]
        self.builder.get_object("sliderSellSTS")['to']=maxValues[2]
        self.builder.get_object("sliderSellSTV")['from_']=minValues[3]
        self.builder.get_object("sliderSellSTV")['to']=maxValues[3]
        self.builder.get_object("sliderSellSMI")['from_']=minValues[4]
        self.builder.get_object("sliderSellSMI")['to']=maxValues[4]
        self.builder.get_object("sliderSellRSI")['from_']=minValues[5]
        self.builder.get_object("sliderSellRSI")['to']=maxValues[5]
        self.builder.get_object("sliderSellDMI_DX")['from_']=minValues[6]
        self.builder.get_object("sliderSellDMI_DX")['to']=maxValues[6]
        self.builder.get_object("sliderSellDMI_ADX")['from_']=minValues[7]
        self.builder.get_object("sliderSellDMI_ADX")['to']=maxValues[7]

        #print("Slider Min and Max Values Have Been Updated:")
        #print(minValues)
        #print(maxValues)


class Interface:
    
    
        
    def __init__(self, master):      

        master.title("Capstone Project Spring 2018")
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('ui_layout.ui')
        self.mainwindow = builder.get_object('MainContainer', master)
        #connect call backs
        builder.connect_callbacks(self)
        
        #configure dropdown menu
        builder.get_object("dropdownData")['values'] = getMarketDataFileNames()

        #set initial values for all the drop menus on the ui
        builder.get_object("dropdownData").current(0)
        builder.get_object("dropdownBuyMACD").current(0)
        builder.get_object("dropdownBuySTF").current(0)
        builder.get_object("dropdownBuySTS").current(0)
        builder.get_object("dropdownBuySTV").current(0)
        builder.get_object("dropdownBuySMI").current(0)
        builder.get_object("dropdownBuyRSI").current(0)
        builder.get_object("dropdownBuyDMI_DX").current(0)
        builder.get_object("dropdownBuyDMI_ADX").current(0)
        builder.get_object("dropdownSellMACD").current(0)
        builder.get_object("dropdownSellSTF").current(0)
        builder.get_object("dropdownSellSTS").current(0)
        builder.get_object("dropdownSellSTV").current(0)
        builder.get_object("dropdownSellSMI").current(0)
        builder.get_object("dropdownSellRSI").current(0)
        builder.get_object("dropdownSellDMI_DX").current(0)
        builder.get_object("dropdownSellDMI_ADX").current(0)
        builder.get_object("dropdownEnableLogging").current(0)

        

        #update slider to first marketdata
        updateSliders(self)        
        
        

        
    
    # these functions are all attached to buttons on the ui
    # they are only triggered when their appropriate button has been pressed
    # START BUTTON CALLBACK FUNCTIONS
    def btnSaveStratPressed(self):
        self.btnTestPressed()#run strat to make sure all values reflect current parameters
        #print("Saving Strategy..")
        
        #collect the usage paramters for buying from the 7 dropdown s
        dropdownValueBuy[0]=self.builder.get_object("dropdownBuyMACD").get()
        dropdownValueBuy[1]=self.builder.get_object("dropdownBuySTF").get()
        dropdownValueBuy[2]=self.builder.get_object("dropdownBuySTS").get()
        dropdownValueBuy[3]=self.builder.get_object("dropdownBuySTV").get()
        dropdownValueBuy[4]=self.builder.get_object("dropdownBuySMI").get()
        dropdownValueBuy[5]=self.builder.get_object("dropdownBuyRSI").get()
        dropdownValueBuy[6]=self.builder.get_object("dropdownBuyDMI_DX").get()
        dropdownValueBuy[7]=self.builder.get_object("dropdownBuyDMI_ADX").get()
        
        #convert the dropdown value to a 0, 1, or 2 for ignore, less than,
        #and greater than respectively
        for i in range(0,len(dropdownValueBuy)):
            if(dropdownValueBuy[i]=="ignore"):
                dropdownValueBuy[i]=0
            elif(dropdownValueBuy[i]=="<"):
                dropdownValueBuy[i]=1
            elif(dropdownValueBuy[i]==">"):
                dropdownValueBuy[i]=2
            else:
                #print("INVALID USAGE VALUE: ",dropdownValueBuy[i])
                return

        #like above, collect sell usage paramters
        dropdownValueSell[0]=self.builder.get_object("dropdownSellMACD").get()
        dropdownValueSell[1]=self.builder.get_object("dropdownSellSTF").get()
        dropdownValueSell[2]=self.builder.get_object("dropdownSellSTS").get()
        dropdownValueSell[3]=self.builder.get_object("dropdownSellSTV").get()
        dropdownValueSell[4]=self.builder.get_object("dropdownSellSMI").get()
        dropdownValueSell[5]=self.builder.get_object("dropdownSellRSI").get()
        dropdownValueSell[6]=self.builder.get_object("dropdownSellDMI_DX").get()
        dropdownValueSell[7]=self.builder.get_object("dropdownSellDMI_ADX").get()

        #the sliders do not get collected here. they get updated each timer the user slides the slider
        #each time slider is being moved it calls the function sliderUpdate____ which can be found below

        
        #convert to 0, 1, or 2 like above
        for i in range(0,len(dropdownValueSell)):
            if(dropdownValueSell[i]=="ignore"):
                dropdownValueSell[i]=0
            elif(dropdownValueSell[i]=="<"):
                dropdownValueSell[i]=1
            elif(dropdownValueSell[i]==">"):
                dropdownValueSell[i]=2
            else:
                #print("INVALID USAGE VALUE: ",dropdownValueSell[i])
                return
        
        
        saveString =self.builder.get_object("dropdownData").get()
        profPerDay = self.builder.get_object("msgProfitPerDay")['text']
        saveString += ","+profPerDay
        for i in range(0,len(sliderValueBuy)):
            saveString += ","+str(sliderValueBuy[i])
        for i in range(0,len(dropdownValueBuy)):
            saveString += ","+str(dropdownValueBuy[i])
        for i in range(0,len(sliderValueSell)):
            saveString += ","+str(sliderValueSell[i])
        for i in range(0,len(dropdownValueSell)):
            saveString += ","+str(dropdownValueSell[i])
        
        
        saveStrategy(saveString,profPerDay)
        
        
    def btnLoadStratPressed(self):
        from tkinter.filedialog import askopenfilename
        #print("Loading Strategy..")
        import os
        savename = askopenfilename(initialdir=os.getcwd()+"/saved strategies",
                           filetypes =(("Strategies", "*.STRAT"),("All Files","*.*")),
                           title = "Choose a Strategy")
        #print (savename)
        try:
            with open(savename,'r') as savefile:
                
                saveData = savefile.read().split(",")
                #print(saveData)
                buyT = [0,0,0,0,0,0,0,0]
                sellT = [0,0,0,0,0,0,0,0]
                buyU = [0,0,0,0,0,0,0,0]
                sellU = [0,0,0,0,0,0,0,0]
                dataset = saveData[0]
                
                for i in range(0,len(buyT)):
                    buyT[i]= saveData[2+i]
                #print("buyT: ",buyT)
                for i in range(0,len(buyU)):
                    buyU[i]= saveData[10+i]
                #print("buyU: ",buyU)
                for i in range(0,len(sellT)):
                    sellT[i]= saveData[18+i]
                #print("sellT: ",sellT)
                for i in range(0,len(sellU)):
                    sellU[i]= saveData[26+i]
                #print("sellU: ",sellU)

                loadStrategy(self,dataset,buyT,buyU,sellT,buyU)
        except:
            print("No file selected or invalid file selected.")
    def btnUpdatePressed(self):        
        updateSliders(self)
    def btnRandomStratPressed(self):
        updateSliders(self)
        #print("min vals ",minValues)
        #print("max vals ",maxValues)
        import random
        dataset = self.builder.get_object("dropdownData").get()
        buyT = [0,0,0,0,0,0,0,0]
        sellT = [0,0,0,0,0,0,0,0]
        buyU = [0,0,0,0,0,0,0,0]
        sellU = [0,0,0,0,0,0,0,0]
        for i in range(0, len(minValues)):
            buyT[i] = random.randint(minValues[i],maxValues[i])
            buyU [i] = random.randint(0,2)
            sellT [i] = random.randint(minValues[i],maxValues[i])
            sellU[i] = random.randint(0,2)
        #print(dataset)
        #print(buyT)
        #print(buyU)
        #print(sellT)
        #print(sellU)

        loadStrategy(self,dataset,buyT,buyU,sellT,sellU)
        

    def btnResetStrategyPressed(self):
        #print("reset strat pressed")
        dataset = self.builder.get_object("dropdownData").get()
        buyT = [0,0,0,0,0,0,0,0]
        sellT = [0,0,0,0,0,0,0,0]
        buyU = [0,0,0,0,0,0,0,0]
        sellU = [0,0,0,0,0,0,0,0]
        loadStrategy(self,dataset,buyT,buyU,sellT,sellU)
        #print("reset strat")
    def btnTestPressed(self):
        updateSliders(self)#update the min and max of each slider for the currently selected market data
        
        #collect the usage paramters for buying from the 7 dropdown s
        dropdownValueBuy[0]=self.builder.get_object("dropdownBuyMACD").get()
        dropdownValueBuy[1]=self.builder.get_object("dropdownBuySTF").get()
        dropdownValueBuy[2]=self.builder.get_object("dropdownBuySTS").get()
        dropdownValueBuy[3]=self.builder.get_object("dropdownBuySTV").get()
        dropdownValueBuy[4]=self.builder.get_object("dropdownBuySMI").get()
        dropdownValueBuy[5]=self.builder.get_object("dropdownBuyRSI").get()
        dropdownValueBuy[6]=self.builder.get_object("dropdownBuyDMI_DX").get()
        dropdownValueBuy[7]=self.builder.get_object("dropdownBuyDMI_ADX").get()
        
        #convert the dropdown value to a 0, 1, or 2 for ignore, less than,
        #and greater than respectively
        for i in range(0,len(dropdownValueBuy)):
            if(dropdownValueBuy[i]=="ignore"):
                dropdownValueBuy[i]=0
            elif(dropdownValueBuy[i]=="<"):
                dropdownValueBuy[i]=1
            elif(dropdownValueBuy[i]==">"):
                dropdownValueBuy[i]=2
            else:
                #print("INVALID USAGE VALUE: ",dropdownValueBuy[i])
                return

        #like above, collect sell usage paramters
        dropdownValueSell[0]=self.builder.get_object("dropdownSellMACD").get()
        dropdownValueSell[1]=self.builder.get_object("dropdownSellSTF").get()
        dropdownValueSell[2]=self.builder.get_object("dropdownSellSTS").get()
        dropdownValueSell[3]=self.builder.get_object("dropdownSellSTV").get()
        dropdownValueSell[4]=self.builder.get_object("dropdownSellSMI").get()
        dropdownValueSell[5]=self.builder.get_object("dropdownSellRSI").get()
        dropdownValueSell[6]=self.builder.get_object("dropdownSellDMI_DX").get()
        dropdownValueSell[7]=self.builder.get_object("dropdownSellDMI_ADX").get()

        #the sliders do not get collected here. they get updated each timer the user slides the slider
        #each time slider is being moved it calls the function sliderUpdate____ which can be found below

        
        #convert to 0, 1, or 2 like above
        for i in range(0,len(dropdownValueSell)):
            if(dropdownValueSell[i]=="ignore"):
                dropdownValueSell[i]=0
            elif(dropdownValueSell[i]=="<"):
                dropdownValueSell[i]=1
            elif(dropdownValueSell[i]==">"):
                dropdownValueSell[i]=2
            else:
                #print("INVALID USAGE VALUE: ",dropdownValueSell[i])
                return
        
        #at this point, collecting the trading strategy from the UI
        #is now complete. We can begin testing the strategy using
        #my backtesting engine: "backtest.py" in main directory 

        
        ##print strategy so i can see if it's indeed correct
        #print("Buy Usage: ",dropdownValueBuy)
        #print("Buy Threshold: ",sliderValueBuy)
        #print("Sell Usage: ",dropdownValueSell)
        #print("Sell Threshold: ", sliderValueSell)

        #import backtest.py 
        import backtest

        #get the selected file name from the marketdata drop down so
        #we know which file to test on.
        selectedMarketdataFile = self.builder.get_object("dropdownData").get()

        #debug info so i know what is being passed in to the backtest
        #print("Marketdata File=",selectedMarketdataFile)    
        #print(initialBalance)
        #print(sliderValueBuy)
        #print(dropdownValueBuy)        
        #print(sliderValueSell)
        #print(dropdownValueSell)

        startingBalance = 0
        #test strategy (it returns the value of the users new balance after the test)
        try:
            startingBalance = float(self.builder.get_object("txtBalance").get())
            feeBuy = float(self.builder.get_object("txtSetBuyFee").get())
            feeSell = float(self.builder.get_object("txtSetSellFee").get())
            if(feeBuy<0):
                feeBuy = .3
                #print("FEE CANNOT BE A NEGATIVE VALUE")
            if(feeSell<0):
                feeSell =.3
                #print("FEE CANNOT BE A NEGATIVE VALUE")
        except:
            feeBuy = .3
            feeSell = .3
            #print("invalid value entered for balance, buy fee, and/or sell fee")
            self.builder.get_object("txtBalance")['text']= ""
            self.builder.get_object("txtSetBuyFee")['text']= ""
            self.builder.get_object("txtSetSellFee")['text']= ""
            startingBalance = 1000
        #print("start bal__",startingBalance)

        
        isLoggingEnabled = self.builder.get_object("dropdownEnableLogging").get()=="True"
        newBalance = backtest.testStrategy(str("marketdata/"+selectedMarketdataFile),False,isLoggingEnabled,feeBuy/100,feeSell/100,startingBalance,sliderValueBuy,dropdownValueBuy,sliderValueSell,dropdownValueSell)
        
        
          
        #calculate profit and show
        profit = newBalance - startingBalance
        #print("--- PROFIT= ",profit)
        #send results to UI
        self.builder.get_object("msgResultsChosenMarketData")['text'] = selectedMarketdataFile
        self.builder.get_object("msgResultsStartBalance")['text'] = str("$"+str(startingBalance))
        self.builder.get_object("msgResultsFinalBalance")['text'] = str("$"+str(round(newBalance,2)))        
        self.builder.get_object("msgResultsProfit")['text']=str("$"+str(round(profit,2)))
        if(profit>0):
            self.builder.get_object("msgResultsProfit")['background']="green"
        elif(profit<0):
            self.builder.get_object("msgResultsProfit")['background']="#ff484d"
        else:
            self.builder.get_object("msgResultsProfit")['background']="white"

        numberOfRows = backtest.getNumberOfRows(str("marketdata/"+selectedMarketdataFile))
        self.builder.get_object("msgRowsInData")['text']=str(numberOfRows)
        marketStartPrice = backtest.getStartPrice(str("marketdata/"+selectedMarketdataFile))
        marketEndPrice = backtest.getEndPrice(str("marketdata/"+selectedMarketdataFile))
        marketChangeInPrice = round(marketEndPrice - marketStartPrice,2)
        percProfit = round(profit / startingBalance*100,2)
        percMarket = round(marketEndPrice / marketStartPrice * 100,2)
        marketStartDate = backtest.getStartDate((str("marketdata/"+selectedMarketdataFile)))
        marketEndDate = backtest.getEndDate((str("marketdata/"+selectedMarketdataFile)))
        profitPerDay = round(profit / numberOfRows,2)
        #print("market % chg: ",percMarket)
        #print("market start: ",marketStartPrice)
        #print("market end:   ",marketEndPrice)
        #print("profit per day: ",profitPerDay)
        #print("profit: ",profit)
        #print("num days: ",numberOfRows)
        self.builder.get_object("msgProfitPercentChange")['text']= str(percProfit)+"%"
        self.builder.get_object("msgMarketPercentChange")['text']= str(percMarket)+"%"
        self.builder.get_object("msgMarketChangeInPrice")['text']="$"+str(marketChangeInPrice)
        self.builder.get_object("msgMarketStartPrice")['text']= "$"+str(marketStartPrice)
        self.builder.get_object("msgMarketEndPrice")['text']= "$"+str(marketEndPrice)
        
        self.builder.get_object("msgProfitPerDay")['text']= "$"+str(profitPerDay)
        self.builder.get_object("msgDateRange")['text']= str("From: "+str(marketStartDate)+"\nTo:   "+str(marketEndDate))
    def sliderUpdateBuy0(self,x):
        sliderValueBuy[0] = self.builder.get_variable("sliderBuyval0")
        sliderValueBuy[0] = int(sliderValueBuy[0].get())
        self.builder.get_object("displayBuyMACD")['text']=sliderValueBuy[0]        
    def sliderUpdateBuy1(self,x):
        sliderValueBuy[1] = self.builder.get_variable("sliderBuyval1")
        sliderValueBuy[1] = int(sliderValueBuy[1].get())
        self.builder.get_object("displayBuySTF")['text']=sliderValueBuy[1]
    def sliderUpdateBuy2(self,x):
        sliderValueBuy[2] = self.builder.get_variable("sliderBuyval2")
        sliderValueBuy[2] = int(sliderValueBuy[2].get())
        self.builder.get_object("displayBuySTS")['text']=sliderValueBuy[2]
    def sliderUpdateBuy3(self,x):
        sliderValueBuy[3] = self.builder.get_variable("sliderBuyval3")
        sliderValueBuy[3] = int(sliderValueBuy[3].get())
        self.builder.get_object("displayBuySTV")['text']=sliderValueBuy[3]
    def sliderUpdateBuy4(self,x):
        sliderValueBuy[4] = self.builder.get_variable("sliderBuyval4")
        sliderValueBuy[4] = int(sliderValueBuy[4].get())
        self.builder.get_object("displayBuySMI")['text']=sliderValueBuy[4]
    def sliderUpdateBuy5(self,x):
        sliderValueBuy[5] = self.builder.get_variable("sliderBuyval5")
        sliderValueBuy[5] = int(sliderValueBuy[5].get())
        self.builder.get_object("displayBuyRSI")['text']=sliderValueBuy[5]
    def sliderUpdateBuy6(self,x):
        sliderValueBuy[6] = self.builder.get_variable("sliderBuyval6")
        sliderValueBuy[6] = int(sliderValueBuy[6].get())
        self.builder.get_object("displayBuyDMI_DX")['text']=sliderValueBuy[6]
    def sliderUpdateBuy7(self,x):
        sliderValueBuy[7] = self.builder.get_variable("sliderBuyval7")
        sliderValueBuy[7] = int(sliderValueBuy[7].get())
        self.builder.get_object("displayBuyDMI_ADX")['text']=sliderValueBuy[7]
    def sliderUpdateSell0(self,x):
        sliderValueSell[0] = self.builder.get_variable("sliderSellval0")
        sliderValueSell[0] = int(sliderValueSell[0].get())
        self.builder.get_object("displaySellMACD")['text']=sliderValueSell[0]
    def sliderUpdateSell1(self,x):
        sliderValueSell[1] = self.builder.get_variable("sliderSellval1")
        sliderValueSell[1] = int(sliderValueSell[1].get())
        self.builder.get_object("displaySellSTF")['text']=sliderValueSell[1]
    def sliderUpdateSell2(self,x):
        sliderValueSell[2] = self.builder.get_variable("sliderSellval2")
        sliderValueSell[2] = int(sliderValueSell[2].get())
        self.builder.get_object("displaySellSTS")['text']=sliderValueSell[2]
    def sliderUpdateSell3(self,x):
        sliderValueSell[3] = self.builder.get_variable("sliderSellval3")
        sliderValueSell[3] = int(sliderValueSell[3].get())
        self.builder.get_object("displaySellSTV")['text']=sliderValueSell[3]
    def sliderUpdateSell4(self,x):
        sliderValueSell[4] = self.builder.get_variable("sliderSellval4")
        sliderValueSell[4] = int(sliderValueSell[4].get())
        self.builder.get_object("displaySellSMI")['text']=sliderValueSell[4]
    def sliderUpdateSell5(self,x):
        sliderValueSell[5] = self.builder.get_variable("sliderSellval5")
        sliderValueSell[5] = int(sliderValueSell[5].get())
        self.builder.get_object("displaySellRSI")['text']=sliderValueSell[5]
    def sliderUpdateSell6(self,x):
        sliderValueSell[6] = self.builder.get_variable("sliderSellval6")
        sliderValueSell[6] = int(sliderValueSell[6].get())
        self.builder.get_object("displaySellDMI_DX")['text']=sliderValueSell[6]
    def sliderUpdateSell7(self,x):
        sliderValueSell[7] = self.builder.get_variable("sliderSellval7")
        sliderValueSell[7] = int(sliderValueSell[7].get())
        self.builder.get_object("displaySellDMI_ADX")['text']=sliderValueSell[7]
    def btnViewMainPressed(self):
        openDirectory("")
    def btnViewDatasetsPressed(self):
        openDirectory("datasets")
    def btnViewMarketDataPressed(self):
        openDirectory("marketdata")
    def btnViewTradeLogsPressed(self):
        openDirectory("trade logs")
    #END BUTTON CALLBACK FUNCTIONS

if(usingCorrectVer):
    #set some initial values for the paramters
    minValues = [0,0,0,0,0,0,0,0]
    maxValues = [100,100,100,100,100,100,100,100]
    sliderValueBuy = [0,0,0,0,0,0,0,0]
    dropdownValueBuy = [0,0,0,0,0,0,0,0]
    sliderValueSell = [0,0,0,0,0,0,0,0]
    dropdownValueSell = [0,0,0,0,0,0,0,0]

    initialBalance = 1000
    profit = 0

    #start the ui
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()





