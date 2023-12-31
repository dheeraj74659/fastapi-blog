# FastAPI Blog App
A simple blog application API built using FastAPI.

The API supports following:
- Retrieve all blogs
- Details of the blog
- Create a blog
- Update the blog
- Delete the blog
- Create a user
- Authentication and Authorizaton using JWT


## Get started:
- Fork the ropo.
- Clone the repo.
- Create virtual envornment.

    ```
    python -m venv ./venv
    ```
- Activate the virtual environment.
    ```
    # for Windows.
    .\venv\scripts\activate

    # for linux.
    .\venv\bin\activate
    ```

- Install required libraries.

    ```
    pip install -r requirements.txt
    ```

- Populate the create a `.env` file in `backend` direcotry, reffering to `.env.template` file.

- Run the `uvicorn` command to start the server.
    ```
    uvicorn main:app
    ```
- Click on the link in the command line to visit the homepage. add `/docs` at the end of the URL to access the doc where one can test all endpoints.

�