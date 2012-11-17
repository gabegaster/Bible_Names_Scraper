import httplib2
import re

def findName(text):
    a = re.match(r"(<.+>)?([A-Z][-'a-z]+)(</a>)?,", text)
    if a: return a.groups()[-2]

def main():
    h = httplib2.Http('.cache')
    url = 'http://en.wikipedia.org/wiki/' + 'List_of_biblical_names_starting_with_'
    letters = ("A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M" "N" "O""P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z")

    f = open('BiblicalNames.txt','w')
    f.write('Biblical Names\n')
    
    for letter in letters:
        print 'Querying letter '+letter,
        url_iter = url + letter
        page = h.request(url_iter, "GET")[1]
        print 'Analyzing letter '+letter

        ## from <ul> to </ul>, grab the second one
        text = re.split(r"</?ul>", page)[1]

        ## split it up into lines.
        lines = re.split(r"<li>", text)
        for line in lines:
            name = findName(line)
            if name:
                f.write(findName(line)+'\n')            
    f.close()

if __name__ == "__main__":
    main()
