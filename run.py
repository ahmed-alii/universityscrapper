from scraper import rankings as r


def main():
    country_list = r.get_countries()
    print(country_list)
    print("Here is the list of countries we have rankings for. \n\n Type the country name (without quotes):")
    country = input("Enter country name : ")
    if country in country_list:
        r.get_results(country)
        print("\n\n --- \n\n")
    else:
        print("You probably made a typo. Write the country name as-it-is.")


if __name__ == "__main__":
    main()
