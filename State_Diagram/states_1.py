#State Population Diagrom <Eric Williams>
#Creating a State Dictionary.
def make():
  s=['Alabama','Alaska','Arizona','Arkansas','California','Colorado',
   'Connecticut','Delaware','District of Columbia','Florida','Georgia',
   'Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
   'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
   'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
   'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma',
   'Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota',
   'Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia',
   'Wisconsin','Wyoming']
  import urllib
  DATA = urllib.urlopen("https://www.census.gov/popest/data/state/totals/2014/tables/NST-EST2014-01.csv")
  while True:
    LINE = DATA.readline()
    if LINE == '':
      break
    L = LINE
    x=51
    H = {}
    if 'West' in L:
      h = 0
      P = []
#To make the List
      while x>0:
        LINE = DATA.readline()
        NEWLINE = LINE.replace(',','')
        NEWLINE = NEWLINE.replace('","',',')
        NEWLINE = NEWLINE.replace(s[h],'')
        NEWLINE = NEWLINE.replace('""',',')
        NEWLINE = NEWLINE.replace('.','')
        NEWLINE = NEWLINE.replace('\'','')
        NEWLINE = NEWLINE.replace('"','')
        NEWLINE = NEWLINE.replace('\r\n','')
        M = NEWLINE.split(',')
        P.append(M)
        h = h + 1
        x = x -1
#To make the Dictionary
  D = {'Alabama':P[0],'Alaska':P[1],'Arizona':P[2],'Arkansas':P[3],'California':P[4],
       'Colorado':P[5],'Connecticut':P[6],'Delaware':P[7],'District of Columbia':P[8],
       'Florida':P[9],'Georgia':P[10],'Hawaii':P[11],'Idaho':P[12],'Illinois':P[13],
       'Indiana':P[14],'Iowa':P[15],'Kansas':P[16],'Kentucky':P[17],'Louisiana':P[18],
       'Maine':P[19],'Maryland':P[20],'Massachusetts':P[21],'Michigan':P[22],
       'Minnesota':P[23],'Mississippi':P[24],'Missouri':P[25],'Montana':P[26],
       'Nebraska':P[27],'Nevada':P[28],'New Hampshire':P[29],'New Jersey':P[30],
       'New Mexico':P[31],'New York':P[32],'North Carolina':P[33],'North Dakota':P[34],
       'Ohio':P[35],'Oklahoma':P[36],'Oregon':P[37],'Pennsylvania':P[38],
       'Rhode Island':P[39],'South Carolina':P[40],'South Dakota':P[41],
       'Tennessee':P[42],'Texas':P[43],'Utah':P[44],'Vermont':P[45],'Virginia':P[46],
       'Washington':P[47],'West Virginia':P[48],'Wisconsin':P[49],'Wyoming':P[50]}
  return D
  DATA.close()
 

