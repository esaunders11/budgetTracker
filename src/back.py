from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="esaunders",
    password="bignuts",
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

