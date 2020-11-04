# Inventory Manager

Description
-----------
 
Our goal was to create an application to keep track of inventory for a retail store. We used Flask and Python to implement a RESTful API that interacts with a SQLite Database. We have two Flask applications: one for the backend/API and one for our frontend/UI. 

Docker 
------

 * Build Docker images from Dockerfiles:
   ```bash
   docker build routing -t routing &&
   docker build webapp -t webapp
   ```

 * Run the API image as a container
   ```bash
   docker run -d --name=routing --net=host routing
   ```

 * Run the wepapp image as a container
   ```bash
   docker run -d --name=webapp --new=host webapp
   ```
   
Usage
------------
* By default, the webapp is hosted at http://127.0.0.1:5001/
* The webbapp will display all the contents of the database
* There is a searchbar at the top that allows you to search the database by ID or Name
* After you search, only matching items will be displayed. You can go back to viewing all of the items by clicking the 'All' button
* Each item has a red 'X' button next to it which will delete the item from the database.
* More items can be added to the database at the bottom of the inventory table.


   

Local Testing (Without Containers)
-------------

 *  Setting up the python virtual envioronment (Within /inventory-manager directory):
    ```bash
    python3 -m venv venv
    ```

 *  Running venv:
    ```bash
    source venv/bin/activate
    ```

 *  Installing dependencies (inside venv):
    ```bash
    pip -r install requirements.txt
    ```

 *  Running the API (Within /routing directory):
    ```bash
    python3 routing.py
    ```

 * Running the webapp (Within /inventory-manager directory)
   ```bash
   python3 webapp/webapp.py
   ```


 
