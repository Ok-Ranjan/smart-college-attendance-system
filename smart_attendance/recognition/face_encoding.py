import face_recognition

def generate_face_encoding(image_path):

    # load image
    image = face_recognition.load_image_file(image_path)

    # Detect faces in the image
    face_locations = face_recognition.face_locations(image)

    # generate encoding
    encodings = face_recognition.face_encodings(image, face_locations)

    if len(encodings) > 0:
        return encodings[0]
    
    return None