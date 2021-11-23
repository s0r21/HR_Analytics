from packages import stats, np, pd
from HR_Recruitment_Draft_Dataset import data_df, posting_responsibilities, posting_requirements, posting_nice_for_position,\
data_set_2_resume_return, data_set_1_resume_return, data_set_3_resume_return, data_set_4_resume_return, data_set_5_resume_return,\
data_set_6_resume_return, data_set_7_resume_return, data_set_8_resume_return, data_set_9_resume_return, test_resume_return

# Hypothesis = H0: x1 = x2 (h naught)
# Hypothesis = Ha: x1 != x2 (alternative hypothesis)

# Note: for this study, because the sample size is so low, We're going to do a t-test.

data_set_1_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_1_resume_return)
data_set_1_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_1_resume_return)
data_set_1_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_1_resume_return)
data_set_1_ttest_average = np.mean([data_set_1_ttest_responsibilities, data_set_1_ttest_nice_to_have, data_set_1_ttest_responsibilities])

data_set_2_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_2_resume_return)
data_set_2_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_2_resume_return)
data_set_2_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_2_resume_return)
data_set_2_ttest_average = np.mean([data_set_2_ttest_responsibilities, data_set_2_ttest_requirements, data_set_2_ttest_nice_to_have])

data_set_3_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_3_resume_return)
data_set_3_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_3_resume_return)
data_set_3_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_3_resume_return)
data_set_3_ttest_average = np.mean([data_set_3_ttest_responsibilities, data_set_3_ttest_requirements, data_set_3_ttest_nice_to_have])

data_set_4_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_4_resume_return)
data_set_4_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_4_resume_return)
data_set_4_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_4_resume_return)
data_set_4_ttest_average = np.mean([data_set_4_ttest_responsibilities, data_set_4_ttest_requirements, data_set_4_ttest_nice_to_have])

data_set_5_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_5_resume_return)
data_set_5_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_5_resume_return)
data_set_5_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_5_resume_return)
data_set_5_ttest_average = np.mean([data_set_5_ttest_responsibilities, data_set_5_ttest_requirements, data_set_5_ttest_nice_to_have])

data_set_6_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_6_resume_return)
data_set_6_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_6_resume_return)
data_set_6_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_6_resume_return)
data_set_6_ttest_average = np.mean([data_set_6_ttest_responsibilities, data_set_6_ttest_requirements, data_set_6_ttest_nice_to_have])

data_set_7_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_7_resume_return)
data_set_7_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_7_resume_return)
data_set_7_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_7_resume_return)
data_set_7_ttest_average = np.mean([data_set_7_ttest_responsibilities, data_set_7_ttest_requirements, data_set_7_ttest_nice_to_have])

data_set_8_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_8_resume_return)
data_set_8_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_8_resume_return)
data_set_8_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_8_resume_return)
data_set_8_ttest_average = np.mean([data_set_8_ttest_responsibilities, data_set_8_ttest_requirements, data_set_8_ttest_nice_to_have])

data_set_9_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, data_set_9_resume_return)
data_set_9_ttest_requirements = stats.ttest_ind(posting_requirements, data_set_9_resume_return)
data_set_9_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, data_set_9_resume_return)
data_set_9_ttest_average = np.mean([data_set_9_ttest_responsibilities, data_set_9_ttest_requirements, data_set_9_ttest_nice_to_have])

test_ttest_responsibilities = stats.ttest_ind(posting_responsibilities, test_resume_return)
test_ttest_requirements = stats.ttest_ind(posting_requirements, test_resume_return)
test_ttest_nice_to_have = stats.ttest_ind(posting_nice_for_position, test_resume_return)
test_ttest_average = np.mean([test_ttest_responsibilities, test_ttest_requirements, test_ttest_nice_to_have])

ttest_raw_df = { 'Name':
                     ['person_1', 'person_2', 'person_3', 'person_4', 'person_5',
                      'person_6', 'person_7', 'person_8', 'person_9', 'person_10'],
                 'Responsibilities_Pvalue':
                 [data_set_1_ttest_responsibilities.pvalue, data_set_2_ttest_responsibilities.pvalue,
                  data_set_3_ttest_responsibilities.pvalue, data_set_4_ttest_responsibilities.pvalue,
                  data_set_5_ttest_responsibilities.pvalue, data_set_6_ttest_responsibilities.pvalue,
                  data_set_7_ttest_responsibilities.pvalue, data_set_8_ttest_responsibilities.pvalue,
                  data_set_9_ttest_responsibilities.pvalue, test_ttest_responsibilities.pvalue,
                 ],
                 'Requirements_Pvalue':
                     [data_set_1_ttest_requirements.pvalue, data_set_2_ttest_requirements.pvalue,
                      data_set_3_ttest_requirements.pvalue, data_set_4_ttest_requirements.pvalue,
                      data_set_5_ttest_requirements.pvalue, data_set_6_ttest_requirements.pvalue,
                      data_set_7_ttest_requirements.pvalue, data_set_8_ttest_requirements.pvalue,
                      data_set_9_ttest_requirements.pvalue, test_ttest_requirements.pvalue,
                      ],
                 'Nice_to_Have_Pvalue':
                     [data_set_1_ttest_nice_to_have.pvalue, data_set_2_ttest_nice_to_have.pvalue,
                      data_set_3_ttest_nice_to_have.pvalue, data_set_4_ttest_nice_to_have.pvalue,
                      data_set_5_ttest_nice_to_have.pvalue, data_set_6_ttest_nice_to_have.pvalue,
                      data_set_7_ttest_nice_to_have.pvalue, data_set_8_ttest_nice_to_have.pvalue,
                      data_set_9_ttest_nice_to_have.pvalue, test_ttest_nice_to_have.pvalue,
                      ],
                 'Average of All P-Values':
                 [
                     data_set_1_ttest_average, data_set_2_ttest_average, data_set_3_ttest_average, data_set_4_ttest_average,
                     data_set_5_ttest_average, data_set_6_ttest_average, data_set_7_ttest_average, data_set_8_ttest_average,
                     data_set_9_ttest_average, test_ttest_average
                 ]
}

ttest_df = pd.DataFrame(ttest_raw_df).sort_values(by='Average of All P-Values', ascending= True).\
    reset_index(drop = True)