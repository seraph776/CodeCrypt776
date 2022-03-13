# M5 The Election
# Adding font class for formatting my graph output
class font:
    BOLD = '\033[1m'
    RED = '\033[1;91m'  # This is actually "Red & bold" - this style will be used for my graph.
    BLUE = '\033['
    # YELLOW = '\033[1;47m' not used.
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Format escape


file = open("election.dat", "r")  # open 'file' in read-mode
lines = file.readlines()  # assign variable 'file' to 'lines' apply method .readlines()
fname = []  # Empty list to hold First Name
lname = []  # Empty list to hold Last Name
district = []  # Empty list to District
votes = []  # Empty list to hold Votes
for x in lines:
    fname.append(x.split(' ')[0])  # split list at index [0] and append to list fname
    lname.append(x.split(' ')[1])  # split list at index [1] and append to list lname
    district.append(x.split(' ')[2])  # split list at index [2] and append to list district
    votes.append(x.split(' ')[3])  # split list at index [3] and append to list votes
file.close()  # Close object
d1 = []  # Empty list for each district 1-10- this creates a list for my while loop to cycle thru.
d2 = []
d3 = []
d4 = []
d5 = []
d6 = []
d7 = []
d8 = []
d9 = []
d10 = []
x = 0  # setting x to zero for the while loop
while x < len(lines):  # This while loop cycles through the list of 'districts' sorting them by their district numbers
    if int(district[
               x]) == 1:  # while 'district' is equal to each set parameter then append to list (in this line of code then append to list d1) - so on and so forth.
        d1.append(lines[x])
    if int(district[x]) == 2:
        d2.append(lines[x])
    if int(district[x]) == 3:
        d3.append(lines[x])
    if int(district[x]) == 4:
        d4.append(lines[x])
    if int(district[x]) == 5:
        d5.append(lines[x])
    if int(district[x]) == 6:
        d6.append(lines[x])
    if int(district[x]) == 7:
        d7.append(lines[x])
    if int(district[x]) == 8:
        d8.append(lines[x])
    if int(district[x]) == 9:
        d9.append(lines[x])
    if int(district[x]) == 10:
        d10.append(lines[x])
    x += 1

votes1 = 0  # Setting vote counts (1-10) equal to zero.
votes2 = 0
votes3 = 0
votes4 = 0
votes5 = 0
votes6 = 0
votes7 = 0
votes8 = 0
votes9 = 0
votes10 = 0

winner1 = 0  # Setting winner counts (1-10) equal to zero.
winner2 = 0
winner3 = 0
winner4 = 0
winner5 = 0
winner6 = 0
winner7 = 0
winner8 = 0
winner9 = 0
winner10 = 0
winners = [None] * 10  # Fail-safe if there are no winners

x = 0
for x in d1:  # each subsequent for-loop will cycle thru the data at index [3] ('vote count') and will generate the 'winners count' per district (1-10)
    votes1 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner1:  # counting votes - if integer at 'votes' index greater than
        winner1 = int(x.split(' ')[3])
        winners[0] = x.split(' ')[0] + ' ' + x.split(' ')[
            1]  # this line appends index [0] & [1] together ('first & last name') to the list of 'winners'
for x in d2:
    votes2 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner2:
        winner2 = int(x.split(' ')[3])
        winners[1] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d3:
    votes3 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner3:
        winner3 = int(x.split(' ')[3])
        winners[2] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d4:
    votes4 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner4:
        winner4 = int(x.split(' ')[3])
        winners[3] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d5:
    votes5 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner5:
        winner5 = int(x.split(' ')[3])
        winners[4] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d6:
    votes6 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner6:
        winner6 = int(x.split(' ')[3])
        winners[5] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d7:
    votes7 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner7:
        winner7 = int(x.split(' ')[3])
        winners[6] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d8:
    votes8 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner8:
        winner8 = int(x.split(' ')[3])
        winners[7] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d9:
    votes9 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner9:
        winner9 = int(x.split(' ')[3])
        winners[8] = x.split(' ')[0] + ' ' + x.split(' ')[1]
for x in d10:
    votes10 += int(x.split(' ')[3])
    if int(x.split(' ')[3]) > winner10:
        winner10 = int(x.split(' ')[3])
        winners[9] = x.split(' ')[0] + ' ' + x.split(' ')[1]

# This is printed data of the 'total vote count' per district.
print(font.BOLD + font.UNDERLINE + "Total Score by District:" + font.END, "\n",
      # font.BOLD/font.END is new technique I found to alter font.
      "\nDistrict 1: ", votes1,
      "\nDistrict 2: ", votes2,
      "\nDistrict 3: ", votes3,
      "\nDistrict 4: ", votes4,
      "\nDistrict 5: ", votes5,
      "\nDistrict 6: ", votes6,
      "\nDistrict 7: ", votes7,
      "\nDistrict 8: ", votes8,
      "\nDistrict 9: ", votes9,
      "\nDistrict 10:", votes10, "\n")
# print(winners,'\n') #- Just prints the winners names. Commented out because I didn't like the formatting.


print(font.BOLD + font.UNDERLINE + "Election Results by District!" + font.END + "\n")  # Making font Bold here.

# This is my attempt at something "fancy for a BONUS" - This is a trick I worked on to print the percentage in a graph form.
# I'm printing ("|") multiplied by (percent formula). I'm also dividing it by 2 again only to reduce the 'print-out size' of the graph by half - Adding Red formmating t o make graph stand out.
print(
    font.UNDERLINE + "District 1:" + font.END,
    winners[0].title() + ": " + font.RED + "|" * int(winner1 / votes1 * 100 / 2) + font.END,
    round(winner1 / votes1 * 100, 2), '%',
    # I'm also using .title() for formatting to get rid of all the CAPS from the raw data.
    font.UNDERLINE + "\nDistrict 2:" + font.END,
    winners[1].title() + ": " + font.RED + "|" * int(winner2 / votes2 * 100 / 2) + font.END,
    round(winner2 / votes2 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 3:" + font.END,
    winners[2].title() + ": " + font.RED + "|" * int(winner3 / votes3 * 100 / 2) + font.END,
    round(winner3 / votes3 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 4:" + font.END,
    winners[3].title() + ": " + font.RED + "|" * int(winner4 / votes4 * 100 / 2) + font.END,
    round(winner4 / votes4 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 5:" + font.END,
    winners[4].title() + ": " + font.RED + "|" * int(winner5 / votes5 * 100 / 2) + font.END,
    round(winner5 / votes5 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 6:" + font.END,
    winners[5].title() + ": " + font.RED + "|" * int(winner6 / votes6 * 100 / 2) + font.END,
    round(winner6 / votes6 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 7:" + font.END,
    winners[6].title() + ": " + font.RED + "|" * int(winner7 / votes7 * 100 / 2) + font.END,
    round(winner7 / votes7 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 8:" + font.END,
    winners[7].title() + ": " + font.RED + "|" * int(winner8 / votes8 * 100 / 2) + font.END,
    round(winner8 / votes9 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 9:" + font.END,
    winners[8].title() + ": " + font.RED + "|" * int(winner9 / votes9 * 100 / 2) + font.END,
    round(winner9 / votes9 * 100, 2), '%',
    font.UNDERLINE + "\nDistrict 10:" + font.END,
    winners[9].title() + ": " + font.RED + "|" * int(winner10 / votes10 * 100 / 2) + font.END,
    round(winner10 / votes10 * 100, 2), '%'
)
