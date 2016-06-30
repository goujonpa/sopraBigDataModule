############################
# Libraries                #
############################ 
library(recommenderlab)
library(rjson)

############################
# Data                     #
############################ 
# Loading data model
load("recommender_model.RData")

# get the notation of the user
notations_matrix = fromJSON(file="employee_predict_in.json")
notations_matrix = do.call(rbind, notations_matrix)

# get the user matrix
user_matrix = matrix(NA, nrow=1, ncol=dim(getModel(recom)$data)[2])


for (i in 1:nrow(notations_matrix)) {
  user_matrix[1, notations_matrix[i,2]] = notations_matrix[i,3]
}

user_rating_matrix = as(user_matrix, "realRatingMatrix")


############################
#  User Based Similarity   #
############################ 
# Predictions
user_prediction <- predict(recommender_model, user_rating_matrix, n=10)

# JSON
json <- toJSON(as(user_prediction, "list"))

# Save JSON file
write(json, file = "employee_predict_out.json")
