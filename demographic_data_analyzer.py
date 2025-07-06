import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. Race count
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors degrees
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education
    higher_education = df[df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum() / len(higher_education) * 100, 1)
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

    # 5. Min work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich percentage among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1)

    # 7. Country with highest % of rich people
    country_rich_percentage = (
        df[df['salary'] == '>50K']['native-country'].value_counts() /
        df['native-country'].value_counts() * 100
    ).dropna()
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # 8. Most popular occupation for rich in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # Return results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among min workers:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupation in India for those earning >50K:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
