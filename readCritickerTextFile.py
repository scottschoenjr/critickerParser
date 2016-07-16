# Test of Python to read files

# Necessary imports
import urllib # For download of Criticker file
import sys    # Command line inputs
import getopt # Support command line options parsing
import math   # Math functions

def main(argv):

    # Download text file
    urllib.urlretrieve("https://www.criticker.com/resource/rankings/conv.php?userid=38891&type=txt&filter=", "./rankings.txt")

    # Define File to read as the one just downloaded
    fileToRead = "rankings.txt"

    # Open file and read in all lines
    fileStream = open( fileToRead, "r" )
    allLines = fileStream.readlines()
    fileStream.close()

    # Get the number of entries to print to file
    startYear = "1850"
    endYear = "2500"
    numPrint = "1000000"
    try:
        options, argument = getopt.getopt(argv,"hs:e:n:", ["startyear=", "endyear=", "numbertoprint="])
    except getopt.GetoptError:
        print( "Options are -s <startyear> -e <endyear> -n <number>" )
        sys.exit(2)
    #
    for option, argument in options:
        if option == '-h':
            print( "Options are -s <startyear> -e <endyear> -n <numbertosave>" )
            sys.exit()
        elif option in ( "-s", "--startyear" ):
            startYearString = argument
            startYear = int( math.floor( float( startYearString ) ) )
        elif option in ( "-e", "--endyear" ):
             endYearString = argument
             endYear = int( math.floor( float( endYearString ) ) )
        elif option in ( "-n", "--numbertoprint" ):
             numPrintString = argument
             numPrint = int( math.floor( float( numPrintString ) ) )
        #
    #
    print( "Saving the top " + numPrint + " movies between " + startYear + " and " + endYear + "." )

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
        #
    #

    # Ensure the bounds and values are appropriate
    if ( startYear < endYear ):
        startYear, endYear = endYear, startYear
    #

    # Find all the years that fall in the approriate range
    validEntryInds = []
    indCount = -1
    for entry in allEntries:
        indCount = indCount + 1
        afterStartYear = ( entry["Year"] >= startYear ) 
        beforeEndYear = ( entry["Year"] <= endYear )
        if ( afterStartYear and beforeEndYear ):
            validEntryInds.append(indCount)
        #
    #
    validEntries = [ allEntries[count] for count in  validEntryInds ]    

    # Print valid entries
    for entry in validEntries:
        print( entry["Year"] + " " + entry["Title"] )
    #

     
#


if __name__ == "__main__":
    main(sys.argv[1:])
#
