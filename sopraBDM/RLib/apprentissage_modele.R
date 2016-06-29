############################
# Libraries                #
############################ 
library(recommenderlab)
library(rjson)


############################
# Data                     #
############################ 
# Generating matrix
data <- matrix(sample(c(as.numeric(0:5), NA), 50,
            replace=TRUE, prob=c(rep(.4/6,6),.6)), ncol=10,
            dimnames=list(user=paste("u", 1:5, sep=''),
            item=paste("i", 1:10, sep='')))

# Real rating matrix
r_app <- as(data, "realRatingMatrix")


############################
#  User Based Similarity   #
############################ 

# Recommender
recom <- Recommender(r_app, method = "UBCF")

# Save model
save(recom, file = "model.RData")