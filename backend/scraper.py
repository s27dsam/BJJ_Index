import pandas as pd
from pytrends.request import TrendReq
from backend.crud import store_popularity_data


def scrap_google_trends_bjj_1():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["bjj"], cat=0, timeframe='today 5-y', geo='', gprop='')
    bjj_trend = pytrends.interest_over_time()
    bjj_trend = bjj_trend["bjj"]
    return bjj_trend


def scrap_google_trends_brazilian_jiu_jitsu_2():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["Brazilian jiu-jitsu"], cat=0, timeframe='today 5-y', geo='', gprop='')
    brazilian_jiu_jitsu_trend = pytrends.interest_over_time()
    brazilian_jiu_jitsu_trend = brazilian_jiu_jitsu_trend["Brazilian jiu-jitsu"]
    return brazilian_jiu_jitsu_trend


def scrap_google_trends_jujitsu_3():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["jujitsu"], cat=0, timeframe='today 5-y', geo='', gprop='')
    jujitsu_trend = pytrends.interest_over_time()
    jujitsu_trend = jujitsu_trend["jujitsu"]
    return jujitsu_trend


# Define the function to get overall average
def get_all_and_get_overall_average():
    # Get the individual trends data
    bjj_trend = scrap_google_trends_bjj_1()
    brazilian_jiu_jitsu_trend = scrap_google_trends_brazilian_jiu_jitsu_2()
    jujitsu_trend = scrap_google_trends_jujitsu_3()

    # Ensure that each trend DataFrame has 'date' and 'value' columns
    # If they are Series, convert them to DataFrames
    if isinstance(bjj_trend, pd.Series):
        bjj_trend = bjj_trend.reset_index()
        bjj_trend.columns = ['date', 'value']
    if isinstance(brazilian_jiu_jitsu_trend, pd.Series):
        brazilian_jiu_jitsu_trend = brazilian_jiu_jitsu_trend.reset_index()
        brazilian_jiu_jitsu_trend.columns = ['date', 'value']
    if isinstance(jujitsu_trend, pd.Series):
        jujitsu_trend = jujitsu_trend.reset_index()
        jujitsu_trend.columns = ['date', 'value']

    # Merge the DataFrames on the 'date' column
    combined_df = bjj_trend.merge(brazilian_jiu_jitsu_trend, on='date', suffixes=('_bjj', '_bjjj'))
    combined_df = combined_df.merge(jujitsu_trend, on='date')
    combined_df.rename(columns={'value': 'jujitsu'}, inplace=True)
    combined_df.rename(columns={'value_bjj': 'bjj', 'value_bjjj': 'brazilian_jiu_jitsu'}, inplace=True)

    # Calculate the average across the specified columns
    combined_df['average'] = combined_df[['bjj', 'brazilian_jiu_jitsu', 'jujitsu']].mean(axis=1).round(1)

    # Return the DataFrame matching the expected schema
    return combined_df[['date', 'bjj', 'brazilian_jiu_jitsu', 'jujitsu', 'average']]


# Example usage
popularity_data = get_all_and_get_overall_average()
# Store the data into the database
store_popularity_data(popularity_data)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Initialize the Selenium WebDriver (for example, using Chrome)
# driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
#
# # Open the webpage
# driver.get('https://ibjjf.com/certified-black-belts')
#
# # Wait for the page to load completely
# driver.implicitly_wait(10)  # Adjust as needed for slow page load
#
# # Locate the element containing the total number (adjust based on inspection)
# total_element = driver.find_element(By.CLASS_NAME, 'totals')
#
# # Extract and print the total value
# total_value = total_element.text
# print(total_value)  # Output should be '10090'
#
# # Close the browser
# driver.quit()
