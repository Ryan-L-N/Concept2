#import libraries
from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.concept2.com/indoor-rowers/training/wod/workout/nojs/random/short/rower"
directory  = r"C:\Users\ryan.neville\Desktop\Visual Studio Code\Concept2 Project\Final\Concept2WorkoutsList.txt"


for i in range(100):
    try:
        page = urllib.request.urlopen(url)
    except:
        print("An error occured.")

    soup = BeautifulSoup(page, 'html.parser')
    # print(soup)

    #Parse the entire HTML Section you are interested in. Store this in the variable "results"
    results = soup.find(id="wod-short")
    pretty_results = results.prettify()

    #Further parse the html using the .find method.  Store this as the workout
    workout = results.find("h4")
    description = results.find("p", class_="light")
    print(workout)
    print(description)

    #Use prettify to turn workout into a string so it can be written to a file
    pretty_workout = workout.prettify()
    pretty_description = description.prettify()


    print(pretty_results)
    print(pretty_workout)
    print(pretty_description)


    #Get the text of the workout with indices.  Remove escape characters and extra space that sneaks in to the string somehow
    start_workout_index = pretty_workout.find('>')
    end_workout_index = pretty_workout.rfind('<')
    workout_string = pretty_workout[start_workout_index+1:-6]
    workout_string_spaceless = workout_string.replace('\n','')
    workout_text = workout_string_spaceless.replace(' ', '',1)
    workout_text_with_semicolon = workout_text + ";"



    #Find the indices and use these to extract text for description
    start_description_index = pretty_description.find('>')
    end_description_index = pretty_description.rfind('<', start_description_index)
    description_string = pretty_description[start_description_index+1: -5]
    description_string_spaceless = description_string.replace('\n','')
    description_text = description_string_spaceless.replace(' ', '',1)
    description_text_with_semicolon = description_text + ";"


    #To get the button sequence, a different method needed to be used.
    #Using the rfind method, the index of the beginning of the string can be found and stored in start_button_index
    #Using this index, the end of the string can be found and stored in end_button_index
    start_button_index = pretty_results.rfind(':')
    end_button_index = pretty_results.find('<', start_button_index)

    # print(start_button_index)
    # print(end_button_index)

    #Using those indices, the button_sequence can be extracted from pretty_results
    button_sequence_text = pretty_results[start_button_index+2:end_button_index]
    button_sequence_spaceless = button_sequence_text.replace('\n','')
    button_sequence_text_with_semicolon = button_sequence_spaceless + ";"




    # print(workout_text)
    # print(description_text)
    # print(button_sequence_text)


    with open(directory, 'a') as file:
        file.write(workout_text_with_semicolon)
        file.write(description_text_with_semicolon)
        file.write(button_sequence_text_with_semicolon)
        file.write("Short; \n")
