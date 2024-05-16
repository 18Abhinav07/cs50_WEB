# import face_recognition
# import os


# def get_name(known_image, db_path):
#     known_image = face_recognition.load_image_file(known_image)
#     known_encoding = face_recognition.face_encodings(known_image)[0]
#     for file in os.walk(db_path):
#         for f in file[2]:
#             print(f)
#             if f.endswith(".jpg"):
#                 unknown_image = face_recognition.load_image_file(
#                     os.path.join(db_path + f)
#                 )
#                 unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#                 results = face_recognition.compare_faces(
#                     [known_encoding], unknown_encoding
#                 )
#                 if results[0]:
#                     return db_path
#     return None


# def res(file):
#     file_path = "./WEBSITE/train/"
#     for dirs in os.walk(file_path):
#         for d in dirs[1]:
#             db_path = "./WEBSITE/train/" + d + "/"
#             res = get_name(file, db_path)
#     return res
