library(conflicted)
conflicted::conflicts_prefer(dplyr::filter)

library(openair)
library(tidyverse)
library(stringi)

aurn_meta <- importMeta(source = "aurn", all = TRUE) #Import site data for aurn network

pm10_sites <- filter(aurn_meta, 
                     variable == "PM10",
                     end_date =="ongoing",
                     site_type=="Rural Background") # Search for pm10 sites with ongoing action with rural background

site <- importAURN(site = "HM", data_type = "24_hour", year = 2024) # Import data for specific site

site<-site[rev(order(as.Date(site$date, format="%m/%d/%Y "))),] # Sort site data by most recent

#Searches for most recent data, at same time as currently, where there is data

day <- format(Sys.time(), "%Y-%m-%d %H:00:00")

found = FALSE;
i<-1
while(found == FALSE){
  if(nchar(mday(day)-1) <2){
    yesterday <-paste("0",mday(day)-i, sep="")
  }else{
    yesterday <-mday(day)-i
  }
  stri_sub(day,9,10)<-yesterday
  
  entry<-filter(site,
                date==day)
  pm25 <-entry[1,6]
  pm10<-entry[1,5]
  
  
  if(is.na(pm25)||is.na(pm10)){
    found = FALSE
  }else{
    found = TRUE
  }
  i<-i+1
}
  
print(paste(pm25, pm10, sep=","))
