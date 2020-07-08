library(magrittr)
library(dplyr)

sex <- c("M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M", "F")
stage <- c("I", "II", "II", "I", "II", "II", "I", "II", "II", "I", "II", "II")
treatment <- c("A", "A", "A", "A", "B", "B", "B", "B", "P", "P", "P", "P")
myc <- c(2343, 457, 4593, 9035, 3450, 3524, 958, 1053, 8674, 3424, 463, 5105)

meta <- data.frame(sex, stage, treatment, myc) #creates the data frame with data.frame(columns)

row.names(meta) <- paste("sample",1:12,sep="")

meta[]

##return only the treatment and sex columns using []:
meta[c(1,3)]

# return the treatment values for samples 5, 7, 9, and 10 using []:
meta[c(5,7,9,10),3]

##use filter() to return all data for those samples receiving treatment P:
filter(meta, treatment=='P')

# use filter()/select()to return only the stage and treatment columns for those samples with myc > 5000:
filter(meta , myc > 5000)

# remove the treatment column from the dataset using []:
df = meta[-3]

df[]

# remove samples 7, 8 and 9 from the dataset using []:
sen = meta[-c(7,8,9),]

sen[]

# keep only samples 1-6 using []:
keep = meta[c(1:6),]

keep[]

# add a column called pre_treatment to the beginning of the 
# dataframe with the values T, F, F, F, T, T, F, T, F, F, T, T (Hint: use cbind()):
##assign pre_treatment
pre_treatment <- c('T','F','F','F','T','T','F', 'T', 'F', 'F', 'T', 'T')
##bind it
cbind(pre_treatment,meta)

# change the names of the columns to: “A”, “B”, “C”, “D”:
colnames(meta) <- c("A", "B", "C", "D")

meta[]


