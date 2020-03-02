import glob, re, os

path = "D:\\ImageRec\\butterflies_and_beetles\\train\\pickups\\"
for filename in glob.glob(path + 'pickup *.jpg' ):
    print(filename)
    #newfilename_removeleftbracket = re.sub(r'\(', '.', filename)
    #newfilename_removerightbracket = re.sub(r'\)', '', newfilename_removeleftbracket)
    newfilename_removedwhitespace = re.sub(" ", ".", filename)
    #print(newfilename_removerightbracket)
    os.rename(filename, newfilename_removedwhitespace)
