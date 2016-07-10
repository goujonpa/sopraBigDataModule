############################
# Libraries                #
############################ 
library(recommenderlab)
library(rjson)


############################
# Data                     #
############################ 
# Generating matrix
data <- matrix(
  sample(
    c(as.numeric(0:5), NA), 
    1000000,
    replace=TRUE,
    prob=c(rep(.4/6,6),.6)
  ), 
  ncol=100,
  dimnames=list(user=paste("u", 1:10000, sep=''), item=paste("i", 1:100, sep=''))
)

# Real rating matrix
r_data <- as(data, "realRatingMatrix")


############################
#  User Based Similarity   #
############################ 

# Recommender
recommender_model <- Recommender(r_data, method = "UBCF")

# Save model
save(recommender_model, file = "./RLib/rdata/recommender_model.RData")
