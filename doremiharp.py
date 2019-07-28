# Libraries
import music21

# Constants
message = "drmfsltwe"

# Mappings
mappingsDictionary = {  #letter : pitch
                        "d" : "C4",
                        "r" : "D4",
                        "m" : "E4",
                        "f" : "F4",
                        "s" : "G4",
                        "l" : "A4",
                        "t" : "B4",
                        "w" : "C5",
                        "e" : "C4"
}

# Music constants
harp = music21.instrument.Harp() # instrument
noteLength = 1                  # note length

# ---- Process Text
characterList = list(message) # Break text into characters

#---- MUSICAL TRANSLATION
#-- Set up musical piece
s = music21.stream.Stream() # create stream for entire piece
p = music21.stream.Part()   # add instrument part to music
p.insert(0, harp)           # choose instrument playing
print( p.show('text') )

# Loop through charachter in the List of charachter List
for charachter in characterList:
    print(charachter)
    
    #is the charachter in the mappingsDictionary? 
    if charachter in list( mappingsDictionary.keys() ):
        pitch = mappingsDictionary[ charachter ]
        print(pitch)


        nextNote =music21.note.Note(  pitchName = pitch, quarterLength = noteLength )
        #print( nextNote )
        print(  charachter, pitch, nextNote)

    else:
        # No pitch, defines rest
        nextNote = music21.note.Rest ( quarterLength = noteLength )
        print(  charachter, nextNote)
    
    p.append( nextNote ) # adding next note to harp part

p.show('text')

s.append(p) # add part to Stream
print("\n Stream \n")
s.show('text')
s.write( 'midi', fp= "doremiharp.mid")
