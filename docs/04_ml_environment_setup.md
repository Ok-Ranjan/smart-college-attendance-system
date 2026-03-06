# Machine Leanring Environment Setup

This project uses a face recognition system to detect students in classroom images.

Libraries used:

- OpenCV
- face_recognition
- dlib
- numpy

## Why dlib is needed

dlib provides a face embedding model that converts a face into a numerical vector.

Example:

    [0.23, -0.11, 0.54, ...]

These vectors allow the system to compare faces mathematically.

## Why face_recognition library

The face_recognition library provides an easy API built on top of dlib.

It allows us to:

- detect faces
- generate face encodings
- compare faces

Example functions:

    face_recognition.face_locations()
    face_recognition.face_encodings()
    face_recognition.compare_faces()