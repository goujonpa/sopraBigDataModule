# Paul GOUJON & Alexandre LACOUR
# UTC - TX Sopra Steria & Big Data

# Train dataset for collaborative filetering generation

# Generating matrix

items_number = 100;
users_number = 10000;
na_proportion = .6;
json_export = T;


others_propotion = 1 - na_proportion;
dataset_matrix <- matrix(
  sample(
    c(as.numeric(0:5), NA), 
    (items_number * users_number),
    replace=TRUE,
    prob=c(rep(others_propotion/6,6), na_proportion)
  ), 
  ncol=items_number,
  dimnames=list(
    user=paste("u", 1:users_number, sep=''), 
    item=paste("i", 1:items_number, sep='')
  )
)

if (json_export) {
  library(rjson);
  s = toJSON(dataset_matrix);
  write(s, paste("UBCF_dataset_", items_number, "i_", users_number, "u_", na_proportion, "naprop.json", sep=''));
}
