from warnings import simplefilter 
simplefilter(action='ignore', category=DeprecationWarning)
import os
from flask import Flask, render_template, redirect, url_for, request, jsonify, session
import boto3
from botocore.exceptions import ClientError
import requests
import os
import botocore
from cognito import cognitoRoute
from flask_cors import CORS
from jobs import jobsRoute
from applicants import applicantsRoute



app = Flask(__name__)
CORS(app)


APP_CLIENT_ID = "1rfl5n6j4su0mgmgkfh43fqbov"
app.secret_key = 'super secret key'
app.register_blueprint(cognitoRoute)
app.register_blueprint(jobsRoute)
app.register_blueprint(applicantsRoute)


if __name__ == '__main__':
   
    app.run(host='0.0.0.0',debug=True) 