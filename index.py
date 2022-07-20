
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
    fp.write("""<!Doctype html>
    <html lang="fa">
    <head>
    <title>Ostad Lotfi</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS v5.2.0-beta1 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css"  integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
    <link rel="stylesheet" href="%s">
    </head>
    <body>
     <div class="row">
    """ %(cssFilePath))

    for p in paragraphs:
        # print(p)
       
      
        if  p[:1].isdigit() : 
            fp.write('<h1>'+p[1:]+'</h1>\n')
        else:
            fp.write('<div class="col-lg">')
            fp.write('<p>'+p+'</p>\n')
            fp.write('</div>')

    
    fp.write(' </div>\n')
    fp.write('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>\n')
    fp.write('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N0Yf4ZOJErLsIcvOU2qSb74wXpOhqTvwVx3OElZRweTnQ6d31fXEoRD1Jy" crossorigin="anonymous"></script>\n')
    fp.write('</body>\n')
    fp.write('</html>\n')
    fp.close()
    print('Successfully generated file index.html')
    print('Written by : Hamidreza Shams(mail@reshinweb.ir)')
except OSError:
     print ("Path of the file is Invalid")