# clpdataengineer
For CLP data engineering case study


Inside the clp folder there are 3 main files

builddocker.sh            
Command line script to execute docker template

createTableclp.sql        
Create table schema

dockerfile                
Docker Template that creates the container


Within, there is another folder named script_file with 2 main scripts

flaskwebsite.py           
Website allow for csv import using python flask

sparkscriptprocess.py     
Pyspark script that completes task C

./templates/upload.html   
html template that flask retrieves to generate baseline website
