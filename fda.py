import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import mean_absolute_error as mae
import math
import statistics


def FDA_Report(train_df, test_df):
    def error_calculation_sbp_without_GE_error(test_df):
        Mean_absolute_error_sbp = mae(test_df["Calc_SBP"], test_df["REF_SBP"])
        mape_sbp_1 = (mean_absolute_percentage_error(test_df["Calc_SBP"], test_df["REF_SBP"])) * 100
        mape_sbp = str(round(mape_sbp_1, 2)) + "%"
        mean = statistics.mean(test_df["SBP_Diff"])
        abs_diff = np.abs(np.array(test_df["SBP_Diff"]) - mean)
        mean_deviation = statistics.mean(abs_diff)
        if len(test_df) > 2:
            STANDARD_DEVIATION = statistics.stdev(test_df["SBP_Diff"])
            return round(Mean_absolute_error_sbp, 2), mape_sbp, round(mean_deviation, 2), round(STANDARD_DEVIATION, 2)
        else:
            STANDARD_DEVIATION = None
            return round(Mean_absolute_error_sbp, 2), mape_sbp, round(mean_deviation, 2), STANDARD_DEVIATION

    def error_calculation_dbp_without_GE_error(test_df):
        Mean_absolute_error_dbp = mae(test_df["Calc_DBP"], test_df["REF_DBP"])
        mape_dbp_1 = (mean_absolute_percentage_error(test_df["Calc_DBP"], test_df["REF_DBP"])) * 100
        mape_dbp = str(round(mape_dbp_1, 2)) + "%"
        mean = statistics.mean(test_df["DBP_Diff"])
        abs_diff = np.abs(np.array(test_df["DBP_Diff"]) - mean)
        mean_deviation = statistics.mean(abs_diff)
        if len(test_df) > 2:
            STANDARD_DEVIATION = statistics.stdev(test_df["DBP_Diff"])
            return round(Mean_absolute_error_dbp, 2), mape_dbp, round(mean_deviation, 2), round(STANDARD_DEVIATION, 2)
        else:
            STANDARD_DEVIATION = None
            return round(Mean_absolute_error_dbp, 2), mape_dbp, round(mean_deviation, 2), STANDARD_DEVIATION


    def sbp_accuracy_without_GE_error(test_df):
        Cumulative_Percentage_sbp_less_than_five = (sum(test_df.SBP_Diff <= 5) / len(test_df["SBP_Diff"])) * 100
        Cumulative_Percentage_sbp_less_than_ten = (sum(test_df.SBP_Diff <= 10) / len(test_df["SBP_Diff"])) * 100
        Cumulative_Percentage_sbp_less_than_fifteen = (sum(test_df.SBP_Diff <= 15) / len(test_df["SBP_Diff"])) * 100
        return round(Cumulative_Percentage_sbp_less_than_five, 2), round(Cumulative_Percentage_sbp_less_than_ten, 2), \
            round(Cumulative_Percentage_sbp_less_than_fifteen, 2)

    def dbp_accuracy_without_GE_error(test_df):
        Cumulative_Percentage_dbp_less_than_five = (sum(test_df.DBP_Diff <= 5) / len(test_df["DBP_Diff"])) * 100
        Cumulative_Percentage_dbp_less_than_ten = (sum(test_df.DBP_Diff <= 10) / len(test_df["DBP_Diff"])) * 100
        Cumulative_Percentage_dbp_less_than_fifteen = (sum(test_df.DBP_Diff <= 15) / len(test_df["DBP_Diff"])) * 100
        return round(Cumulative_Percentage_dbp_less_than_five, 2), round(Cumulative_Percentage_dbp_less_than_ten, 2), \
            round(Cumulative_Percentage_dbp_less_than_fifteen, 2)

    Number_of_userid_train_data = len(train_df.USR_ID.unique())
    Number_of_msrid_train_data = len(train_df.MSR_ID.unique())
    train_data_min_sbp = round(min(train_df["Calc_SBP"]))
    train_data_max_sbp = round(max(train_df["Calc_SBP"]))
    train_data_min_dbp = round(min(train_df["Calc_DBP"]))
    train_data_max_dbp = round(max(train_df["Calc_DBP"]))

    Number_of_userid_test_data = len(test_df.USR_ID.unique())
    Number_of_msrid_test_data = len(test_df.MSR_ID.unique())
    test_data_min_sbp = round(min(test_df["Calc_SBP"]))
    test_data_max_sbp = round(max(test_df["Calc_SBP"]))
    test_data_min_dbp = round(min(test_df["Calc_DBP"]))
    test_data_max_dbp = round(max(test_df["Calc_DBP"]))

    Mean_absolute_error_sbp, mape_sbp, mean_deviation_sbp, std_dev_sbp = error_calculation_sbp_without_GE_error(test_df)
    Cumulative_Percentage_sbp_less_than_five, Cumulative_Percentage_sbp_less_than_ten, \
        Cumulative_Percentage_sbp_less_than_fifteen = sbp_accuracy_without_GE_error(test_df)

    Mean_absolute_error_dbp, mape_dbp, mean_deviation_dbp, std_dev_dbp = error_calculation_dbp_without_GE_error(test_df)
    Cumulative_Percentage_dbp_less_than_five, Cumulative_Percentage_dbp_less_than_ten, \
        Cumulative_Percentage_dbp_less_than_fifteen = dbp_accuracy_without_GE_error(test_df)

    test_df_male = test_df[test_df["GENDER"] == "male"]
    if len(test_df_male) > 0:
        number_of_user_id_male_test = len(test_df_male.USR_ID.unique())
        number_of_msr_id_male_test = len(test_df_male.MSR_ID.unique())
        Mean_absolute_error_sbp_male, mape_sbp_male, mean_deviation_sbp_male, \
            std_dev_sbp_male = error_calculation_sbp_without_GE_error(test_df_male)
        Cumulative_Percentage_sbp_less_than_five_male, Cumulative_Percentage_sbp_less_than_ten_male, \
            Cumulative_Percentage_sbp_less_than_fifteen_male = sbp_accuracy_without_GE_error(test_df_male)
    else:
        number_of_user_id_male_test = 0
        number_of_msr_id_male_test = 0
        Mean_absolute_error_sbp_male, mape_sbp_male, mean_deviation_sbp_male, std_dev_sbp_male = None, None, None, None
        Cumulative_Percentage_sbp_less_than_five_male, Cumulative_Percentage_sbp_less_than_ten_male, \
            Cumulative_Percentage_sbp_less_than_fifteen_male = None, None, None

    test_df_female = test_df[test_df["GENDER"] == "female"]
    if len(test_df_female) > 0:
        number_of_user_id_female_test = len(test_df_female.USR_ID.unique())
        number_of_msr_id_female_test = len(test_df_female.MSR_ID.unique())
        Mean_absolute_error_sbp_female, mape_sbp_female, mean_deviation_sbp_female, \
            std_dev_sbp_female = error_calculation_sbp_without_GE_error(test_df_female)
        Cumulative_Percentage_sbp_less_than_five_female, Cumulative_Percentage_sbp_less_than_ten_female, \
            Cumulative_Percentage_sbp_less_than_fifteen_female = sbp_accuracy_without_GE_error(test_df_female)
    else:
        number_of_user_id_female_test = 0
        number_of_msr_id_female_test = 0
        Mean_absolute_error_sbp_female, mape_sbp_female, mean_deviation_sbp_female, \
            std_dev_sbp_female = None, None, None, None
        Cumulative_Percentage_sbp_less_than_five_female, Cumulative_Percentage_sbp_less_than_ten_female, \
            Cumulative_Percentage_sbp_less_than_fifteen_female = None, None, None

    test_df_less_than_120_sbp_1 = test_df[test_df["Calc_SBP"] < 120]
    if len(test_df_less_than_120_sbp_1) > 0:
        number_of_user_id_test_df_less_than_120_sbp = len(test_df_less_than_120_sbp_1.USR_ID.unique())
        number_of_msr_id_test_df_less_than_120_sbp = len(test_df_less_than_120_sbp_1.MSR_ID.unique())
        Mean_absolute_error_less_than_120_sbp, mape_less_than_120_sbp, mean_deviation_less_than_120_sbp, \
            std_dev_less_than_120_sbp = error_calculation_sbp_without_GE_error(test_df_less_than_120_sbp_1)
        Cumulative_Percentage_less_than_five_less_than_120_sbp, Cumulative_Percentage_less_than_ten_less_than_120_sbp, \
            Cumulative_Percentage_less_than_fifteen_less_than_120_sbp = \
            sbp_accuracy_without_GE_error(test_df_less_than_120_sbp_1)
    else:
        number_of_user_id_test_df_less_than_120_sbp = 0
        number_of_msr_id_test_df_less_than_120_sbp = 0
        Mean_absolute_error_less_than_120_sbp, mape_less_than_120_sbp, mean_deviation_less_than_120_sbp, \
            std_dev_less_than_120_sbp = None, None, None, None
        Cumulative_Percentage_less_than_five_less_than_120_sbp, Cumulative_Percentage_less_than_ten_less_than_120_sbp, \
            Cumulative_Percentage_less_than_fifteen_less_than_120_sbp = None, None, None

    test_df_lies_btw_120_140_sbp_1 = test_df[(test_df['Calc_SBP'] >= 120) & (test_df['Calc_SBP'] < 140)]
    if len(test_df_lies_btw_120_140_sbp_1) > 0:
        number_of_user_id_test_df_lies_btw_120_140_sbp = len(test_df_lies_btw_120_140_sbp_1.USR_ID.unique())
        number_of_msr_id_test_df_lies_btw_120_140_sbp = len(test_df_lies_btw_120_140_sbp_1.MSR_ID.unique())
        Mean_absolute_error_lies_btw_120_140_sbp, mape_lies_btw_120_140_sbp, mean_deviation_lies_btw_120_140_sbp, \
            std_dev_lies_btw_120_140_sbp = error_calculation_sbp_without_GE_error(test_df_lies_btw_120_140_sbp_1)
        Cumulative_Percentage_less_than_five_lies_btw_120_140_sbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_120_140_sbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_120_140_sbp = \
            sbp_accuracy_without_GE_error(test_df_lies_btw_120_140_sbp_1)
    else:
        number_of_user_id_test_df_lies_btw_120_140_sbp = 0
        number_of_msr_id_test_df_lies_btw_120_140_sbp = 0
        Mean_absolute_error_lies_btw_120_140_sbp, mape_lies_btw_120_140_sbp, mean_deviation_lies_btw_120_140_sbp, \
            std_dev_lies_btw_120_140_sbp = None, None, None, None
        Cumulative_Percentage_less_than_five_lies_btw_120_140_sbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_120_140_sbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_120_140_sbp = None, None, None

    test_df_lies_btw_140_160_sbp_1 = test_df[(test_df['Calc_SBP'] >= 160) & (test_df['Calc_SBP'] < 160)]
    if len(test_df_lies_btw_140_160_sbp_1) > 0:
        number_of_user_id_test_df_lies_btw_140_160_sbp = len(test_df_lies_btw_140_160_sbp_1.USR_ID.unique())
        number_of_msr_id_test_df_lies_btw_140_160_sbp = len(test_df_lies_btw_140_160_sbp_1.MSR_ID.unique())
        Mean_absolute_error_lies_btw_140_160_sbp, mape_lies_btw_140_160_sbp, mean_deviation_lies_btw_140_160_sbp, \
            std_dev_lies_btw_140_160_sbp = error_calculation_sbp_without_GE_error(test_df_lies_btw_140_160_sbp_1)
        Cumulative_Percentage_less_than_five_lies_btw_140_160_sbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_140_160_sbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_140_160_sbp = \
            sbp_accuracy_without_GE_error(test_df_lies_btw_140_160_sbp_1)
    else:
        number_of_user_id_test_df_lies_btw_140_160_sbp = 0
        number_of_msr_id_test_df_lies_btw_140_160_sbp = 0
        Mean_absolute_error_lies_btw_140_160_sbp, mape_lies_btw_140_160_sbp, mean_deviation_lies_btw_140_160_sbp, \
            std_dev_lies_btw_140_160_sbp = None, None, None, None
        Cumulative_Percentage_less_than_five_lies_btw_140_160_sbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_140_160_sbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_140_160_sbp = None, None, None

    test_df_greater_than_160_sbp_1 = test_df[test_df["Calc_SBP"] >= 160]
    if len(test_df_greater_than_160_sbp_1) > 0:
        number_of_user_id_test_df_greater_than_160 = len(test_df_greater_than_160_sbp_1.USR_ID.unique())
        number_of_msr_id_test_df_greater_than_160 = len(test_df_greater_than_160_sbp_1.MSR_ID.unique())
        Mean_absolute_error_greater_than_160_sbp, mape_lies_greater_than_160_sbp, mean_deviation_greater_than_160_sbp, \
            std_dev_greater_than160_sbp = error_calculation_sbp_without_GE_error(test_df_greater_than_160_sbp_1)
        Cumulative_Percentage_less_than_five_greater_than_sbp, \
            Cumulative_Percentage_less_than_ten_greater_than_160_sbp, \
            Cumulative_Percentage_less_than_fifteen_greater_than_160_sbp = \
            sbp_accuracy_without_GE_error(test_df_greater_than_160_sbp_1)
    else:
        number_of_user_id_test_df_greater_than_160 = 0
        number_of_msr_id_test_df_greater_than_160 = 0
        Mean_absolute_error_greater_than_160_sbp, mape_lies_greater_than_160_sbp, mean_deviation_greater_than_160_sbp, \
            std_dev_greater_than160_sbp = None, None, None, None
        Cumulative_Percentage_less_than_five_greater_than_sbp, \
            Cumulative_Percentage_less_than_ten_greater_than_160_sbp, \
            Cumulative_Percentage_less_than_fifteen_greater_than_160_sbp = None, None, None

    test_df_less_than_80_dbp_1 = test_df[test_df["Calc_DBP"] < 80]
    if len(test_df_less_than_80_dbp_1) > 0:
        number_of_user_id_test_df_less_than_80_dbp = len(test_df_less_than_80_dbp_1.USR_ID.unique())
        number_of_msr_id_test_df_less_than_80_dbp = len(test_df_less_than_80_dbp_1.MSR_ID.unique())
        Mean_absolute_error_less_than_80_dbp, mape_less_than_80_dbp, mean_deviation_less_than_80_dbp, \
            std_dev_less_than_80_dbp = error_calculation_sbp_without_GE_error(test_df_less_than_80_dbp_1)
        Cumulative_Percentage_less_than_five_less_than_80_dbp, Cumulative_Percentage_less_than_ten_less_than_80_dbp, \
            Cumulative_Percentage_less_than_fifteen_less_than_80_dbp = \
            sbp_accuracy_without_GE_error(test_df_less_than_80_dbp_1)
    else:
        number_of_user_id_test_df_less_than_80_dbp = 0
        number_of_msr_id_test_df_less_than_80_dbp = 0
        Mean_absolute_error_less_than_80_dbp, mape_less_than_80_dbp, mean_deviation_less_than_80_dbp, \
            std_dev_less_than_80_dbp = None, None, None, None
        Cumulative_Percentage_less_than_five_less_than_80_dbp, Cumulative_Percentage_less_than_ten_less_than_80_dbp, \
            Cumulative_Percentage_less_than_fifteen_less_than_80_dbp = None, None, None

    test_df_lies_btw_80_90_dbp_1 = test_df[(test_df['Calc_DBP'] >= 80) & (test_df['Calc_DBP'] < 90)]
    if len(test_df_lies_btw_80_90_dbp_1) > 0:
        number_of_user_id_test_df_lies_btw_80_90_dbp = len(test_df_lies_btw_80_90_dbp_1.USR_ID.unique())
        number_of_msr_id_test_df_lies_btw_80_90_dbp = len(test_df_lies_btw_80_90_dbp_1.MSR_ID.unique())
        Mean_absolute_error_lies_btw_80_90_dbp, mape_lies_btw_80_90_dbp, mean_deviation_lies_btw_80_90_dbp, \
            std_dev_lies_btw_80_90_dbp = error_calculation_sbp_without_GE_error(test_df_lies_btw_80_90_dbp_1)
        Cumulative_Percentage_less_than_five_lies_btw_80_90_dbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_80_90_dbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_80_90_dbp = \
            sbp_accuracy_without_GE_error(test_df_lies_btw_80_90_dbp_1)
    else:
        number_of_user_id_test_df_lies_btw_80_90_dbp = 0
        number_of_msr_id_test_df_lies_btw_80_90_dbp = 0
        Mean_absolute_error_lies_btw_80_90_dbp, mape_lies_btw_80_90_dbp, mean_deviation_lies_btw_80_90_dbp, \
            std_dev_lies_btw_80_90_dbp = None, None, None, None
        Cumulative_Percentage_less_than_five_lies_btw_80_90_dbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_80_90_dbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_80_90_dbp = None, None, None

    test_df_lies_btw_90_100_dbp_1 = test_df[(test_df['Calc_DBP'] >= 90) & (test_df['Calc_DBP'] < 100)]
    if len(test_df_lies_btw_90_100_dbp_1) > 0:
        number_of_user_id_test_df_lies_btw_90_100_dbp = len(test_df_lies_btw_90_100_dbp_1.USR_ID.unique())
        number_of_msr_id_test_df_lies_btw_90_100_dbp = len(test_df_lies_btw_90_100_dbp_1.MSR_ID.unique())
        Mean_absolute_error_lies_btw_90_100_dbp, mape_lies_btw_90_100_dbp, mean_deviation_lies_btw_90_100_dbp, \
            std_dev_lies_btw_90_100_dbp = error_calculation_sbp_without_GE_error(test_df_lies_btw_90_100_dbp_1)
        Cumulative_Percentage_less_than_five_lies_btw_90_100_dbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_90_100_dbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_90_100_dbp = \
            sbp_accuracy_without_GE_error(test_df_lies_btw_90_100_dbp_1)
    else:
        number_of_user_id_test_df_lies_btw_90_100_dbp = 0
        number_of_msr_id_test_df_lies_btw_90_100_dbp = 0
        Mean_absolute_error_lies_btw_90_100_dbp, mape_lies_btw_90_100_dbp, mean_deviation_lies_btw_90_100_dbp, \
            std_dev_lies_btw_90_100_dbp = None, None, None, None
        Cumulative_Percentage_less_than_five_lies_btw_90_100_dbp, \
            Cumulative_Percentage_less_than_ten_lies_btw_90_100_dbp, \
            Cumulative_Percentage_less_than_fifteen_lies_btw_90_100_dbp = None, None, None

    test_df_greater_than_100_dbp_1 = test_df[test_df["Calc_DBP"] >= 100]
    if len(test_df_greater_than_100_dbp_1) > 0:
        number_of_user_id_test_df_greater_than_100_dbp = len(test_df_greater_than_100_dbp_1.USR_ID.unique())
        number_of_msr_id_test_df_greater_than_100_dbp = len(test_df_greater_than_100_dbp_1.MSR_ID.unique())
        Mean_absolute_error_greater_than_100_dbp, mape_greater_than_100_dbp, mean_deviation_greater_than_100_dbp, \
            std_dev_greater_than_100_dbp = error_calculation_sbp_without_GE_error(test_df_greater_than_100_dbp_1)
        Cumulative_Percentage_less_than_five_greater_than_100_dbp, \
            Cumulative_Percentage_less_than_ten_greater_than_100_dbp, \
            Cumulative_Percentage_less_than_fifteen_greater_than_100_dbp = \
            sbp_accuracy_without_GE_error(test_df_greater_than_100_dbp_1)
    else:
        number_of_user_id_test_df_greater_than_100_dbp = 0
        number_of_msr_id_test_df_greater_than_100_dbp = 0
        Mean_absolute_error_greater_than_100_dbp, mape_greater_than_100_dbp, mean_deviation_greater_than_100_dbp, \
            std_dev_greater_than_100_dbp = None, None, None, None
        Cumulative_Percentage_less_than_five_greater_than_100_dbp, \
            Cumulative_Percentage_less_than_ten_greater_than_100_dbp, \
            Cumulative_Percentage_less_than_fifteen_greater_than_100_dbp = None, None, None

    data1 = {'': ["MODEL INFORMATION", "No of USERID in  Model data", "No of MSRID in Model data",

                  "Any important details on this(if applicable)"],
             ' ': ['', Number_of_userid_train_data, Number_of_msrid_train_data,
                   'Min SBP-' + str(train_data_min_sbp) + " ,  " + 'Max SBP-' + str(
                       train_data_max_sbp) + " ,  " + 'Min DBP-' + str(train_data_min_dbp) + " ,  " + 'Max DBP-' + str(
                       train_data_max_dbp)]}

    data2 = {'': ["TEST DATA INFORMATION", "No of USERID in Test data", "No of MSRID in Test data",
                  "Any important details on this(if applicable)", " "],
             ' ': [' ', Number_of_userid_test_data, Number_of_msrid_test_data,
                   'Min SBP-' + str(test_data_min_sbp) + " ,  " + 'Max SBP-' + str(
                       test_data_max_sbp) + " ,  " + 'Min DBP-' + str(test_data_min_dbp) + " ,  " + 'Max DBP-' + str(
                       test_data_max_dbp), '']}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    merged_df = pd.concat([df1, df2], axis=0)
    merged_df = merged_df.reset_index()
    merged_df.drop('index', axis=1, inplace=True)
    info_df = merged_df

    data4 = {'ACCURACY INFORMATION': ["", " ", "SBP", "DBP", " ", "SBP Males", "SBP Females", " ", "SBP Normal",
                                      "SBP Pre-hypertension", "SBP Stage 1 Hypertension", "SBP Stage 2 Hypertension",
                                      " ", "DBP Normal", "DBP Pre-hypertension", "DBP Stage 1 Hypertension",
                                      "DBP Stage 2 Hypertension"],
             ' ': ['', '', 'For all MSRID', 'For all MSRID', ' ', 'For Males only', 'For Females only', '', '<120',
                   '120-139', '140-160', '>160', '', '<80', '80-89', '90-100', '>100'],
             '  ': ['', 'No of USERID', Number_of_userid_test_data, Number_of_userid_test_data, ' ',
                    number_of_user_id_male_test, number_of_user_id_female_test, ' ',
                    number_of_user_id_test_df_less_than_120_sbp, number_of_user_id_test_df_lies_btw_120_140_sbp,
                    number_of_user_id_test_df_lies_btw_140_160_sbp, number_of_user_id_test_df_greater_than_160, ' ',
                    number_of_user_id_test_df_less_than_80_dbp, number_of_user_id_test_df_lies_btw_80_90_dbp,
                    number_of_user_id_test_df_lies_btw_90_100_dbp, number_of_user_id_test_df_greater_than_100_dbp],
             '   ': ['', 'No of MSRID', Number_of_msrid_test_data, Number_of_msrid_test_data, ' ',
                     number_of_msr_id_male_test, number_of_msr_id_female_test, ' ',
                     number_of_msr_id_test_df_less_than_120_sbp, number_of_msr_id_test_df_lies_btw_120_140_sbp,
                     number_of_msr_id_test_df_lies_btw_140_160_sbp, number_of_msr_id_test_df_greater_than_160,
                     ' ', number_of_msr_id_test_df_less_than_80_dbp,
                     number_of_msr_id_test_df_lies_btw_80_90_dbp, number_of_msr_id_test_df_lies_btw_90_100_dbp,
                     number_of_msr_id_test_df_greater_than_100_dbp],
             '    ': ['Mean Absolute Deviation (MAD in mmHg)', ' ', Mean_absolute_error_sbp, Mean_absolute_error_dbp,
                      ' ', Mean_absolute_error_sbp_male, Mean_absolute_error_sbp_female, '',
                      Mean_absolute_error_less_than_120_sbp, Mean_absolute_error_lies_btw_120_140_sbp,
                      Mean_absolute_error_lies_btw_140_160_sbp, Mean_absolute_error_greater_than_160_sbp,
                      '', Mean_absolute_error_less_than_80_dbp,
                      Mean_absolute_error_lies_btw_80_90_dbp, Mean_absolute_error_lies_btw_90_100_dbp,
                      Mean_absolute_error_greater_than_100_dbp],
             '     ': ['Mean Absolute percentage Deviation (MAPD in %)', '', mape_sbp, mape_dbp, ' ', mape_sbp_male,
                       mape_sbp_female, '', mape_less_than_120_sbp, mape_lies_btw_120_140_sbp,
                       mape_lies_btw_140_160_sbp, mape_lies_greater_than_160_sbp,
                       '', mape_less_than_80_dbp, mape_lies_btw_80_90_dbp, mape_lies_btw_90_100_dbp,
                       mape_greater_than_100_dbp],
             '      ': ['Mean Deviation (MD in mmHg)', ' ', mean_deviation_sbp, mean_deviation_dbp, ' ',
                        mean_deviation_sbp_male, mean_deviation_sbp_female, '', mean_deviation_less_than_120_sbp,
                        mean_deviation_lies_btw_120_140_sbp, mean_deviation_lies_btw_140_160_sbp,
                        mean_deviation_greater_than_160_sbp, '',
                        mean_deviation_less_than_80_dbp, mean_deviation_lies_btw_80_90_dbp,
                        mean_deviation_lies_btw_90_100_dbp, mean_deviation_greater_than_100_dbp],
             '       ': ['Standard Deviation (SD in mmHg)', ' ', std_dev_sbp, std_dev_dbp, ' ', std_dev_sbp_male,
                         std_dev_sbp_female, '', std_dev_less_than_120_sbp, std_dev_lies_btw_120_140_sbp,
                         std_dev_lies_btw_140_160_sbp, '', '', std_dev_less_than_80_dbp, std_dev_lies_btw_80_90_dbp,
                         std_dev_lies_btw_90_100_dbp, std_dev_greater_than_100_dbp],
             '        ': ['Cumulative Percentage 5 (CP5)', 'Cumulative % of MSRID with error below 5 mmHG',
                          Cumulative_Percentage_sbp_less_than_five, Cumulative_Percentage_dbp_less_than_five, ' ',
                          Cumulative_Percentage_sbp_less_than_five_male,
                          Cumulative_Percentage_sbp_less_than_five_female, '',
                          Cumulative_Percentage_less_than_five_less_than_120_sbp,
                          Cumulative_Percentage_less_than_five_lies_btw_120_140_sbp,
                          Cumulative_Percentage_less_than_five_lies_btw_140_160_sbp,
                          Cumulative_Percentage_less_than_five_greater_than_sbp, '',
                          Cumulative_Percentage_less_than_five_less_than_80_dbp,
                          Cumulative_Percentage_less_than_five_lies_btw_80_90_dbp,
                          Cumulative_Percentage_less_than_five_lies_btw_90_100_dbp,
                          Cumulative_Percentage_less_than_five_greater_than_100_dbp],
             '         ': ['CP 10', 'Cumulative % of MSRID with error below 10 mmHG',
                           Cumulative_Percentage_sbp_less_than_ten, Cumulative_Percentage_dbp_less_than_ten, ' ',
                           Cumulative_Percentage_sbp_less_than_ten_male, Cumulative_Percentage_sbp_less_than_ten_female,
                           '', Cumulative_Percentage_less_than_ten_less_than_120_sbp,
                           Cumulative_Percentage_less_than_ten_lies_btw_120_140_sbp,
                           Cumulative_Percentage_less_than_ten_lies_btw_140_160_sbp,
                           Cumulative_Percentage_less_than_ten_greater_than_160_sbp, '',
                           Cumulative_Percentage_less_than_ten_less_than_80_dbp,
                           Cumulative_Percentage_less_than_ten_lies_btw_80_90_dbp,
                           Cumulative_Percentage_less_than_ten_lies_btw_90_100_dbp,
                           Cumulative_Percentage_less_than_ten_greater_than_100_dbp],
             '          ': ['CP 15', 'Cumulative % of MSRID with error below 15 mmHG',
                            Cumulative_Percentage_sbp_less_than_fifteen, Cumulative_Percentage_dbp_less_than_fifteen,
                            ' ', Cumulative_Percentage_sbp_less_than_fifteen_male,
                            Cumulative_Percentage_sbp_less_than_fifteen_female, '',
                            Cumulative_Percentage_less_than_fifteen_less_than_120_sbp,
                            Cumulative_Percentage_less_than_fifteen_lies_btw_120_140_sbp,
                            Cumulative_Percentage_less_than_fifteen_lies_btw_140_160_sbp,
                            Cumulative_Percentage_less_than_fifteen_greater_than_160_sbp, '',
                            Cumulative_Percentage_less_than_fifteen_less_than_80_dbp,
                            Cumulative_Percentage_less_than_fifteen_lies_btw_80_90_dbp,
                            Cumulative_Percentage_less_than_fifteen_lies_btw_90_100_dbp,
                            Cumulative_Percentage_less_than_fifteen_greater_than_100_dbp]}
    df4 = pd.DataFrame(data4)
    accuracy_df = df4

    return info_df, accuracy_df
