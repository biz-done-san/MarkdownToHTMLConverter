import os
import sys
import markdown

class Markdown:
    CMDS = ["markdown"]

    # Markdown
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # convert(arguments)                    - string            : Main method. Call "Markdown.validate()" and convert markdown file to html file
    # validate(arguments)                   - string            : validate arguments. Call "Helper" Class static functions.
    # 

    @staticmethod
    def convert(arguments):
        if not Markdown.validate(arguments):
            return "Wrong something..."
        
        inputFile = arguments[2]
        outputFile = arguments[3]

        print("Read file...")
        with open(inputFile) as f:
            contents = f.read()
        print("Finshed reading file!!")
    
        contents = markdown.markdown(contents, extensions=['tables'])

        print("Convert file...")
        with open(outputFile, 'w') as f:
            f.write(contents)
        print("Finshed Converting file!!")

        return "Done!!!"
    
    @staticmethod
    def validate(arguments):
        if not Helper.isValidLength(arguments, 4):
            return False
        
        if arguments[1] not in Markdown.CMDS:
            return False

        if not Helper.isFileExist(arguments[2]):
            return False

        if not Helper.verifyOutputPath(arguments[3]):
            return False

        print("Succeeded in validation!!")
        return True

class Helper:
    # Helper
    # 
    # [Function Name(Parameters)]           - [Return Value]    : [Overview]
    # ========================================================================================================================
    # isFileExist(filepath)                  - boolean           : Check file exist
    # inputUserYorN(question)               - int               : Input and check the user prompt only Yes or No
    # verifyOutputPath(outputPath)          - boolean           : Veryfy overwriting output file if output path is exist
    # isValidLength(arguments, arrLen)      - boolean           : Verify arguments length
    # 

    @staticmethod
    def isFileExist(filepath):
        return os.path.isfile(filepath)

    @staticmethod
    def inputUserYorN(question):
        inputUserPrompt = input(question)
        if inputUserPrompt == 'y' or inputUserPrompt == 'Y':
            return 1
        elif inputUserPrompt == 'n' or inputUserPrompt == 'N':
            return 0
        else:
            return -1
    
    @staticmethod
    def verifyOutputPath(outputPath):
        allowOverwriting = 1
        
        if Helper.isFileExist(outputPath):
            allowOverwriting = Helper.inputUserYorN("The destination file already exists. Do you want to overwrite it?（y/N）: ")
        
        while allowOverwriting == -1:
            allowOverwriting = Helper.inputUserYorN("A different input was made. Do you want to overwrite the destination file?（y/N）: ")
        
        return bool(allowOverwriting)
    
    @staticmethod
    def isValidLength(arguments, arrLen):
        return len(arguments) == arrLen

if __name__ == "__main__":
    print(Markdown.convert(sys.argv))