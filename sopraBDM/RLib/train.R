# Paul GOUJON & Alexandre LACOUR
# UTC - TX - Sopra & Big Data

# LIBS
library(rjson)
library(recommenderlab)
library(tools)

# DATA
# Get the counts
counts = fromJSON(file="./json/train_counts_in.json")

# instanciate a matrix
ratings_matrix = matrix(NA, nrow=counts$employees, ncol=counts$widgets)

# Get notations
notations = fromJSON(file="./json/train_employee_widget_in.json")
notations = do.call(rbind, notations)
# We get the notations with the format [employee, widget, notation] for each line

for (i in 1:nrow(notations)) {
  ratings_matrix[notations[i, 1], notations[i, 2]] = notations[i, 3]
}


