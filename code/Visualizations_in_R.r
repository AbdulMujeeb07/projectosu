# Clear the Environment
rm(list=ls())

library(dplyr)
library(tidyr)
library(ggplot2)
library(extrafont)
library(reshape2)


###################################
# - Read in data set
###################################

data = read.csv("C:/Users/vwbus/OneDrive - Oklahoma A and M System/Documents/GitHub/project-deliverable-2-red-hot-stilly-peppers/data/Cleaned_Data_dv_2.csv", header = T)


ggplot(data=data,aes(x=Beds,y=Cost.Per.Person,group=Beds))+
  ggtitle('Cost (per Person) by Number of Beds',subtitle = 'As you bring in more Roomates, How much should you expect to save?') +
  labs(x="Number of Beds in the Apartment/House",y='Cost Per Person')+
  geom_boxplot(outlier.color = 'red', outlier.shape=7,
               outlier.size=4)+
  theme(
    plot.title = element_text(size = 14, face="bold"),
    axis.title.x = element_text(size = 12, face = "bold"),
    axis.title.y = element_text(size = 12, face = "bold")
  )+
  scale_y_continuous(limits=c(NA,1200),n.breaks=9,labels=scales::dollar_format())


library(plotly)


fig2 <- plot_ly(data, x = ~Time.taken.by.walk, y = ~Time.taken.by.car, z = ~Cost.Per.Person)
fig2 <- fig2 %>% add_markers()
fig2 <- fig2 %>% layout(scene = list(xaxis = list(title = 'Walk time to the Library'),
                                   yaxis = list(title = 'Drive time to the Library'),
                                   zaxis = list(title = 'Cost Per Person')))

fig2

data$Number.of.Amenities=count.fields(textConnection(data$Amenities), sep = ",")

ggplot(data=data,aes(x=Number.of.Amenities,y=Cost.Per.Person))+
  ggtitle('Number of Amenities in the Ad vs Cost (Per Person)',subtitle = 'It seems the number of amenities is based more on the quality of the advertisment, and less on the overall quality of the apartment.') +
  labs(x="Number of Amenities",y='Cost Per Person')+
  geom_point()+
  scale_y_continuous(limits=c(NA,1200),n.breaks=9,labels=scales::dollar_format())

