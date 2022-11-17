year_interest = int(input("Enter the year of interest: "))
country_interest = input("Enter the country of interest: ")
print()

with open("life-expectancy.csv") as life_expectancy:
    max_life_expectancy = 0
    min_life_expectancy = 99999
    max_entity = ""
    min_entity = ""
    max_year = 0
    min_year = 99999

    #Year of interest
    total = 0
    counter = 0
    max_year_interest_life = 0
    min_year_interest_life = 99999
    max_year_interest_entity = ""
    min_year_interest_entity = ""

    #Country of interest
    total_country = 0
    counter_country = 0
    max_country_life = 0
    min_country_life = 99999
    max_country_year = 0
    min_country_year = 99999
    
    
    for line in life_expectancy:

        line_separeted = line.strip()
        line_separeted = line.split(",")
        
        if not (line.startswith("Entity")):

            # Parts: Entity,Code,Year,Life expectancy (years)
            entity = line_separeted[0]
            code = line_separeted[1]
            year = int(line_separeted[2])
            life_expectancy_years = float(line_separeted[3])
 
            #calculating max and min
            if max_life_expectancy < life_expectancy_years:
                max_life_expectancy = life_expectancy_years
                max_entity = entity
                max_year = year

            if min_life_expectancy > life_expectancy_years:
                min_life_expectancy = life_expectancy_years
                min_entity = entity
                min_year = year

           #year of interest 
           #Calculating average 
            if year_interest == year:
                total += life_expectancy_years #sum
                counter += 1 #length
                
                #Max and min life expectancy year interest
                if max_year_interest_life < life_expectancy_years:
                    max_year_interest_life = life_expectancy_years
                    max_year_interest_entity = entity

                if min_year_interest_life > life_expectancy_years:
                    min_year_interest_life = life_expectancy_years
                    min_year_interest_entity = entity
               
            #country of interest
            if country_interest.lower() == entity.lower():
                total_country += life_expectancy_years
                counter_country += 1

                if max_country_life < life_expectancy_years:
                    max_country_life = life_expectancy_years
                    max_country_year = year
                
                if min_country_life > life_expectancy_years:
                    min_country_life = life_expectancy_years
                    min_country_year = year

    average = total / counter
    average_country = total_country / counter_country

    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_entity} in {max_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_entity} in {min_year}")
    print()

    print(f"For the year {year_interest}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {max_year_interest_entity} with {max_year_interest_life} ")
    print(f"The min life expectancy was in {min_year_interest_entity} with {min_year_interest_life} ")
    print()

    print(f"For the country {country_interest}:")
    print(f"The average life expectancy across all years was {average_country:.2f}")
    print(f"The max life expectancy was {max_country_life} in {max_country_year} ")
    print(f"The min life expectancy was {min_country_life} in {min_country_year} ")
    print()

    

    
    
