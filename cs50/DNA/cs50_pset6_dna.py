import csv
from sys import argv

# Only when users enter 2 command-line argument, the program will be continued
while True:
    try:
        data_csv = argv[1]
        seq_txt = argv[2]
        break
    except:
        print("Error")
        exit(0)


def Compare(ppl_dict: list, freq_dict: dict) -> str:
    '''
    Compare STR counts of every individuals with the list of consecutive repeats of STR.
    Input: a list of dictionaries of people, in which contain the STR counts;
    a dictionary recording the number of highest consec repeats of every STR in DNA
    Output: a string, either the name of the person who matches; or 'No match' when
    none is found.

    '''
    for person in ppl_dict:
        match = False
        for k, v in freq_dict.items():
            if int(person[k]) != v:
                match = False
                break
            match = True
        if match == True:
            return person["name"]
    else:
        return "No match"

def Count(seq: str, pattern: list) -> dict:
    freq_dict = {}
    for p in pattern:
        tmp = []
        for i in range(len(seq) - len(p)):
            j = i  # make a copy of i, so that loops work without affecting the value of i
            freq = 0
            # if the substring of the DNA matches with the STR pattern
            while seq[j: j + len(p)] == p:
                freq += 1
                j += len(p)  # shift to the right by the length of STR pattern
            # store the number of repeats for every single position into a list
            tmp.append(freq)
        freq_dict[p] = freq_dict.get(p, max(tmp))

    return freq_dict

# read in csv file
with open(data_csv) as csvfile:
    dnareader = csv.DictReader(csvfile)
    pattern, ppl_dict = [], []
    for row in dnareader:
        ppl_dict.append(row)

    # store the names of STR
    for key in dnareader.fieldnames[1:]:
        pattern.append(key)

# read in text file
with open(seq_txt) as txtfile:
    seq = txtfile.read()
    freq_dict = Count(seq, pattern)

print(Compare(ppl_dict, freq_dict))
