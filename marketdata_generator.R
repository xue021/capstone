asset_name = "ETH"
#------ You should not need to edit anything below this point
#------ marketdata file and its metadata can be found in the marketdata folder
source_data = read.csv("datasets/CRYPTO SOURCE DATA.csv")
source_data = source_data[which(source_data$symbol==asset_name),]

path = paste("datasets/",asset_name,".csv",sep="")
output_marketdata_path = paste("marketdata/",asset_name,"_marketdata.csv",sep="")
output_metadata_marketdata_path = paste("marketdata/",asset_name,"_marketdata_metadata.csv",sep="")

data = data.frame(source_data$date,source_data$open,source_data$high,source_data$low,source_data$close,source_data$volume)
colnames(data) = c("Date","Open","High","Low","Close","Volume")

data$Date = as.Date(data$Date)
data$Close = as.numeric(data$Close)
data$High = as.numeric(data$High)
data$Low = as.numeric(data$Low)
data$Volume = as.numeric(data$Volume)
hlc = data.frame(data$High,data$Low,data$Close)

library("TTR")
data$sma10 = SMA(x = data$Close,n=10)
data$sma20 = SMA(x = data$Close,n=20)

macd = MACD(x=data$Close, nFast = 5, nSlow = 26, nSig = 20, percent = TRUE)
data$macd = macd[,1]



stoch_14_3_3 = stoch(HLC=data$Close, nFastK = 14, nFastD = 3, nSlowD = 3, bounded = TRUE,smooth = 1)
data$stochfast = stoch_14_3_3[,1]*100
data$stochslow = stoch_14_3_3[,3]*100

smi_13_2_25 = SMI(HLC=hlc, n = 13, nFast = 2, nSlow = 25, nSig = 9, bounded = TRUE,smooth = 1)
data$smi = smi_13_2_25[,1]

stoch_volume = stoch(HLC=data$Volume, nFastK = 14, nFastD = 3, nSlowD = 3, bounded = TRUE,smooth = 1)
data$stoch_volume = stoch_volume[,1]*100

rsi = RSI(data$Close)
data$rsi = rsi

adx = ADX(hlc)
data$adx_DX = adx[,3]
data$adx_ADX = adx[,4]


# format data for out put in df
outputdata = data.frame(data$Date,data$Close,data$macd,data$stochfast,data$stochslow,data$stoch_volume,data$smi,data$rsi,data$adx_DX,data$adx_ADX)
outputdata = outputdata[complete.cases(outputdata),]#remove rows that have any NAs
colnames(outputdata)=c("date","close","macd","stochfast","stochslow","stoch_volume","smi","rsi","dmi_dx","dmi_adx")#change colnames
write.csv(outputdata,output_marketdata_path,row.names = FALSE)# write to csv file

#create meta data that stores min and max value of each column in output data so we know the range of values we can choose from
metadata = data.frame(colnames(outputdata))
colnames(metadata)="column"
metadata$max = -1
metadata$min = 1

for(i in 1:nrow(metadata)){
  metadata$max[i] = max(outputdata[,i])
  
}
for(i in 1:nrow(metadata)){
  metadata$min[i] = min(outputdata[,i])
  
}
for(i in 1:nrow(metadata)){
  metadata$datatype[i] = class(outputdata[,i])
  
}
write.csv(metadata,output_metadata_marketdata_path,row.names = FALSE)