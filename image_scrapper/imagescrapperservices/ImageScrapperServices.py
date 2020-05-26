import os


class ImageScrapperServices:
    def delete_existing_image(self, list_of_images):
        for self.image in list_of_images:
            try:
                os.remove("./static/"+self.image)
            except Exception as e:
                print('error in deleting:  ',e)
        return 0

    def list_only_jpg_files(self,folder_name:str):
        self.list_of_jpg_files=[]
        self.list_of_files=os.listdir(folder_name)
        print('list of files==')
        print(self.list_of_files)
        for self.file in self.list_of_files:
            self.name_array= self.file.split('.')
            if(self.name_array[1]=='jpg'):
                self.list_of_jpg_files.append(self.file)
            else:
                print('filename does not end withn jpg')
        return self.list_of_jpg_files