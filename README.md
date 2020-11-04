# Inventory Manager


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
   docker run -d --name=webapp --net=host webapp
   ```



Before you commit
-----------------

 * 	Make sure you put unnecessary files in the .gitignore file



Local Testing (Without Containers)
-------------

 *  Setting up the python virtual enviornment (Within /inventory-manager directory):
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

