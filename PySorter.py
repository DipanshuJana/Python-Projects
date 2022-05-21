import os
import time

def main(path):
    num = 0
    print ('Changing the path...')
    time.sleep(1)
    try:
        os.chdir(path)
        files = os.listdir()
    except Exception as e:
        print ('Error! invalid path entered')
    
    for file in files:
        num += 1
    
    imgExt = ['.png', '.jpeg', '.jpg', '.gif', '.tiff']
    docExt = ['.docx', '.doc', '.txt', '.pdf', '.xlsx', '.ppt']
    mediaExt = ['.mp4', '.mkv', '.mpeg', '.flv', '.mp3', '.avi', '.wav', '.ogg']
    archiveExt = ['.zip', '.rar', '.7z']
    appExt = ['.exe', '.rpm', '.iso', '.bat', '.cmd', '.msi']


    images = [file for file in files if os.splitext(file)[1].lower() in imgExt]
    docs = [file for file in files if os.splitext(file)[1].lower() in docExt]
    medias = [file for file in files if os.splitext(file)[1].lower() in mediaExt]
    archives = [file for file in files if os.splitext(file)[1].lower() in archiveExt] 
    applications = [file for file in files if os.splitext(file)[1].lower() in appExt] 
    others = []

    for file in files:
        ext = os.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and (ext not in archiveExt) and (ext not in appExt) and (os.path.isfile(file)) and (ext != '.py'):
            others.append(file)
        
    def createFolder():
        i = 0

        print ('Creating folder...')
        time.sleep(2)
        for item in files:
            print (f"{i}: {item}") 
            i = i + 1
        try:
            if not os.path.exists('Images'):
                os.mkdir('Images')

            if not os.path.exists('Documents'):
                os.mkdir('Documents')

            if not os.path.exists('Media'):    
                os.mkdir('Media')

            if not os.path.exists('Archives'):    
                os.mkdir('Archives')

            if not os.path.exists('Applications'):    
                os.mkdir('Applications')
                
            if not os.path.exists('Others'):    
                os.mkdir('Others')

        except Exception as e:
            print ('Error! Could not create folder')


    def move(folerName):
        print ('Sorting the files...')
        time.sleep(3) 
        try:
            for image in images:
                os.replace(image, f"{folerName}/{image}")

            for doc in docs:
                os.replace(doc, f"{folerName}/{doc}")

            for media in medias:
                os.replace(media, f"{folerName}/{media}")

            for archive in archives:
                os.replace(archive, f"{folerName}/{archive}")
            
            for application in applications:
                os.replace(application, f"{folerName}/{application}")

            for other in others:
                os.replace(other, f"{folerName}/{other}")

        except Exception as e:
            print ('Error! Could not move files into directory')

    print (f'Successfully sorted {num} files in your specified directory')

if __name__ == '__main__':
    path = str(input ('Enter the directory you want to sort files:\n'))
    main(path)
    main.createFolder()
    main.move("Images")
    main.move("Documents")
    main.move("Medias")
    main.move("Archives")
    main.move("Applications")
    main.move("Others")