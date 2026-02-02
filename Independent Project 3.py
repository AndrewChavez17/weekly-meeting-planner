# Andrew Chavez
# Independent Project 3
# Python meeting planner project created for coursework
# This program lets the user set up a number of weekly meetings and assign each of them a leader name and a topic

# Function definition: AssignMeetings
# Function purpose: Assigns the leader and topic to a meeting week
# Arguments: List of leaders, list of topics, and the meeting number
# Return value: Returns nothing
def AssignMeetings (LeaderList,TopicsList, MeetingNumber):
    LeaderName = input("What is the leader's name? ")
    LeaderList[MeetingNumber] = LeaderName
    MeetingTopic = input("What is the topic for the week? " )
    TopicsList[MeetingNumber] = MeetingTopic

# Function definition: PrintMeetings
# Function purpose: Shows all open and assigned meetings to the user. Will only show open meetings if the user requests to.
# Arguments: List of leaders, list of topics, and boolean value of OnlyOpen
# Return value: Displays the meetings
def PrintMeetings (LeaderList,TopicsList, OnlyOpen=False):
    for i in range(len(LeaderList)):
        Leader = LeaderList[i]
        Topic = TopicsList[i]
        if OnlyOpen == False:
            print("Meeting", i, ": " + Leader, Topic)
        elif Leader == "Open" and Topic == "Unplanned":
            print("Meeting", i, ": " + Leader, Topic)
        
# Defining name and topic list
LeaderNames = []
MeetingTopics = []

print("Welcome to the UMW meeting planner")

# Grabs the number of meetings
NmbrOfMeetings = int(input("How many meetings will you have? "))

# Sets the amount of open and unplanned meetings
for y in range(NmbrOfMeetings):
    LeaderNames.append("Open")
    MeetingTopics.append("Unplanned")


NmbrOfAssignedWeeks = 0

print("")

# Gives the user four options to choose from and will loop until all
# weeks are assigned or if the user chooses to quit the program
while NmbrOfAssignedWeeks != NmbrOfMeetings:
    print("A: Assign a person to lead a week and enter the week's topic")
    print("L: Print a list of all of the meetings information")
    print("O: Print a list of all of the 'Open' meetings")
    print("Q: Quit the program:")
    response = input("What would you like to do next? ")
    
    # Asks the user for which meeting number and uses the AssignMeeting function
    if response == "A":
        MeetingNmbr = int(input("Which week do you want to assign a leader to? "))
        AssignMeetings(LeaderNames, MeetingTopics, MeetingNmbr)
        print ("")
        NmbrOfAssignedWeeks+=1
        
    # Displays all meetings whether assigned or open
    elif response == "L":
        PrintMeetings(LeaderNames, MeetingTopics, False)
        print ("")
        
    # Displays only open meetings
    elif response == "O":
        PrintMeetings(LeaderNames, MeetingTopics, True)
        print ("")
        
    # Allows the user to exit the program
    elif response == "Q":
        print ("")
        break

# Shows the user all of their assigned meetings or all meetings if the
# user decided to exit out of the program early
if NmbrOfAssignedWeeks == NmbrOfMeetings:
    print("All of the meetings have been assigned!")
    PrintMeetings(LeaderNames, MeetingTopics, False)
    print ("")
    print("Thanks for using the program!")
    
else:
    print("Here is a list of all assigned and open meetings!")
    PrintMeetings(LeaderNames, MeetingTopics, False)
    print ("")
    print("Thanks for using the program!")

