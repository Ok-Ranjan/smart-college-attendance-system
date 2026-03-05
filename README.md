# Smart College Attendance System

A Django + Machine Learning based system that automates classroom attendance using face recognition.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![ML](https://img.shields.io/badge/MachineLearning-FaceRecognition-orange)

---

## Problem
Manual attendence wastes time and is prone to proxy attendance.

## Solution
A system where teacher upload a classroom photo and the system automatically amrks attendence using face recognition.

---

## Features

- Face recognition based attendance
- Teacher dashbord
- HOD monitoring system
- Assignment tracking
- Student internal marks claculation
- Character scoring system
- Student activity particiation tracking

---

## Tech Stack

Backend:
- Django

MAchine Learning:
- OpenCV
- face_recognition
- dlib

Databese:
- SQLite (develoment)

---

## System Architecture

Teacher Upload Image
        |
Face Detection (OpenCV)
        |
Compare with Student Database
        |
Mark Attendance

---

## Project Structure

smart-attendance
│
├── accounts
├── attendance
├── recogintion
├── academics
│
├── media
├── manage.py
└── requirements.txt

---

## Feature Improvements

- YOLO based classroom detection
- Mobile application for teachers
- Cloud deployment