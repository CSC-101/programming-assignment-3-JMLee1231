import data
import build_data
import unittest
import data
import county_demographics
import build_data
import hw3

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total_empty_list(self):
        counties = []
        expected = 0
        result = hw3.population_total(counties)
        self.assertEqual(result, expected)

    def test_population_total_reduced_data(self):
        # Reduced data is already defined elsewhere in the file
        expected_population = 655813  # This should be the manually calculated total population

        # Call the population_total function
        result = hw3.population_total(reduced_data)

        # Assert that the result matches the expected population
        self.assertEqual(result, expected_population)

    # Part 2
    # test filter_by_state
    def test_filter_by_state(self):
        # Assuming `reduced_data` is the list of counties for testing
        california_counties = hw3.filter_by_state(reduced_data, "CA")

        # Verify that the list contains counties only from California
        for county in california_counties:
            self.assertEqual(county.state, "CA")

        # Check the expected number of counties for California
        self.assertEqual(len(california_counties), 2)  # Adjust based on your reduced_data

    def test_filter_by_state_no_match(self):
        # Test for a state that doesn't exist in the list
        texas_counties = hw3.filter_by_state(reduced_data, "TX")
        self.assertEqual(texas_counties, [])
    # Part 3
    # test population_by_education
    def test_population_by_education(self):

        result = hw3.population_by_education(reduced_data, "Bachelor's Degree or Higher")

        expected_result = 195114.091
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_population_by_education_no_match(self):
        # Test for an education level not present in the data
        result = hw3.population_by_education(reduced_data, "Master's Degree or Higher")
        self.assertEqual(result, 0.0)


    # test population_by_ethnicity


    def test_population_by_ethnicity_valid(self):
        # Sample reduced_data from your original data
        counties = reduced_data  # Assume `reduced_data` contains the sample county data
        ethnicity = "Black Alone"  # Example ethnicity
        expected = 25204.844  # This is the expected result for the "Black Alone" ethnicity
        result = hw3.population_by_ethnicity(counties, ethnicity)
        self.assertEqual(result, expected)

    def test_population_by_ethnicity_non_existent(self):
        counties = reduced_data  # Assume `reduced_data` contains the sample county data
        ethnicity = "Nonexistent Ethnicity"  # This ethnicity does not exist in the data
        expected = 0  # Since the ethnicity doesn't exist, the result should be 0
        result = hw3.population_by_ethnicity(counties, ethnicity)
        self.assertEqual(result, expected)

    # test population_below_poverty_level

    def test_population_below_poverty_level(self):
        counties = reduced_data
        # Calculate the expected result by manually summing up the populations below poverty level for each county
        expected = (55395 * 12.1 / 100) + (61697 * 20.2 / 100) + (279083 * 14.3 / 100) + (207590 * 19.1 / 100) + \
                   (2622 * 15.7 / 100) + (42225 * 18.4 / 100) + (7201 * 11.2 / 100)

        result = hw3.population_below_poverty_level(counties)
        self.assertEqual(result, expected)

    def test_population_below_poverty_level_empty(self):
        counties = []
        expected = 0  # No counties in the list, so the result should be 0
        result = hw3.population_below_poverty_level(counties)
        self.assertEqual(result, expected)

    # Part 4
    # test percent_by_education
    def test_percent_by_bachelors_degree(self):
        # The education level to test
        education_level = "Bachelor's Degree or Higher"

        # Call the function with reduced_data and the specified education level
        result = hw3.percent_by_education(reduced_data, education_level)

        # We expect a specific percentage based on the data
        expected_result = (  # Manually calculated or expected result based on data in reduced_data
                                  (55395 * 20.9) + (61697 * 14.3) + (279083 * 31.5) + (207590 * 37.9) + (2622 * 17.9) +
                                  (42225 * 15.2) + (7201 * 17.2)) / (
                                      55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201)

        # Assert that the result is within a small margin of error
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_percent_by_high_school_or_higher(self):
        # The education level to test
        education_level = "High School or Higher"

        # Call the function with reduced_data and the specified education level
        result = hw3.percent_by_education(reduced_data, education_level)

        # We expect a specific percentage based on the data
        expected_result = (  # Manually calculated or expected result based on data in reduced_data
                                  (55395 * 85.6) + (61697 * 82.2) + (279083 * 89.6) + (207590 * 84.3) + (
                                      2622 * 89.2) +
                                  (42225 * 81.8) + (7201 * 90.2)) / (
                                      55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201)

        # Assert that the result is within a small margin of error
        self.assertAlmostEqual(result, expected_result, places=2)
    # test percent_by_ethnicity

    def test_percent_by_black_alone(self):
        # The ethnicity to test
        ethnicity = "Black Alone"

        result = hw3.percent_by_ethnicity(reduced_data, ethnicity)

        expected_result = (
            (55395 * 18.7) + (61697 * 1.6) + (279083 * 2.2) + (207590 * 3.0) + (2622 * 0.2) +
            (42225 * 3.4) + (7201 * 0.7) ) / (55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201)

        self.assertAlmostEqual(result, expected_result, places=2)


    def test_percent_by_white_alone(self):
        # The ethnicity to test
        ethnicity = "White Alone"

        result = hw3.percent_by_ethnicity(reduced_data, ethnicity)

        expected_result = ((55395 * 77.9) + (61697 * 91.5) + (279083 * 89.0) + (207590 * 75.9) + (2622 * 96.1) +
                                  (42225 * 92.9) + (7201 * 95.0)) / (55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201)

        self.assertAlmostEqual(result, expected_result, places=2)
    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        result = hw3.percent_below_poverty_level(reduced_data)

        expected_result = ((55395 * 12.1) + (61697 * 20.2) + (279083 * 14.3) + (207590 * 19.1) + (2622 * 15.7) +
                                  (42225 * 18.4) + (7201 * 11.2)) / (55395 + 61697 + 279083 + 207590 + 2622 + 42225 + 7201)

        self.assertAlmostEqual(result, expected_result, places=2)

    def test_percent_below_poverty_level_case_2(self):
        result = hw3.percent_below_poverty_level([reduced_data[0], reduced_data[1]])
        expected_result = ((55395 * 12.1) + (61697 * 20.2)) / (55395 + 61697)
        self.assertAlmostEqual(result, expected_result, places=2)

    # Part 5
    # test education_greater_than
    def test_education_greater_than_25(self):
        result = hw3.education_greater_than(reduced_data, "Bachelor's Degree or Higher", 25.0)
        self.assertEqual(len(result), 2)
        for county in result:
            self.assertGreater(county.education["Bachelor's Degree or Higher"],
                               25.0)

            def test_education_greater_than_40(self):
                result = hw3.education_greater_than(reduced_data, "Bachelor's Degree or Higher", 40.0)

                self.assertEqual(len(result), 1)
                for county in result:
                    self.assertGreater(county.education["Bachelor's Degree or Higher"], 40.0)
    # test education_less_than

    def test_education_less_than_20(self):
        result = hw3.education_less_than(reduced_data, "Bachelor's Degree or Higher", 20.0)
        self.assertEqual(len(result), 4)
        for county in result:
            self.assertLess(county.education["Bachelor's Degree or Higher"],
                            20.0)

    def test_education_less_than_15(self):
        result = hw3.education_less_than(reduced_data, "Bachelor's Degree or Higher", 15.0)
        self.assertEqual(len(result), 1)
        for county in result:
            self.assertLess(county.education["Bachelor's Degree or Higher"], 15.0)

    # test ethnicity_greater_than

    def test_ethnicity_greater_than_10(self):
        result = hw3.ethnicity_greater_than(reduced_data, 'Hispanic or Latino', 10.0)

        self.assertEqual(len(result), 2)

        for county in result:
            self.assertGreater(county.ethnicities['Hispanic or Latino'], 10.0)

    def test_ethnicity_greater_than_5(self):
        result = hw3.ethnicity_greater_than(reduced_data, 'Black Alone', 5.0)

        self.assertEqual(len(result), 1)

        for county in result:
            self.assertGreater(county.ethnicities['Black Alone'], 5.0)
    # test ethnicity_less_than
    def test_ethnicity_less_than_5(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Black Alone', 5.0)

        self.assertEqual(len(result), 6)

        for county in result:
            self.assertLess(county.ethnicities['Black Alone'], 5.0)

    def test_ethnicity_less_than_2(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Asian Alone', 2.0)

        self.assertEqual(len(result), 5)

        for county in result:
            self.assertLess(county.ethnicities['Asian Alone'], 2.0)
    # test below_poverty_level_greater_than

    def test_below_poverty_level_greater_than_15(self):
        result = hw3.below_poverty_level_greater_than(reduced_data, 15.0)

        self.assertEqual(len(result), 4)

        for county in result:
            self.assertGreater(county.income['Persons Below Poverty Level'], 15.0)

    def test_below_poverty_level_greater_than_20(self):
        result = hw3.below_poverty_level_greater_than(reduced_data, 20.0)

        self.assertEqual(len(result), 1)

        for county in result:
            self.assertGreater(county.income['Persons Below Poverty Level'], 20.0)

    # test below_poverty_level_less_than


    def test_below_poverty_level_less_than_15(self):
        result = hw3.below_poverty_level_less_than(reduced_data, 15.0)

        self.assertEqual(len(result), 3)

        for county in result:
            self.assertLess(county.income['Persons Below Poverty Level'], 15.0)

    def test_below_poverty_level_less_than_20(self):
        result = hw3.below_poverty_level_less_than(reduced_data, 20.0)

        self.assertEqual(len(result), 6)

        for county in result:
            self.assertLess(county.income['Persons Below Poverty Level'], 20.0)


if __name__ == '__main__':
    unittest.main()
