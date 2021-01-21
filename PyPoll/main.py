from statistics import mean
import os
import csv

elect_csv = os.path.join('Resources', 'election_data.csv')
write_csv = os.path.join('Analysis', 'output.csv')

votes = 0
ballots = []

with open(elect_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for r in csvreader:

        votes +=1
        ballots.append(r[2])

def most_frequent(ballots):
    return max(set(ballots), key = ballots.count)

khan = ballots.count('Khan')
khanavg = khan/votes
khanpercent = "{:.3%}".format(khanavg)

correy = ballots.count('Correy')
correyavg = correy/votes
correypercent = "{:.3%}".format(correyavg)

Li = ballots.count('Li')
Liavg = Li/votes
Lipercent = "{:.3%}".format(Liavg)

Otool = ballots.count(r"O'Tooley")
Otoolavg = Otool/votes
Otoolpercent ="{:.3%}".format(Otoolavg)

winner = most_frequent(ballots)

print('Election Results')
print('-------------------------')
print(votes)
print('-------------------------')
print('Khan: ', khanpercent,' (', khan, ')')
print('Correy: ', correypercent,' (', correy, ')')
print('Li: ', Lipercent,' (', Li, ')')
print(r"O'Tooley: ",  Otoolpercent,' (', Otool, ')')
print('-------------------------')
print('Winner: ', winner)
print('-------------------------')

with open(write_csv, 'w', newline = '') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([votes])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Khan: ', khanpercent,' (', khan, ')'])
    csvwriter.writerow(['Correy: ', correypercent,' (', correy, ')'])
    csvwriter.writerow(['Li: ', Lipercent,' (', Li, ')'])
    csvwriter.writerow([r"O'Tooley: ",  Otoolpercent,' (', Otool, ')'])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow(['Winner: ', winner])
    csvwriter.writerow(['-------------------------'])