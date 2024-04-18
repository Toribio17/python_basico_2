import os
import shutil
import pathlib
from os import walk
import zipfile


class file_managment():

    def __init__(self):
        print("My constructor")

    #zip a file 
    def zip_files(self):
        zip_file = zipfile.ZipFile('','w')
        zip_file.write('',compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()


    def read_file(self,path,file_name,mode):
        #f = open(file_name, mode) 
        #Read a pdf use rb
        f = open(path + "/" + file_name, mode)
        #print(f.read())
        print("Done")

        return f


    def delete_file(self,path,file_name):
        os.remove(path + "/" + file_name)

        print("Delete it")

        return "delete it"

    def exist_file(self, path,file_name):
        status = False

        if os.path.exists(path + "/" + file_name):
            status = True
        else:
            status = False

        print("file status: ",status)

        return status

    #test with a txt
    def write_file(self,path,file_name,mode,content):

        f = self.read_file(path,file_name,mode) #"r, w, a"
        f.write(content)
        f.close()

        print("Complete")

    def create_folder(self,path,directory_name):
        # Path definition
        path = os.path.join(path, directory_name)
        # Create the directory
        os.mkdir(path) 
        print("Directory '% s' created" % path) 
        
    def folder_access(self,path,directory_name):
        
        path = os.path.join(path, directory_name)
        os.chmod(path,0o777) # si quieren ejecutar en shell usar -> chmod 777
        
        print("Directory '% s' chmod" % path) 
        
        
    #borrar folder (si esta vacia); necesitas borrar antes los archivos
    def delete_os_folder(self,path,directory_name):
        # Path
        path = os.path.join(path, directory_name) 
        
        #remove the path
        os.rmdir(path) # si quieren ejecutar en shell usar -> mdir
        print("% s has been removed successfully" % directory_name)

    #borrar folder y sus files dentro
    def delete_shutil_folder(self,path,directory_name):
        #path
        path = os.path.join(path, directory_name)
        #print("path result: ", path)
        # removing directory
        shutil.rmtree(path)
        print("% s has been removed successfully" % directory_name)

   
    def list_folder_files(self,path,directory_name):

        list_result = []

        dir_path = os.path.join(path, directory_name)
        # iterar en los folders
        for file_name in os.listdir(dir_path):
            #verificar si el actual path es un file
            if os.path.isfile(os.path.join(dir_path, file_name)):
                # add filename to list
                list_result.append(file_name)
                
        
        print("List of files", list_result)
        return list_result

    def list_walk_folder_files(self,path,directory_name):

        dir_path = os.path.join(path, directory_name)
        # list to store files name
        list_result = list()
        for (dir_path, dir_names, file_names) in walk(dir_path):
            print(file_names)

        print("List of files", list_result)


    def list_pathlib_folder_files(self,path,directory_name):

        # salvar el file
        list_files_result = []
        list_directory_result = list()

        # definir el path a consultar 
        path_directory = pathlib.Path(path + "/" + directory_name)

        # iterate directory
        for entry in path_directory.iterdir():
            # check if it a file
            if entry.is_file():
                list_files_result.append(entry)
            else:
                list_directory_result.append(entry)

        print("List of files", list_files_result)
        print("List of directories", list_directory_result)

        return list_files_result, list_directory_result

    def file_rename(self):
        pass


if __name__ == "__main__":
    obj = file_managment()
    #Coloca tu path
    #path = ""
    #Coloca el file_name 
    file_name = "python_testing.txt"
    #Coloca tu path
    path = "/Users/luistoribio/Documents/curso_python_avanzado/sesion_1_python_avanzado"
    #Coloca el file_directory
    directory_name = "dir_testing"
    obj.read_file(path,file_name,"w")
    #obj.delete_file(path,file_name)
    #obj.exist_file(path,file_name)
    #obj.write_file(path,file_name,"w","third content in python avanzado")
    #obj.create_folder(path,directory_name)
    #obj.delete_os_folder(path,directory_name)
    #obj.delete_shutil_folder(path,directory_name)
    #obj.list_folder_files(path,directory_name)
    #obj.list_walk_folder_files(path,directory_name)
    #obj.list_pathlib_folder_files(path,directory_name)







    
    

    
            


    

    