import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    total_bachelor = df.loc[df['education'] == "Bachelors"].shape[0]
    percentage_bachelors = round((total_bachelor/total_people)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    df_50K = df.loc[df["salary"] == ">50K"]
    df_degree = df.loc[(df["education"] == "Bachelors") |
                        (df["education"] == "Masters") |
                        (df["education"] == "Doctorate")]
    total_50K = df_50K.shape[0]
    total_degree = df_degree.shape[0]
    total_degree_50K = df_degree.loc[df_degree["salary"] == ">50K"].shape[0]

    # What percentage of people without advanced education make more than 50K?
    total_no_degree = total_people - total_degree
    total_no_degree_50K = total_50K - total_degree_50K

    # percentage with salary >50K
    higher_education_rich = round((total_degree_50K/total_degree)*100, 1)
    lower_education_rich = round((total_no_degree_50K/total_no_degree)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours].shape[0]
    num_min_workers_50K = df.loc[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0]

    rich_percentage = round((num_min_workers_50K/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df["native-country"].unique()
    country_percent = {}
    for i in countries:
        total_country = (df["native-country"] == i).sum()
        total_country_50K = df.loc[(df["native-country"] == i) & (df["salary"] == ">50K")].shape[0]
        country_percent[i] = round((total_country_50K/total_country)*100, 1)

    highest_earning_country = max(country_percent, key=country_percent.get)
    highest_earning_country_percentage = country_percent[highest_earning_country]

    # Identify the most popular occupation for those who earn >50K in India.
    IN_50K = df.loc[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    IN_50K_occup = IN_50K["occupation"].value_counts()
    top_IN_occupation = IN_50K_occup.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
