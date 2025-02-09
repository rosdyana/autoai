# Copyright 2021 BlobCity, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This python file consists of class  PyComments,  which has dictionary models and procedures utilized to add comments/meta description in Code generation.
"""
class IpynbComments:
    models={
        'Classification':{
            'TF':'Neural Network Model Description',
            'LogisticRegression':"""### Model
**Logistic regression :**\n

Logistic regression is a statistical model that in its basic form uses a logistic function to model a binary dependent variable, although many more complex extensions exist. In regression analysis, logistic regression (or logit regression) is estimating the parameters of a logistic model (a form of binary regression). This can be extended to model several classes of events.

#### Model Tuning Parameters
1. penalty : Used to specify the norm used in the penalization.

2. C : Inverse of regularization strength; must be a positive float. Like in support vector machines, smaller values specify stronger regularization.

3. tol : Tolerance for stopping criteria.

4. solver : Algorithm to use in the optimization problem.

5. max_iter : Maximum number of iterations taken for the solvers to converge.

6. multi_class : If the option chosen is 'ovr', then a binary problem is fit for each label. For 'multinomial' the loss minimised is the multinomial loss fit across the entire probability distribution, even when the data is binary. 'multinomial' is unavailable when solver='liblinear'. 'auto' selects 'ovr' if the data is binary, or if solver='liblinear', and otherwise selects 'multinomial'.
""",
            'RidgeClassifier':"""### Model

Classifier using Ridge regression.

This classifier first converts the target values into {-1, 1} and then treats the problem as a regression task (multi-output regression in the multiclass case).

#### Model Tuning Parameters

> **alpha** -> Regularization strength; must be a positive float. Regularization improves the conditioning of the problem and reduces the variance of the estimates. Larger values specify stronger regularization.

> **solver** -> Solver to use in the computational routines {'auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga'}

> **tol** -> Precision of the solution.
""",
            'SGDClassifier':"""### Model
Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression. SGD is merely an optimization technique and does not correspond to a specific family of machine learning models. It is only a way to train a model. Often, an instance of SGDClassifier or SGDRegressor will have an equivalent estimator in the scikit-learn API, potentially using a different optimization technique.


For example, using SGDClassifier(loss='log') results in logistic regression, i.e. a model equivalent to LogisticRegression which is fitted via SGD instead of being fitted by one of the other solvers in LogisticRegression. 

#### Model Tuning Parameters
> - **loss** -> The loss function to be used. 
> - **penalty** -> The penalty (aka regularization term) to be used.
> - **alpha** -> Constant that multiplies the regularization term. The higher the value, the stronger the regularization. Also used to compute the learning rate when set to learning_rate is set to 'optimal'.
> - **l1_ratio** -> The Elastic Net mixing parameter.
> - **tol** -> The stopping criterion
> - **learning_rate** -> The learning rate schedule,possible values {'optimal','constant','invscaling','adaptive'}
> - **eta0** -> The initial learning rate for the 'constant', 'invscaling' or 'adaptive' schedules.
> - **power_t** -> The exponent for inverse scaling learning rate.
> - **epsilon** -> Epsilon in the epsilon-insensitive loss functions; only if loss is 'huber', 'epsilon_insensitive', or 'squared_epsilon_insensitive'.""",
            'ExtraTreesClassifier':"""### Model
ExtraTreesClassifier is an ensemble learning method fundamentally based on decision trees. ExtraTreesClassifier, like RandomForest, randomizes certain decisions and subsets of data to minimize over-learning from the data and overfitting.

#### Model Tuning Parameters

1. n_estimators: The number of trees in the forest. 

2. criterion: The function to measure the quality of a split. Supported criteria are 'gini' for the Gini impurity and 'entropy' for the information gain.
  
3. max_depth: The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.
    
4. max_features: The number of features to consider when looking for the best split:""",
            'RandomForestClassifier':"""### Model

A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the <code>max_samples</code> parameter if <code>bootstrap=True</code> (default), otherwise the whole dataset is used to build each tree.

#### Model Tuning Parameters

1. n_estimators : The number of trees in the forest.

2. criterion : The function to measure the quality of a split. Supported criteria are 'gini' for the Gini impurity and 'entropy' for the information gain.

3. max_depth : The maximum depth of the tree.

4. max_features : The number of features to consider when looking for the best split:

5. bootstrap : Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.

6. oob_score : Whether to use out-of-bag samples to estimate the generalization accuracy.
""",
            'AdaBoostClassifier':"""### Model

AdaBoost is one of the initial boosting ensemble algorithms to be adapted in solving studies. It helps by combine multiple “weak classifiers” into a single “strong classifier.” The core concept of the algorithm is to fit a sequence of weak learners on repeatedly modified versions of the data. The predictions from all the Weak learners are then combined through a weighted majority vote or sum to produce the outcome/Prediction. The data modifications at each iteration consist of applying weights to each of the training samples. Initially, those weights are all set so that the first iteration only trains a weak learner on the original data. For every successive iteration, the sample weights are individually modified, and the algorithm is reapplied to the reweighted data. At a given iteration, those training examples which get incorrectly classified by the model at the previous iteration have their weights increased. Whereas the weight gets decreased for data that has been predicted accurately.As iterations continue, data that are difficult to predict or incorrectly classified receive ever-increasing influence. Each subsequent weak learner is thereby forced to concentrate on the data that are missed by the previous ones in the sequence

#### Tuning Parameters

1. base_estimator: The base estimator from which the boosted ensemble is built. Support for sample weighting is required, as well as proper classes_ and n_classes_ attributes. If None, then the base estimator is DecisionTreeClassifier initialized with max_depth=1.

2. n_estimators: The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early.

3. learning_rate: Learning rate shrinks the contribution of each classifier by learning_rate. There is a trade-off between learning_rate and n_estimators.

4. algorithm: If 'SAMME.R' then use the SAMME.R real boosting algorithm. base_estimator must support calculation of class probabilities. If 'SAMME' then use the SAMME discrete boosting algorithm. The SAMME.R algorithm typically converges faster than SAMME, achieving a lower test error with fewer boosting iterations.

#### Note:
>For better performance of the Adaboost model, the base estimator (Decision Tree Model) can be fine-tuned.
""",
            'GradientBoostingClassifier':"""## Model
**GradientBoostingClassifier**

Gradient Boosting builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions.In each stage nclasses regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function.

 #### Model Tuning Parameters

    1. loss : The loss function to be optimized. 'deviance' refers to deviance (= logistic regression) for classification with probabilistic outputs. For loss 'exponential' gradient boosting recovers the AdaBoost algorithm.

    2. learning_rate : Learning rate shrinks the contribution of each tree by learning_rate. There is a trade-off between learning_rate and n_estimators.

    3. n_estimators : The number of trees in the forest.

    4. criterion : The function to measure the quality of a split. Supported criteria are 'friedman_mse' for the mean squared error with improvement score by Friedman, 'mse' for mean squared error, and 'mae' for the mean absolute error. The default value of 'friedman_mse' is generally the best as it can provide a better approximation in some cases.

    5. max_depth : The maximum depth of the individual regression estimators. The maximum depth limits the number of nodes in the tree. Tune this parameter for best performance; the best value depends on the interaction of the input variables.

    6. max_features : The number of features to consider when looking for the best split:  
    
    7. n_iter_no_change : n_iter_no_change is used to decide if early stopping will be used to terminate training when validation score is not improving. By default it is set to None to disable early stopping. If set to a number, it will set aside validation_fraction size of the training data as validation and terminate training when validation score is not improving in all of the previous n_iter_no_change numbers of iterations. The split is stratified.
    
    8. tol : Tolerance for the early stopping. When the loss is not improving by at least tol for <code>n_iter_no_change</code> iterations (if set to a number), the training stops.""",
            'HistGradientBoostingClassifier':"""### Model

Histogram-based Gradient Boosting Classification Tree.This estimator is much faster than GradientBoostingClassifier for big datasets (n_samples >= 10 000).This estimator has native support for missing values (NaNs). 

[Reference](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingClassifier.html#sklearn.ensemble.HistGradientBoostingClassifier)

> **loss**: The loss function to use in the boosting process.

> **learning_rate**: The learning rate, also known as shrinkage. This is used as a multiplicative factor for the leaves values. Use 1 for no shrinkage.

> **max_iter**: The maximum number of iterations of the boosting process, i.e. the maximum number of trees.

> **max_depth**: The maximum depth of each tree. The depth of a tree is the number of edges to go from the root to the deepest leaf. Depth isn’t constrained by default.

> **l2_regularization**: The L2 regularization parameter. Use 0 for no regularization (default).

> **early_stopping**: If 'auto', early stopping is enabled if the sample size is larger than 10000. If True, early stopping is enabled, otherwise early stopping is disabled.

> **n_iter_no_change**: Used to determine when to 'early stop'. The fitting process is stopped when none of the last n_iter_no_change scores are better than the n_iter_no_change - 1 -th-to-last one, up to some tolerance. Only used if early stopping is performed.

> **tol**: The absolute tolerance to use when comparing scores during early stopping. The higher the tolerance, the more likely we are to early stop: higher tolerance means that it will be harder for subsequent iterations to be considered an improvement upon the reference score.

> **scoring**: Scoring parameter to use for early stopping. """,
            'SVC':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

Here we have used SVC, the svc implementation is based on libsvm.  

### Model Tuning Parameters
1. C -> Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.

2. kernel -> Specifies the kernel type to be used in the algorithm.

3. gamma -> Gamma is a hyperparameter that we have to set before the training model. Gamma decides how much curvature we want in a decision boundary.

4. degree -> Degree of the polynomial kernel function ('poly'). Increasing degree parameter leads to higher training times.
""",
            'NuSVC':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

SVC and NuSVC are similar methods, but accept slightly different sets of parameters and have different mathematical formulations. 

* #### Model Tuning Parameters
1. nu -> An upper bound on the fraction of margin errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1].

2. kernel -> Specifies the kernel type to be used in the algorithm.

3. gamma -> Gamma is a hyperparameter that we have to set before the training model. Gamma decides how much curvature we want in a decision boundary.

4. degree -> Degree of the polynomial kernel function ('poly'). Increasing degree parameter leads to higher training times.""",
            'LinearSVC':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

LinearSVC is similar to SVC with kernel='linear'. It has more flexibility in the choice of tuning parameters and is suited for large samples.

* #### Model Tuning Parameters
1. * penalty -> Specifies the norm used in the penalization.
   
2. * Loss -> Specifies the loss function.
   
3. * C -> Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.
   
4. * tolerance -> Tolerance for stopping criteria.
   
5. * dual -> Select the algorithm to either solve the dual or primal optimization problem. Prefer dual=False when n_samples > n_features.""",
            'DecisionTreeClassifier':"""### Model
 Decision tree is the most powerful and popular tool for classification and prediction. A Decision tree is a flowchart like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node holds a outcome label.

As with other classifiers, DecisionTreeClassifier takes as input two arrays: an array X, sparse or dense, of shape (n_samples, n_features) holding the training samples, and an array Y of integer values, shape (n_samples,), holding the class labels for the training samples.
It is capable of both binary ([-1,1] or [0,1]) classification and multiclass ([0, …,K-1]) classification.

#### Model Tuning Parameter

1. criterion ->  The function to measure the quality of a split. Supported criteria are 'gini' for the Gini impurity and 'entropy' for the information gain.

2. max_depth -> The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

3. max_leaf_nodes -> Grow a tree with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.

4. max_features -> The number of features to consider when looking for the best split: **{auto , sqrt, log2}**""",
            'KNeighborsClassifier':"""## Model
**KNeighborsClassifier :**

KNN is one of the easiest Machine Learning algorithms based on Supervised Machine Learning technique. The algorithm stores all the available data and classifies a new data point based on the similarity. It assumes the similarity between the new data and data and put the new case into the category that is most similar to the available categories.KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much similar to the available data. Model Tuning Parameters:

* n_neighbors -> Number of neighbors to use by default for kneighbors queries.

* weights -> weight function used in prediction. {uniform,distance}

* algorithm-> Algorithm used to compute the nearest neighbors. {'auto', 'ball_tree', 'kd_tree', 'brute'}

* p -> Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.

* leaf_size -> Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.""",
            'RadiusNeighborsClassifier':"""### Model
RadiusNeighborsClassifier implements learning based on the number of neighbors within a fixed radius  of each training point, where  is a floating-point value specified by the user.
In cases where the data is not uniformly sampled, radius-based neighbors classification can be a better choice.

#### Model Tuning Parameters

1. **radius** : Range of parameter space to use by default for radius_neighbors queries.

2. **weights** : weight function used in prediction. Possible values {'uniform','distance'}

3. **algorithm** : Algorithm used to compute the nearest neighbors

4. **leaf_size** : Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.""",
            'MultinomialNB':"""### Model
With a multinomial event model, samples (feature vectors) represent the frequencies with which certain events have been generated by a multinomial probability that an event occurs.

The multinomial Naive Bayes classifier is suitable for classification with discrete features. The multinomial distribution normally requires integer feature counts. However, in practice, fractional counts such as tf-idf may also work.

Model Tuning Parameters
1. alpha : Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).

2. fit_prior : Whether to learn class prior probabilities or not. If false, a uniform prior will be used.

3. class_prior : Prior probabilities of the classes. If specified the priors are not adjusted according to the data.""",
            'CategoricalNB':"""### Model

CategoricalNB implements the categorical naive Bayes algorithm for categorically distributed data. It assumes that each feature, which is described by the index , has its own categorical distribution.

The categorical Naive Bayes classifier is suitable for classification with discrete features that are categorically distributed. The categories of each feature are drawn from a categorical distribution.

Model Tuning Parameters

1. alpha : Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).

2. fit_prior : Whether to learn class prior probabilities or not. If false, a uniform prior will be used.

3. class_prior : Prior probabilities of the classes. If specified the priors are not adjusted according to the data.""",
            'XGBClassifier':"""### Model
XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way.

For Tuning parameters, details refer to official API documentation [Tunning Parameters](https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn) """,
            'NearestCentroid':"""### Model

The NearestCentroid classifier is a simple algorithm that represents each class by the centroid of its members. In effect, this makes it similar to the label updating phase of the KMeans algorithm. It also has no parameters to choose, making it a good baseline classifier. It does, however, suffer on non-convex classes, as well as when classes have drastically different variances, as equal variance in all dimensions is assumed.

#### Tuning Parameter

1. **metric** : The metric to use when calculating distance between instances in a feature array. If metric is a string or callable, it must be one of the options allowed by metrics.pairwise.pairwise_distances for its metric parameter. The centroids for the samples corresponding to each class is the point from which the sum of the distances of all samples that belong to that particular class are minimized. If the “manhattan” metric is provided, this centroid is the median and for all other metrics, the centroid is now set to be the mean.

2. **shrink_threshold** :Threshold for shrinking centroids to remove features.""",
            'Perceptron':"""### Model
 the perceptron is an algorithm for supervised learning of binary classifiers.
 The algorithm learns the weights for the input signals in order to draw a linear decision boundary.This enables you to distinguish between the two linearly separable classes +1 and -1.
#### Model Tuning Parameters

1. **penalty** ->The penalty (aka regularization term) to be used. {'l2','l1','elasticnet'}

2. **alpha** -> Constant that multiplies the regularization term if regularization is used.

3. **l1_ratio** -> The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1. l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1. Only used if penalty='elasticnet'.

4. **tol** -> The stopping criterion. If it is not None, the iterations will stop when (loss > previous_loss - tol).

5. **early_stopping**-> Whether to use early stopping to terminate training when validation. score is not improving. If set to True, it will automatically set aside a stratified fraction of training data as validation and terminate training when validation score is not improving by at least tol for n_iter_no_change consecutive epochs.

6. **validation_fraction** -> The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1. Only used if early_stopping is True.

7. **n_iter_no_change** -> Number of iterations with no improvement to wait before early stopping."""
        },
        'Regression':{
            'LinearRegression':"""### Model

Linear regression algorithm attempts to model the relationship between two variables by fitting a linear equation to observed data. One variable is considered to be an independent variable, and the other is considered to be a dependent variable. 

LinearRegression fits a linear model with coefficients w = (w1, …, wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.""",
            'Ridge':"""### Model
Ridge regression addresses some of the problems of Ordinary Least Squares by imposing a penalty on the size of the coefficients. The ridge coefficients minimize a penalized residual sum of squares:

The complexity parameter  controls the amount of shrinkage: the larger the value of , the greater the amount of shrinkage and thus the coefficients become more robust to collinearity.

This model solves a regression model where the loss function is the linear least squares function and regularization is given by the l2-norm. Also known as Ridge Regression or Tikhonov regularization. This estimator has built-in support for multi-variate regression (i.e., when y is a 2d-array of shape (n_samples, n_targets)).

#### Model Tuning Parameters

1. **alpha** -> Regularization strength; must be a positive float. Regularization improves the conditioning of the problem and reduces the variance of the estimates. Larger values specify stronger regularization.

2. **solver** -> Solver to use in the computational routines.""",
            'SGDRegressor':"""### Model

Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression. SGD is merely an optimization technique and does not correspond to a specific family of machine learning models. It is only a way to train a model. Often, an instance of SGDClassifier or SGDRegressor will have an equivalent estimator in the scikit-learn API, potentially using a different optimization technique.

#### Model Tuning Parameters
1. **loss** -> The loss function to be used. The possible values are ‘squared_loss’, ‘huber’, ‘epsilon_insensitive’, or ‘squared_epsilon_insensitive’
2. **penalty** -> The penalty (aka regularization term) to be used. Defaults to ‘l2’ which is the standard regularizer for linear SVM models. ‘l1’ and ‘elasticnet’ might bring sparsity to the model (feature selection) not achievable with ‘l2’.
3. **alpha** -> Constant that multiplies the regularization term. The higher the value, the stronger the regularization. Also used to compute the learning rate when set to learning_rate is set to ‘optimal’.
4. **l1_ratio** -> The Elastic Net mixing parameter, with 0 <= l1_ratio <= 1. l1_ratio=0 corresponds to L2 penalty, l1_ratio=1 to L1. Only used if penalty is ‘elasticnet’.
5. **tol** -> The stopping criterion
6. **learning_rate** -> The learning rate schedule,possible values {'optimal','constant','invscaling','adaptive'}
7. **eta0** -> The initial learning rate for the ‘constant’, ‘invscaling’ or ‘adaptive’ schedules.
8. **power_t** -> The exponent for inverse scaling learning rate.
9. **epsilon** -> Epsilon in the epsilon-insensitive loss functions; only if loss is ‘huber’, ‘epsilon_insensitive’, or ‘squared_epsilon_insensitive’.""",
            'ExtraTreesRegressor':"""### Model
ExtraTrees Regressor model implements a meta estimator that fits a number of randomized decision trees (a.k.a. extra-trees) on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

#### Model Tuning Parameters

    1. n_estimators: The number of trees in the forest.

    2.criterion: The function to measure the quality of a split. Supported criteria are “mse” for the mean squared error, which is equal to variance reduction as feature selection criterion, and “mae” for the mean absolute error.

    3.max_depth: The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

    4.max_features: The number of features to consider when looking for the best split""",
            'RandomForestRegressor':"""### Model

A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the <code>max_samples</code> parameter if <code>bootstrap=True</code> (default), otherwise the whole dataset is used to build each tree.

#### Model Tuning Parameters

    1. n_estimators : The number of trees in the forest.

    2. criterion : The function to measure the quality of a split. Supported criteria are 'mse' for the mean squared error, which is equal to variance reduction as feature selection criterion, and 'mae' for the mean absolute error.

    3. max_depth : The maximum depth of the tree.

    4. max_features : The number of features to consider when looking for the best split:

    5. bootstrap : Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree.

    6. oob_score : Whether to use out-of-bag samples to estimate the generalization accuracy.""",
            'AdaBoostRegressor':"""### Model

AdaBoost is one of the initial boosting ensemble algorithms to be adapted in solving studies. It helps by combine multiple 'weak classifiers' into a single 'strong classifier.' The core concept of the algorithm is to fit a sequence of weak learners on repeatedly modified versions of the data. The predictions from all the Weak learners are then combined through a weighted majority vote or sum to produce the outcome/Prediction. The data modifications at each iteration consist of applying weights to each of the training samples. Initially, those weights are all set so that the first iteration only trains a weak learner on the original data. For every successive iteration, the sample weights are individually modified, and the algorithm is reapplied to the reweighted data.    At a given iteration, those training examples which get incorrectly classified by the model at the previous iteration have their weights increased. Whereas the weight gets decreased for data that has been predicted accurately.As iterations continue, data that are difficult to predict or incorrectly classified receive ever-increasing influence. Each subsequent weak learner is thereby forced to concentrate on the data that are missed by the previous ones in the sequence

#### Model Tuning Parameters:

    1. base_estimator: The base estimator from which the boosted ensemble is built. If None, then the base estimator is DecisionTreeRegressor initialized with max_depth=3.

    2. n_estimators: The maximum number of estimators at which boosting is terminated. In case of perfect fit, the learning procedure is stopped early.

    3. learning_rate: Learning rate shrinks the contribution of each regressor by learning_rate. There is a trade-off between learning_rate and n_estimators.

    4. loss: The loss function to use when updating the weights after each boosting iteration.

#### Note: For better performance of the Adaboost model, the base estimator (Decision Tree Model) can be fine-tuned.
""",
            'GradientBoostingRegressor':"""### Model

Gradient Boosting builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage a regression tree is fit on the negative gradient of the given loss function.

#### Model Tuning Parameters

    1. loss : Loss function to be optimized.

    2. learning_rate: Learning rate shrinks the contribution of each tree by learning_rate. There is a trade-off between learning_rate and n_estimators.

    3. n_estimators : The number of trees in the forest.

    4. criterion : The function to measure the quality of a split. Supported criteria are 'friedman_mse' for the mean squared error with improvement score by Friedman, 'mse' for mean squared error, and 'mae' for the mean absolute error. The default value of 'friedman_mse' is generally the best as it can provide a better approximation in some cases.

    5. max_depth : The maximum depth of the individual regression estimators. The maximum depth limits the number of nodes in the tree. Tune this parameter for best performance; the best value depends on the interaction of the input variables.

    6. max_features : The number of features to consider when looking for the best split:  
    
    7. n_iter_no_change : Is used to decide if early stopping will be used to terminate training when validation score is not improving. By default it is set to None to disable early stopping. If set to a number, it will set aside <code>validation_fraction</code> size of the training data as validation and terminate training when validation score is not improving in all of the previous <code>n_iter_no_change</code> numbers of iterations. The split is stratified.
    
    8. tol : Tolerance for the early stopping.""",
            'HistGradientBoostingRegressor':"""### Model

Histogram-based Gradient Boosting Regression Tree.This estimator is much faster than GradientBoostingRegressor for big datasets (n_samples >= 10 000).This estimator has native support for missing values (NaNs). 

#### Tuning Parameters 
[Reference](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)

1. **loss**: The loss function to use in the boosting process. 

2. **learning_rate**: The learning rate, also known as shrinkage. This is used as a multiplicative factor for the leaves values.

3. **max_iter**: The maximum number of iterations of the boosting process.

4. **max_depth**: The maximum depth of each tree. The depth of a tree is the number of edges to go from the root to the deepest leaf.

5. **l2_regularization**: The L2 regularization parameter.

6. **early_stopping**: If 'auto', early stopping is enabled if the sample size is larger than 10000. If True, early stopping is enabled, otherwise early stopping is disabled.

7. **n_iter_no_change**: Used to determine when to 'early stop'. The fitting process is stopped when none of the last n_iter_no_change scores are better than the n_iter_no_change - 1 -th-to-last one, up to some tolerance.

8. **tol**: The absolute tolerance to use when comparing scores during early stopping.

9. **scoring**: Scoring parameter to use for early stopping. """,
            'SVR':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

Here we will use SVR, the svr implementation is based on libsvm. The fit time scales at least quadratically with the number of samples and maybe impractical beyond tens of thousands of samples. 

#### Model Tuning Parameters

    1. C : Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive. The penalty is a squared l2 penalty.

    2. kernel : Specifies the kernel type to be used in the algorithm.

    3. gamma : Gamma is a hyperparameter that we have to set before the training model. Gamma decides how much curvature we want in a decision boundary.

    4. degree : Degree of the polynomial kernel function ('poly'). Ignored by all other kernels. Increasing degree parameter leads to higher training times.
""",
            'NuSVR':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

Here we will use NuSVR, the NuSVR implementation is based on libsvm. Similar to NuSVC, for regression, uses a parameter nu to control the number of support vectors. However, unlike NuSVC, where nu replaces C, here nu replaces the parameter epsilon of epsilon-SVR. 
#### Model Tuning Parameters

    1. nu : An upper bound on the fraction of training errors and a lower bound of the fraction of support vectors. Should be in the interval (0, 1]. By default 0.5 will be taken.

    2. C : Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive. The penalty is a squared l2 penalty.

    3. kernel : Specifies the kernel type to be used in the algorithm. 

    4. gamma : Gamma is a hyperparameter that we have to set before the training model. Gamma decides how much curvature we want in a decision boundary.

    5. degree : Degree of the polynomial kernel function ('poly'). Ignored by all other kernels.Using degree 1 is similar to using a linear kernel. Also, Increasing degree parameter leads to higher training times.""",
            'LinearSVR':"""### Model
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

A Support Vector Machine is a discriminative classifier formally defined by a separating hyperplane. In other terms, for a given known/labelled data points, the SVM outputs an appropriate hyperplane that classifies the inputted new cases based on the hyperplane. In 2-Dimensional space, this hyperplane is a line separating a plane into two segments where each class or group occupied on either side.

LinearSVR is similar to SVR with kernel='linear'. It has more flexibility in the choice of tuning parameters and is suited for large samples.

#### Model Tuning Parameters

    1. epsilon : Epsilon parameter in the epsilon-insensitive loss function.

    2. loss : Specifies the loss function. 'hinge' is the standard SVM loss (used e.g. by the SVC class) while 'squared_hinge' is the square of the hinge loss. The combination of penalty='l1' and loss='hinge' is not supported.

    3. C : Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.

    4. tol : Tolerance for stopping criteria.

    5. dual : Select the algorithm to either solve the dual or primal optimization problem. Prefer dual=False when n_samples > n_features.""",
            'DecisionTreeRegressor':"""### Model
 Decision tree is the most powerful and popular tool for classification and prediction. A Decision tree is a flowchart like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node holds a outcome label.

Decision trees can also be applied to regression problems, using the DecisionTreeRegressor class.

As in the classification setting, the fit method will take as argument arrays X and y, only that in this case y is expected to have floating point values instead of integer values

#### Model Tuning Parameter

1. criterion ->  The function to measure the quality of a split. Supported criteria are “mse” for the mean squared error, which is equal to variance reduction as feature selection criterion and minimizes the L2 loss using the mean of each terminal node, “friedman_mse”, which uses mean squared error with Friedman’s improvement score for potential splits, “mae” for the mean absolute error, which minimizes the L1 loss using the median of each terminal node, and “poisson” which uses reduction in Poisson deviance to find splits.

2. max_depth -> The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.

3. max_leaf -> Grow a tree with max_leaf_nodes in best-first fashion. Best nodes are defined as relative reduction in impurity. If None then unlimited number of leaf nodes.

4. max_features -> The number of features to consider when looking for the best split: **{auto , sqrt, log2}**""",
            'KNeighborsRegressor':"""### Model

KNN is one of the easiest Machine Learning algorithms based on Supervised Machine Learning technique. The algorithm stores all the available data and classifies a new data point based on the similarity. It assumes the similarity between the new data and data and put the new case into the category that is most similar to the available categories.KNN algorithm at the training phase just stores the dataset and when it gets new data, then it classifies that data into a category that is much similar to the available data.
#### Model Tuning Parameters
   1. n_neighbors -> Number of neighbors to use by default for kneighbors queries.

   2. weights -> weight function used in prediction. {**uniform,distance**}
   
   3. algorithm -> Algorithm used to compute the nearest neighbors. {**'auto', 'ball_tree', 'kd_tree', 'brute'**}

   4. p -> Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2.
    
   5. leaf_size -> Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.""",
            'Lasso':"""### Model

Linear Model trained with L1 prior as regularizer (aka the Lasso)

The Lasso is a linear model that estimates sparse coefficients. It is useful in some contexts due to its tendency to prefer solutions with fewer non-zero coefficients, effectively reducing the number of features upon which the given solution is dependent. For this reason Lasso and its variants are fundamental to the field of compressed sensing.

#### Model Tuning Parameter
1. **alpha** -> Constant that multiplies the L1 term. Defaults to 1.0. alpha = 0 is equivalent to an ordinary least square, solved by the LinearRegression object. For numerical reasons, using alpha = 0 with the Lasso object is not advised.

2. **selection** -> If set to ‘random’, a random coefficient is updated every iteration rather than looping over features sequentially by default. This (setting to ‘random’) often leads to significantly faster convergence especially when tol is higher than 1e-4.

3. **tol** -> The tolerance for the optimization: if the updates are smaller than tol, the optimization code checks the dual gap for optimality and continues until it is smaller than tol.

4. **max_iter** -> The maximum number of iterations.""",
            'Lars':"""### Model

Least-angle regression (LARS) is a regression algorithm for high-dimensional data, developed by Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani. LARS is similar to forward stepwise regression. At each step, it finds the feature most correlated with the target. When there are multiple features having equal correlation, instead of continuing along the same feature, it proceeds in a direction equiangular between the features.

### Tuning parameters

1. **jitter** -> Upper bound on a uniform noise parameter to be added to the y values, to satisfy the model’s assumption of one-at-a-time computations. Might help with stability.

2. **eps** -> The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Unlike the tol parameter in some iterative optimization-based algorithms, this parameter does not control the tolerance of the optimization.

3. **n_nonzero_coefs** -> Target number of non-zero coefficients. Use np.inf for no limit.

4. **precompute** -> Whether to use a precomputed Gram matrix to speed up calculations. """,
            'BayesianRidge':"""### Model

Bayesian Regression can be very useful when we have insufficient data in the dataset or the data is poorly distributed. The output of a Bayesian Regression model is obtained from a probability distribution, as compared to regular regression techniques where the output is just obtained from a single value of each attribute.
Bayesian regression techniques can be used to include regularization parameters in the estimation procedure: the regularization parameter is not set in a hard sense but tuned to the data at hand.

If there is a large amount of data available for our dataset, the Bayesian approach is not good for such cases.

#### Model Tuning Parameters

1. **alpha_1** : shape parameter for the Gamma distribution prior over the alpha parameter.

2. **alpha_2** : inverse scale parameter (rate parameter) for the Gamma distribution prior over the alpha parameter.

3. **lambda_1** : shape parameter for the Gamma distribution prior over the lambda parameter.

4. **lambda_2** : inverse scale parameter (rate parameter) for the Gamma distribution prior over the lambda parameter.""",
            'LassoLars':"""### Model

LassoLars is a lasso model implemented using the LARS algorithm, and unlike the implementation based on coordinate descent, this yields the exact solution, which is piecewise linear as a function of the norm of its coefficients.

### Tuning parameters

1. **fit_intercept** -> whether to calculate the intercept for this model. If set to false, no intercept will be used in calculations

2.  **alpha** -> Constant that multiplies the penalty term. Defaults to 1.0. alpha = 0 is equivalent to an ordinary least square, solved by LinearRegression. For numerical reasons, using alpha = 0 with the LassoLars object is not advised and you should prefer the LinearRegression object.

3.  **eps** -> The machine-precision regularization in the computation of the Cholesky diagonal factors. Increase this for very ill-conditioned systems. Unlike the tol parameter in some iterative optimization-based algorithms, this parameter does not control the tolerance of the optimization.

4. **max_iter** -> Maximum number of iterations to perform.

5. **positive** -> Restrict coefficients to be >= 0. Be aware that you might want to remove fit_intercept which is set True by default. Under the positive restriction the model coefficients will not converge to the ordinary-least-squares solution for small values of alpha. Only coefficients up to the smallest alpha value (alphas_[alphas_ > 0.].min() when fit_path=True) reached by the stepwise Lars-Lasso algorithm are typically in congruence with the solution of the coordinate descent Lasso estimator.

6. **precompute** -> Whether to use a precomputed Gram matrix to speed up calculations. """,
            'XGBRegressor':"""### Model
XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way.

For Tuning parameters, details refer to official API documentation [Tunning Parameters](https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.sklearn) """,
            'ARDRegressor':"""### Model

Bayesian ARD regression.

Fit the weights of a regression model, using an ARD prior. The weights of the regression model are assumed to be in Gaussian distributions. Also estimate the parameters lambda (precisions of the distributions of the weights) and alpha (precision of the distribution of the noise). The estimation is done by an iterative procedures (Evidence Maximization)

#### Parameters:
1. **n_iter**: Maximum number of iterations.
2. **tol**: Stop the algorithm if w has converged.
3. **alpha_1**: shape parameter for the Gamma distribution prior over the alpha parameter.
4. **alpha_2**: inverse scale parameter (rate parameter) for the Gamma distribution prior over the alpha parameter.
5. **lambda_1**: shape parameter for the Gamma distribution prior over the lambda parameter.
6. **lambda_2**: inverse scale parameter (rate parameter) for the Gamma distribution prior over the lambda parameter.""",
            'CatBoostRegressor':"""### Model

CatBoost is an algorithm for gradient boosting on decision trees. Developed by Yandex researchers and engineers, it is the successor of the MatrixNet algorithm that is widely used within the company for ranking tasks, forecasting and making recommendations

#### Tuning parameters

1. **learning_rate**:, The learning rate. Used for reducing the gradient step.

2. **l2_leaf_reg**: Coefficient at the L2 regularization term of the cost function. Any positive value is allowed.

3. **bootstrap_type**: Bootstrap type. Defines the method for sampling the weights of objects.
    
4. **subsample**: Sample rate for bagging. This parameter can be used if one of the following bootstrap types is selected:

For more information refer: [API](https://catboost.ai/docs/concepts/python-reference_catboostregressor.html)""",
            'GammaRegressor':"""### Model

Generalized Linear Model with a Gamma distribution.This regressor uses the 'log' link function.

1. alpha: Constant that multiplies the penalty term and thus determines the regularization strength.

2. max_iter: The maximal number of iterations for the solver.

3. tol: Stopping criterion.

For Ref: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.GammaRegressor.html""",
            'LGBMRegressor':"""### Model

LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and efficient with the following advantages:

- Faster training speed and higher efficiency.

- Lower memory usage.

- Better accuracy.

- Support of parallel, distributed, and GPU learning.

- Capable of handling large-scale data.

### Tuning parameters
1. **boosting_type** - 'gbdt', traditional Gradient Boosting Decision Tree. 'dart', Dropouts meet Multiple Additive Regression Trees. 'goss', Gradient-based One-Side Sampling. 'rf', Random Forest

2. **num_leaves** - Maximum tree leaves for base learners.

3. **max_depth**  - Maximum tree depth for base learners, <=0 means no limit.

4. **p** - Power parameter for the Minkowski metric.

5. **learning_rate**  - Boosting learning rate. You can use callbacks parameter of fit method to shrink/adapt learning rate in training using reset_parameter callback. Note, that this will ignore the learning_rate argument in training.

6. **min_split_gain** - Minimum loss reduction required to make a further partition on a leaf node of the tree.

7. **min_child_samples** - Minimum number of data needed in a child (leaf).

For more information refer: [API](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html)""",
            'RadiusNeighborsRegressor':"""### Model

 RadiusNeighborsRegressor implements learning based on the neighbors within a fixed radius  of the query point, where  is a floating-point value specified by the user.
 
#### Tuning parameters

1. **radius**: Range of parameter space to use by default for radius_neighbors queries.

2. **algorithm**: Algorithm used to compute the nearest neighbors:

3. **leaf_size**: Leaf size passed to BallTree or KDTree. 

4. **p**: Power parameter for the Minkowski metric.

5. **metric**: the distance metric to use for the tree. 

6. **outlier_label**: label for outlier samples 

7. **weights**: weight function used in prediction.

For more information refer: [API](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor)""",
            'PassiveAggressiveRegressor':"""### Model

The passive-aggressive algorithms are a family of algorithms for large-scale learning. They are similar to the Perceptron in that they do not require a learning rate. However, contrary to the Perceptron, they include a regularization parameter C

1. **C** ->Maximum step size (regularization). Defaults to 1.0.

2. **max_iter** ->The maximum number of passes over the training data (aka epochs). It only impacts the behavior in the fit method, and not the partial_fit method.

3. **tol**->The stopping criterion. If it is not None, the iterations will stop when (loss > previous_loss - tol).

4. **early_stopping**->Whether to use early stopping to terminate training when validation. score is not improving. If set to True, it will automatically set aside a fraction of training data as validation and terminate training when validation score is not improving by at least tol for n_iter_no_change consecutive epochs.

5. **validation_fraction**->The proportion of training data to set aside as validation set for early stopping. Must be between 0 and 1. Only used if early_stopping is True.

6. **n_iter_no_change**->Number of iterations with no improvement to wait before early stopping.

7. **shuffle**->Whether or not the training data should be shuffled after each epoch.

8. **loss**->The loss function to be used: epsilon_insensitive: equivalent to PA-I in the reference paper. squared_epsilon_insensitive: equivalent to PA-II in the reference paper.

9. **epsilon**->If the difference between the current prediction and the correct label is below this threshold, the model is not updated.""",
            'HuberRegressor':"""### Model

Linear regression model that is robust to outliers. The Huber Regressor optimizes the squared loss for the samples where |(y - X'w) / sigma| < epsilon and the absolute loss for the samples where |(y - X'w) / sigma| > epsilon, where w and sigma are parameters to be optimized. The parameter sigma makes sure that if y is scaled up or down by a certain factor, one does not need to rescale epsilon to achieve the same robustness. Note that this does not take into account the fact that the different features of X may be of different scales.
This makes sure that the loss function is not heavily influenced by the outliers while not completely ignoring their effect.
#### Tuning Parameters:

1. epsilon: The parameter epsilon controls the number of samples that should be classified as outliers. The smaller the epsilon, the more robust it is to outliers.

2. max_iter: Maximum number of iterations that scipy.optimize.minimize(method="L-BFGS-B") should run for.

3. alpha: Regularization parameter.

4. tol: The iteration will stop when max{|proj g_i | i = 1, ..., n} <= tol where pg_i is the i-th component of the projected gradient.
""",
            'ElasticNet':"""### Model

Elastic Net first emerged as a result of critique on Lasso, whose variable selection can be too dependent on data and thus unstable. The solution is to combine the penalties of Ridge regression and Lasso to get the best of both worlds.

 #### Model Tuning Parameters

    1. alpha : Constant that multiplies the penalty terms.

    2. l1_ratio : The ElasticNet mixing parameter.

    3. max_iter : The maximum number of iterations.

    4. tol : The tolerance for the optimization: if the updates are smaller than tol, the optimization code checks the dual gap for optimality and continues until it is smaller than tol.

    5. selection : If set to 'random', a random coefficient is updated every iteration rather than looping over features sequentially by default. 'random' often leads to significantly faster convergence especially when tol is higher than 1e-4.
""",
    'PoissonRegressor':"""### Model

Poisson regression is a generalized linear model form of regression used to model count data and contingency tables. It assumes the response variable or target variable Y has a Poisson distribution, and assumes the logarithm of its expected value can be modeled by a linear combination of unknown parameters. It is sometimes known as a log-linear model, especially when used to model contingency tables.

#### Model Tuning Parameters
1. **alpha**  -> Constant that multiplies the penalty term and thus determines the regularization strength. alpha = 0 is equivalent to unpenalized GLMs.

2. **tol**  -> Stopping criterion.

3. **max_iter** -> The maximal number of iterations for the solver.""",
'TF':'Neural Network Model Description'
        }
    }

    procedure={
        'datafetch':"### Data Fetch\n Pandas is an open-source, BSD-licensed library providing high-performance,easy-to-use data manipulation and data analysis tools.",
        'missing':"### Data Preprocessing\n Since the majority of the machine learning models in the Sklearn library doesn't handle string category data and Null value,we have to explicitly remove or replace null values.The below snippet have functions, which removes the null value if any exists.",
        'encoding':"### Data Encoding\n Converting the string classes data in the datasets by encoding them to integer either using OneHotEncoding or LabelEncoding",
        'datasplit':"### Train & Test\n The train-test split is a procedure for evaluating the performance of an algorithm.The procedure involves taking a dataset and dividing it into two subsets.The first subset is utilized to fit/train the model.The second subset is used for prediction.The main motive is to estimate the performance of the model on new data.",
        'metrics':"### Accuracy Metrics\n Performance metrics are a part of every machine learning pipeline. They tell you if you're making progress, and put a number on it. All machine learning models,whether it's linear regression, or a SOTA technique like BERT, need a metric to judge performance.",
        'x&y':"### Feature Selection\n It is the process of reducing the number of input variables when developing a predictive model.Used to reduce the number of input variables to reduce the computational cost of modelling and,in some cases,to improve the performance of the model.",
        'cor_matrix': "### Correlation Matrix\n In order to check the correlation between the features, we will plot a correlation matrix. It is effective in summarizing a large amount of data where the goal is to see patterns."
    }