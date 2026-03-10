# Face Encoding System

Face recognition systems do not compare images directly.

Instead, each face is converted into a numerical representation called a face encoding.

The encoding is a 128-dimensional vector representing facial features.

Example:

    [0.13, -0.52, 0.41, ...]

When two faces are compared, the system calculates the distance between their encodings.

If the distance is small, the faces belong to the same person.

This project uses the face_recognition library to generate these encodings.