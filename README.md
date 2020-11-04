# Inventory Manager

Description
-----------
 
Our goal was to create an application to keep track of inventory for a retail store. We used Flask and Python to implement a RESTful API that interacts with a SQLite Database. We have two Flask applications: one for the backend/API and one for our frontend/UI. 

Docker 
------

 * Build and run Docker images
   ```bash
    make docker
   ```
   
Usage
------------
* By default, the webapp is hosted at http://127.0.0.1:5001/
* The webbapp will display all the contents of the database
* There is a searchbar at the top that allows you to search the database by ID or Name
* After you search, only matching items will be displayed. You can go back to viewing all of the items by clicking the 'All' button
* Each item has a red 'X' button next to it which will delete the item from the database.
* More items can be added to the database at the bottom of the inventory table.

* Our API accepts HTTP form data. Sending a POST request to http://127.0.0.1:5000/api/inventory/echo with form data will return with your sent data and print to stdout. To test this, you must send form-data in a POST Request. Example:

| key | value |
|---|---|
| name | chips |
| stock | 100 |
| price | 2.99 |
  

Local Testing (Without Containers)
-------------

 *  Build the API locally:
    ```bash
    make build
    ```

 *  Run the API locally:
    ```bash
    make run
  
