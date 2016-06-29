############################
# Libraries                #
############################ 
library(recommenderlab)
library(rjson)


############################
# Data                     #
############################ 
# Loading data model
load("model.RData")
to_predict_score = matrix(c(1, NA, NA, NA, 3, NA, NA, NA, 4, 5), nrow=1, ncol=10)
to_predict_score = as(to_predict_score, "realRatingMatrix")


############################
#  User Based Similarity   #
############################ 
# Predictions
recom_user <- predict(recom, to_predict_score, n=3)

# JSON
json <- toJSON(as(recom_user, "list"))

# Save JSON file
write(json, file = "recom_user.json")
