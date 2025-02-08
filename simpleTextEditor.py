import os

def read_file(filename):
        with open(filename,'r') as file:
            content = file.read()
            print(content)

def write_to_file(filename,contentToWrite):
      with open(filename,'w') as file:
            file.write('\n'.join(contentToWrite)) 
            
def getUserInput():
        print("Enter the Content to write to the file(SAVE to save the content): ")
        contentToWrite = []    
        while True:
            userInput = input()
            if userInput == 'SAVE':
                break
            contentToWrite.append(userInput)
        return contentToWrite

def main():
    filename = input("Enter the filename: ")
    try:
        if(os.path.exists(filename)):
            read_file(filename)
        else:
            write_to_file(filename,'') 
    except Exception as e:
        print(e)
    
    try:
        contentToWrite = getUserInput()
        write_to_file(filename,contentToWrite)
    except Exception as e:
        print(e)
    
if __name__ ==  '__main__':
    main()