# this program can save a security copy of your files 
# receives Two parameters
# folder :one path of dir and make copy of security
# fiter: a boolean for indicate if only save files
        # with extens is .py or .txt

import zipfile, os

def backupToZip(folder,fiter ):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)
    print(folder)
    number=1
    # Figure out the filename this code should use based on
    # what files already exist.
    while True:
        if fiter == "txt-py":
            zipFileName= os.path.basename(folder) + '_' + str(number)+"txt-py" +'.zip'
        if fiter=='nn-txt-py':
            zipFileName= os.path.basename(folder) + '_' + str(number)+"nn-txt-py" +'.zip'
        if fiter=="jpg-jpeg":
            zipFileName= os.path.basename(folder) + '_' + str(number)+"jpg-jpeg" +'.zip'
        if fiter=="none":
            zipFileName= os.path.basename(folder) + '_' + str(number)+'.zip'
        if not os.path.exists(zipFileName):
            break
        number+=1
    # TODO: Create the ZIP file.
    print("creating %s..." %(zipFileName))
    backupZip=zipfile.ZipFile(zipFileName,'w')
    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s..' %(foldername))
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            print(filename)
            newBase = os.path.basename(folder) + '_'
            print("newBase: ",newBase)
            if filename.startswith(newBase) and filename.endswith('.zip'):
                print("entro en el condicional de aca")
                continue # don't backup the backup ZIP files
            if (filename.endswith('.txt') or filename.endswith('.py')) and fiter == "txt-py":
                print("entro condicion 1")
                backupZip.write(os.path.join(foldername, filename))
            if (filename.endswith('.txt')==False and (filename.endswith('.py'))==False) and fiter=='nn-txt-py':
                print("entro condicion 2")
                backupZip.write(os.path.join(foldername, filename))
            if (filename.endswith('.jpg') or (filename.endswith('.jpeg'))) and fiter=="jpg-jpeg":
                backupZip.write(os.path.join(foldername, filename))
            if filter == "none":                
                backupZip.write(os.path.join(foldername, filename))
        backupZip.close()
    print("Done")
    
backupToZip("C:\\Users\\Juan\\Documents\\respaldo pc juanma\\Python\\DESARROLLO_FINES_DE_SEMANA\\automate_boring_thimgs_with_python\\10_08_2022\\carpeta.20-10-2020", "jpg-jpeg")