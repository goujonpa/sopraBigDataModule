# Paul GOUJON & Alexandre LACOUR
# UTC - TX - Sopra Steria & Big Data

# LIBS
library(recommenderlab)
library(rjson)

# DATA
# Get the counts
counts = fromJSON(file="./RLib/json/train_counts_in.json")

# instanciate a matrix
ratings_matrix = matrix(NA, nrow=counts$employees, ncol=counts$widgets)

# Get notations
notations = fromJSON(file="./RLib/json/train_employee_widget_in.json")
notations = do.call(rbind, notations)
# We get the notations with the format [employee, widget, notation] for each line

for (i in 1:nrow(notations)) {
  ratings_matrix[notations[i, 1], notations[i, 2]] = notations[i, 3]
}

# Real rating matrix
r_data <- as(ratings_matrix, "realRatingMatrix")


# RECOMMENDER
# We learn a User Based Recommender

# Recommender
recommender_model <- Recommender(r_data, method = "UBCF")

# Save model
save(recommender_model, file = "./RLib/rdata/recommender_model.RData")
