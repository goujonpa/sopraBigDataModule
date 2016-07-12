# Paul GOUJON & Alexandre LACOUR
# UTC - TX - Sopra Steria & Big Data

# This script outputs a recommendation using the recommender model previously learned

# LIBS
library(recommenderlab)
library(rjson)

# DATA
# Loading data model
load("./RLib/rdata/recommender_model.RData")

# get the notation of the user
notations_matrix = fromJSON(file="./RLib/json/employee_predict_in.json")
notations_matrix = do.call(rbind, notations_matrix)

# get the asked predictions number
predictions_number = as.numeric(fromJSON(file="./RLib/json/predictions_number.json"))

# get the user matrix
user_matrix = matrix(NA, nrow=1, ncol=dim(getModel(recommender_model)$data)[2])

for (i in 1:nrow(notations_matrix)) {
  user_matrix[1, notations_matrix[i,2]] = notations_matrix[i,3]
}

user_rating_matrix = as(user_matrix, "realRatingMatrix")

# PREDICTION using UBCF (User Based Collaborative Filtering)
# Predictions
user_prediction <- predict(recommender_model, user_rating_matrix, n=predictions_number)

# EXPORT

# json cast
json <- toJSON(as(user_prediction, "list"))

# write to file
write(json, file = "./RLib/json/employee_predict_out.json")
