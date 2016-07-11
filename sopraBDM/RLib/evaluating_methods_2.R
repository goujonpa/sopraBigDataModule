# Paul GOUJON & Alexandre LACOUR
# UTC - TX - Sopra Steria & Big Data

# In this script, we try to evaluate the performances of our recommender system 
# using two different Recommender methods :
# - UBCF : User Based Collaborative Filtering
# - 

# LIBS

library(recommenderlab)
library(rjson)
library(ggplot2)
library(devtools)

# DATA

# Generating data
data(MovieLense)

# Keep relevant data
ratings_movies <- MovieLense[rowCounts(MovieLense) > 50, colCounts(MovieLense) > 100]
## 560 x 332 rating matrix of class 'realRatingMatrix' with 55298 ratings.

# MODEL EVALUATION - RATINGS

# 10 folds cross validation
n_fold <- 10

# It's better that the "items_to_keep" parameter is lower than the minimum number of items purchased by any user so 
# that we don't have users without items to test the models
# Number of item to keep has to be lower than : min(rowCounts(r_app))

# > min(rowCounts(ratings_movies))
# [1] 18
items_to_keep <- 15   

# Evaluating a model consists of comparing the recommendations with the unknown purchases. The ratings are between 1 
# and 5, and we need to define what constitutes good and bad items. For this purpose, we will define a threshold with 
# the minimum rating that is considered good
rating_threshold <- 3 
eval_sets <- evaluationScheme(data = ratings_movies, 
                              method = "cross-validation", 
                              k = n_fold, 
                              given = items_to_keep, 
                              goodRating = rating_threshold)
# > eval_sets
# Evaluation scheme with 15 items given
# Method: ‘cross-validation’ with 10 run(s).
# Good ratings: >=3.000000
# Data set: 560 x 332 rating matrix of class ‘realRatingMatrix’ with 55298 ratings.


# To count how many items in each set 
size_sets <- sapply(eval_sets@runsTrain, length)
# 504 in each set

# Evaluation of a method : UBCF
ubcf_eval_recommender <- Recommender(data = getData(eval_sets, "train"), 
                                     method = "UBCF", 
                                     parameter = NULL)

# Evaluation of a method : SVD
svd_eval_recommender <- Recommender(data = getData(eval_sets, "train"), 
                                     method = "SVD", 
                                     parameter = NULL)

# Predicted ratings
items_to_recommend = 10
ubcf_eval_prediction <- predict(object = ubcf_eval_recommender, 
                                newdata = getData(eval_sets, "known"), 
                                n = items_to_recommend, 
                                type = "ratings") 

items_to_recommend = 10
svd_eval_prediction <- predict(object = svd_eval_recommender, 
                                newdata = getData(eval_sets, "known"), 
                                n = items_to_recommend, 
                                type = "ratings") 

# Measures about each user, compute Root mean square error (RMSE), Mean squared error (MSE) and Mean absolute error (MAE)
ubcf_eval_accuracy <- calcPredictionAccuracy(x = ubcf_eval_prediction, 
                                             data = getData(eval_sets, "unknown"), 
                                             byUser = TRUE)

svd_eval_accuracy <- calcPredictionAccuracy(x = svd_eval_prediction, 
                                             data = getData(eval_sets, "unknown"), 
                                             byUser = TRUE)


apply(ubcf_eval_accuracy, 2, mean)
# > apply(ubcf_eval_accuracy, 2, mean)
# RMSE       MSE       MAE 
# 0.9162346 0.8737574 0.7293243 

apply(svd_eval_accuracy, 2, mean)
# > apply(svd_eval_accuracy, 2, mean)
# RMSE       MSE       MAE 
# 0.9461154 0.9312675 0.7622858 

# TOP N RECOMMENDERS EVALUATIONS
n_recommendations <- c(1, 3, 5, 10)

ubcf_res <- evaluate(eval_sets, method="UBCF", type="topNList", n=n_recommendations)
# > ubcf_res <- evaluate(eval_sets, method="UBCF", type="topNList", n=n_recommendations)
# UBCF run fold/sample [model time/prediction time]
# 1  [0.007sec/0.14sec] 
# 2  [0.006sec/0.142sec] 
# 3  [0.006sec/0.135sec] 
# 4  [0.018sec/0.131sec] 
# 5  [0.007sec/0.149sec] 
# 6  [0.006sec/0.131sec] 
# 7  [0.006sec/0.122sec] 
# 8  [0.006sec/0.14sec] 
# 9  [0.006sec/0.126sec] 
# 10  [0.006sec/0.126sec] 

svd_res <- evaluate(eval_sets, method="SVD", type="topNList", n=n_recommendations)
# > svd_res <- evaluate(eval_sets, method="SVD", type="topNList", n=n_recommendations)
# SVD run fold/sample [model time/prediction time]
# 1  [0.106sec/0.029sec] 
# 2  [0.123sec/0.043sec] 
# 3  [0.11sec/0.027sec] 
# 4  [0.112sec/0.033sec] 
# 5  [0.121sec/0.027sec] 
# 6  [0.095sec/0.026sec] 
# 7  [0.107sec/0.025sec] 
# 8  [0.087sec/0.025sec] 
# 9  [0.086sec/0.025sec] 
# 10  [0.092sec/0.026sec] 

avg(ubcf_res)
#> avg(ubcf_res)
# TP       FP       FN       TN precision     recall        TPR         FPR
# 1  0.700000 0.300000 72.46607 243.5339 0.7000000 0.01257710 0.01257710 0.001150343
# 3  1.950000 1.050000 71.21607 242.7839 0.6500000 0.03336490 0.03336490 0.004011253
# 5  3.039286 1.960714 70.12679 241.8732 0.6078571 0.05114569 0.05114569 0.007567253
# 10 5.367857 4.632143 67.79821 239.2018 0.5367857 0.08612002 0.08612002 0.018018548

avg(svd_res)
# > avg(svd_res)
# TP        FP       FN       TN precision     recall        TPR         FPR
# 1  0.6017857 0.3982143 72.56429 243.4357 0.6017857 0.01050422 0.01050422 0.001550348
# 3  1.5910714 1.4089286 71.57500 242.4250 0.5303571 0.02594005 0.02594005 0.005533374
# 5  2.4446429 2.5553571 70.72143 241.2786 0.4889286 0.03832720 0.03832720 0.010097304
# 10 4.5089286 5.4910714 68.65714 238.3429 0.4508929 0.06790978 0.06790978 0.021742855

pdf("plots/ubcf_topn_10folds_res.pdf")
plot(ubcf_res, annotate=T)
dev.off()

pdf("plots/svd_topn_10folds_res.pdf")
plot(svd_res, annotate=T)
dev.off()


# DIFFERENT PARAMETERS AND MODELS EVALUATION
# As a reminder, here are the different params for the different recommenders

# $UBCF_realRatingMatrix
# Recommender method: UBCF
# Description: Recommender based on user-based collaborative filtering (real data).
# Parameters:
#   method nn sample normalize
# 1 cosine 25  FALSE    center

# $SVD_realRatingMatrix
# Recommender method: SVD
# Description: Recommender based on SVD approximation with column-mean imputation (real data).
# Parameters:
#   k maxiter normalize
# 1 10     100    center


# Evaluation Cosine versus Pearson
models_to_evaluate <- list(
  UBCF_cos_30 = list(name = "UBCF", param = list(method = "cosine", nn = 30)),
  UBCF_cos_50 = list(name = "UBCF", param = list(method = "cosine", nn = 50)),
  UBCF_pear_30 = list(name = "UBCF", param = list(method = "pearson", nn = 30)),
  UBCF_pear_50 = list(name = "UBCF", param = list(method = "pearson", nn = 50)),
  SVD_3 = list(name = "SVD", param = list(k = 3, maxiter = 100)),
  SVD_10 = list(name = "SVD", param = list(k = 10, maxiter = 100)),
  SVD_10 = list(name = "SVD", param = list(k = 10, maxiter = 300)),
  SVD_20 = list(name = "SVD", param = list(k = 20, maxiter = 100)),
  SVD_40 = list(name = "SVD", param = list(k = 40, maxiter = 100))
)

# Varying number of recommendation 
n_recommendations <- c(1, 3, 5, 10)

list_results <- evaluate(x = eval_sets, method = models_to_evaluate, n = n_recommendations)

# Plot ROC 
pdf("./plots/ROC_cosinevspearson.pdf")
plot(list_results, annotate = 1, legend = "topleft") 
title("ROC curve")
dev.off()

# Plot Precision/Recall
pdf("./plots/PRvsRC_cosinevspearson.pdf")
plot(list_results, "prec/rec", annotate = 1, legend = "bottomleft") 
title("Precision-recall")
dev.off()

# Optimizing k
vector_k <- c(5, 10, 30, 50)
models_to_evaluate <- lapply(vector_k, function(k){ list(name = "UBCF", 
                                                    param = list(method = "pearson", 
                                                    nn = k))})

names(models_to_evaluate) <- paste0("UBCF_k_", vector_k)

list_results <- evaluate(x = eval_sets, method = models_to_evaluate, n = n_recommendations)

# Plot ROC
pdf("./plots/optK_ROC.pdf")
plot(list_results, annotate = 1, legend = "topleft") 
title("ROC curve")
dev.off()

# Plot Precision/Recall
pdf("./plots/optK_PRvsRC.pdf")
plot(list_results, "prec/rec", annotate = 1, legend = "bottomleft")
title("Precision-recall")
dev.off()

