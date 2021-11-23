# Create a KNN for all the factors.

from packages import train_test_split, pd, KNeighborsClassifier
from HR_Recruitment_Draft_Dataset import data_df_KNN

print(data_df_KNN.head())

def condition_columns(data_set, conditional_column_name, column_name):
    data_set[conditional_column_name] = 0
    data_set.loc[(data_set[column_name] > -0.01) & (data_set[column_name] < 0.01), conditional_column_name] = 1
    return data_set

# Creating a df for the names of people so I know who is who.
index_values = data_df_KNN['Name']

# Data manipulation & splitting the data for the model.
condition_columns(data_df_KNN, 'Total_conditions', 'Total Average')
condition_columns(data_df_KNN, 'Requirements_conditions', 'Requirements')
condition_columns(data_df_KNN, 'Responsibilities_conditions', 'Responsibilities')
condition_columns(data_df_KNN, 'Nice_to_have_conditions', 'Nice to have')

# KNN for Total Average
x_total_average = data_df_KNN.drop('Total_conditions', axis = 1).drop('Name', axis = 1)
y_total_average = data_df_KNN['Total_conditions']

X_train_total_average, X_test_total_average, y_train_total_average, y_test_total_average\
    = train_test_split(x_total_average, y_total_average, test_size = 0.25)

# Building the model
KNN_Model_total_average = KNeighborsClassifier(n_neighbors=3).fit(X_train_total_average, y_train_total_average)
KNN_prediction_total_average = KNN_Model_total_average.predict(X_test_total_average)

# Getting the results of the model
Residual_Values_total_average = pd.DataFrame({
    'Total_Average_Actual Values': y_test_total_average,
    'Total_Average_Predicted Values': KNN_prediction_total_average
})

# KNN for Requirements

x_requirements = data_df_KNN.drop('Requirements_conditions', axis = 1).drop('Name', axis = 1)
y_requirements = data_df_KNN['Requirements_conditions']

X_train_requirements, X_test_requirements, y_train_requirements, y_test_requirements \
    = train_test_split(x_requirements, y_requirements, test_size = 0.25)

# Building the model
KNN_Model_requirements = KNeighborsClassifier(n_neighbors=3).fit(X_train_requirements, y_train_requirements)
KNN_prediction_requirements = KNN_Model_requirements.predict(X_test_requirements)

# Getting the results of the model
Residual_Values_requirements = pd.DataFrame({
    'Requirements_Actual Values': y_test_requirements,
    'Requirements_Predicted Values': KNN_prediction_requirements
})

# KNN for Responsibilities
x_responsibilities = data_df_KNN.drop('Responsibilities_conditions', axis = 1).drop('Name', axis = 1)
y_responsibilities = data_df_KNN['Responsibilities_conditions']

X_train_responsibilities, X_test_responsibilities, y_train_responsibilities, y_test_responsibilities \
    = train_test_split(x_responsibilities, y_responsibilities, test_size = 0.25)

# Building the model
KNN_Model_responsibilities = KNeighborsClassifier(n_neighbors=3).fit(X_train_responsibilities, y_train_responsibilities)
KNN_prediction_responsibilities = KNN_Model_responsibilities.predict(X_test_responsibilities)

# Getting the results of the model
Residual_Values_responsibilities = pd.DataFrame({
    'Responsibilities_Actual Values': y_test_responsibilities,
    'Responsibilities_Predicted Values': KNN_prediction_responsibilities
})

# KNN for Nice to have
x_nice_to_have = data_df_KNN.drop('Nice_to_have_conditions', axis = 1).drop('Name', axis = 1)
y_nice_to_have = data_df_KNN['Nice_to_have_conditions']

X_train_nice_to_have, X_test_nice_to_have, y_train_nice_to_have, y_test_nice_to_have \
    = train_test_split(x_nice_to_have, y_nice_to_have, test_size = 0.25)

# Building the model
KNN_Model_nice_to_have = KNeighborsClassifier(n_neighbors=3).fit(X_train_nice_to_have, y_train_nice_to_have)
KNN_prediction_nice_to_have = KNN_Model_nice_to_have.predict(X_test_nice_to_have)

# Getting the results of the model
Residual_Values_nice_to_have = pd.DataFrame({
    'nice_to_have_Actual Values': y_test_nice_to_have,
    'nice_to_have_Predicted Values': KNN_prediction_nice_to_have
})

Residual_dataframe = pd.concat([
    Residual_Values_total_average,
    Residual_Values_requirements,
    Residual_Values_responsibilities,
    Residual_Values_nice_to_have
], axis = 1)

print(Residual_dataframe)