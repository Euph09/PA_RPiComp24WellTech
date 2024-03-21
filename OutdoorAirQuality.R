library(conflicted)
conflicted::conflicts_prefer(dplyr::filter)

library(openair)
library(tidyverse)
library(stringi)

#Access DEFRA AURN data
aurn_meta <- importMeta(source = "aurn", all = TRUE) #Import site data for aurn network

#Filter sites by those that are currently measuring PM10, and are in a Rural Background
pm10_sites <- filter(aurn_meta, 
                     variable == "PM10",
                     end_date =="ongoing",
                     site_type=="Rural Background") # Search for pm10 sites with ongoing action with rural background


site <- importAURN(site = "HM", data_type = "24_hour", year = 2024) # Import data for specific site

site<-site[rev(order(as.Date(site$date, format="%m/%d/%Y "))),] # Sort site data by most recent


#Assign variables values for most recent PM2.5 an PM10
pm25 <-site[1,6]
pm10 <-site[1,5]

day <- format(Sys.time(), "%Y-%m-%d %H:00:00")

if(nchar(mday(day)-1) <2){
  yesterday <-paste("0",mday(day)-1, sep="")
}else{
  yesterday <-mday(day)-1
}
stri_sub(day,9,10)<-yesterday

entry<-filter(site,
              date==day)

pm25 <-entry[1,6]
pm10<-entry[1,5]
print(paste(pm25, pm10, sep=","))
