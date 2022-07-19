
print("\nHi, This program takes a txt file and a css file\n then checks the paragraphs(multi lines) and if\n paragraph starts with number, it will generate\n a 'h1' tag with paragraph content other paragraphs\n will result in a 'p' tag in the index.html file\n in current directory\n")
textFilePath = input("Enter txt file path(default is lorem.txt - leave it blank to use default): ")
if not textFilePath:
    textFilePath = 'lorem.txt'

cssFilePath = input("Enter css file path(default is index.css - leave it blank to use default): ")
if not cssFilePath:
    cssFilePath = 'index.css'
try:
    open(cssFilePath, 'r')
    if (cssFilePath.split(".")[1] != "css"):
         print("please enter valid css file next time, bye!");
         exit()
except OSError:
    print ("Path of the css file is Invalid")
    exit()
paragraphs = []                      
linenum = 0
substr = "\n" 
try:
    with open (textFilePath, 'rt') as myfile:
        for line in myfile:
            if line != "\n":
                linenum += 1
                if line.lower().find(substr) != -1:    # if case-insensitive match,
                    paragraphs.append(line.rstrip('\n'))
        paragraphs.append(line.rstrip('\n'))


    fp = open('index.html', 'w')
    fp.write("""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ostad Lotfi</title>
        <link rel="stylesheet" href="%s">
    </head>
    <body>
    """ %(cssFilePath))

    for p in paragraphs:
        # print(p)
        if  p[:1].isdigit() : 
            fp.write('<h1>'+p[1:]+'</h1>\n')
        else:
            fp.write('<p>'+p+'</p>\n')
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()
    print('Successfully generated file index.html')
    print('Written by : Hamidreza Shams(mail@reshinweb.ir)')
except OSError:
     print ("Path of the file is Invalid")