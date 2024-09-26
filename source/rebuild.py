
RGBToUse = "HEX"

def formatRGB(rgb):
    return ("RGB(" + str(rgb[0]) + ", " + str(rgb[1]) + ", " + str(rgb[2]) + ")")

for variant in ["Light", "Dark"]:
    themeName = "Solarized-" + variant
    print("Rebuilding '" + themeName + "'...")
    
    inputFile = themeName + ".txt"
    print("  Loading '" + inputFile + "'...")
    if (fin := open(inputFile, "r")):
        line = fin.readline()
        
        # Parse first line...
        if ((len(line) > 50) and (line[0:6] == "SOLARI")):
            RGBOffset = line.index(RGBToUse)
            
            # Parse color names and values...
            scheme = {}
            while (line := fin.readline()):
                if ((len(line) > RGBOffset) and(line[RGBOffset] == "#")):
                    colorName = line[0:RGBOffset - 1].strip()
                    RGBStr = line[RGBOffset + 1 : RGBOffset + 7].strip()
                    scheme[colorName] = (
                            int(RGBStr[0:2], 16),
                            int(RGBStr[2:4], 16),
                            int(RGBStr[4:6], 16)
                        )
            #print(scheme)
            
            # Generate new .prefs file based on Template...
            outputFile = "../" + themeName + ".prefs"
            print("  Generating '" + outputFile + "'...")
            templateFile = "Template.prefs"
            if (tempIn := open(templateFile, "r")):
                if (fout := open(outputFile, "w")):
                    while (line := tempIn.readline()):
                        line = line.replace("{themeName}", themeName)
                        for key in scheme:
                            line = line.replace("{" + key + "}", formatRGB(scheme[key]))
                        fout.write(line)
                    fout.close()
                tempIn.close()
        fin.close()
        print("  Done!")
    print("")

