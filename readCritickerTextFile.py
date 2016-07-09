# Test of puthon to read files

# Necessary imports
import urllib as urllib

def main():

    # Download text file
    urllib.urlretrieve("https://www.criticker.com/resource/rankings/conv.php?userid=38891&type=txt&filter=", "./rankings.txt")

    # Define File to read as the one just downloaded
    fileToRead = "rankings.txt"

    # Open file and read in all lines
    fileStream = open( fileToRead, "r" )
    allLines = fileStream.readlines()
    fileStream.close()

    # Initialize new entry flag
    newEntryFound = False

    # Initialize all entries array
    allEntries = []

    for currentLine in allLines:
        # Get rid of new line charcter
        currentLine = currentLine.strip()

        # If the line is empty, then we've reached the end of the entry
        if (not currentLine):
            newEntryFound = False
            continue
        #

        # Check if we've found a line with a parenthesis 
        parenIndex = currentLine.rfind("(")
    
        # If we have found one, and we haven't yet found a new entry, parse the
        # ranking, title, and year
        if (parenIndex >= 0) & (not newEntryFound):
            # Indicate that we've found a new entry
            newEntryFound = True
            newEntry = { "Title":"", "Year":0, "Rating":"", "Summary":"" }

            # Find the tab between the year and the title
            tabIndex = currentLine.find("\t")
            if (not tabIndex):
                continue # go to the next line if we have no tabs
            #

            # Find the rating, year, and title
            ratingString = currentLine[:tabIndex]
            titleString = currentLine[tabIndex+1:parenIndex-1] 
            yearString = currentLine[parenIndex+1:parenIndex+5]
            
            # Store data to entry 
            newEntry["Title"] = titleString
            newEntry["Year"] = int(yearString)
            newEntry["Rating"] = int(ratingString)            # 

            # Append new entry to array
            allEntries.append( newEntry )
            print( ratingString + " " + titleString + ", " + yearString )
        
        #


    #
#

main() 
