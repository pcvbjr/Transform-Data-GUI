# Transform-Data-GUI
 A simple GUI using Flask. Allows upload of CSV and returns download file with transformed data. 

# Instructions
Run the app with the command "python app.py" in terminal. The terminal will return a URL on which the app is running. Copy and paste the address into your browser to view the GUI.

Within app.py, the transform() function accepts the file path for a user-uploaded file and creates a pandas DataFrame from this. You can edit transform() to do any data manipulation you like. Return a DataFrame you would like the user to then download as a CSV file.

Some ideas for data transformations:
- Load a saved model and predict on the uploaded data
- Create pivots or summary tables from the uploaded data
- Perform statistical analyses and return results

Edit the HTML files in the /templates folder as needed to give directions and information to the user.

# Sources
Code adapted from <a href="https://medevel.com/flask-tutorial-upload-csv-file-and-insert-rows-into-the-database/">medevel.com</a> and <a href="https://buildcoding.com/upload-and-download-file-using-flask-in-python/">buildcoding.com.
