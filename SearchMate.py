import webbrowser

# Function to automate searching for people based on a list of names and a follow-up string (e.g., organization or community)
def search_names(names_string):
    # Split the input names string by commas to get individual names
    names = names_string.split(',')
    
    # Iterate through each name to process it individually
    for name in names:
        # Clean each name by stripping extra spaces from the beginning and end
        name = name.strip()
        
        # Combine the name with the follow-up string to form the search query
        query = f"{name} {followup}"
        
        # Open the default web browser and search for the query on Google
        webbrowser.open(f"https://www.google.com/search?q={query}")

# Main code to get user input for the follow-up string and the list of names
followup = input("Enter a string that the query should be followed by: ")
names_input = input("Enter names separated by commas (usually a noun): ")

# Call the function to search for the profiles of the entered names
search_names(names_input)