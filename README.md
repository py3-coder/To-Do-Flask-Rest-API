
# To-Do-Flask-Rest-API

## A Backend application for implementing the TODO list application.

For Example: 

    Task   ~    Status

    1. Go for a run - Complete

    2. Work on templates -Incomplete

    3. Water plants - Incomplete

In the above example, each item is considered as a task, where in a person can check off each item in the list after they complete that task.

### Functional requirements:

● Create apis to create, delete and update a task

● Create an Api to mark the task as complete / Incomplete




## Run Locally

#### `Check-Point` :
  a. Make Sure You have Python 3.8 installed in your local machine

  b. Make Sure to Postman API Testing Tool installed ~ For Testsing Purpose


Step 1: Clone the project

```bash
  git clone https://github.com/py3-coder/To-Do-Flask-Rest-API
```

Step 2: Go to the project directory

```bash
  cd To-Do-Flask-Rest-API
```

Step 3: Install dependencies by 

```bash
  pip install -r requirements.txt
```

or

```bash
  pip install Flask
  python3 -m pip install --upgrade 'sqlalchemy<2.0'
```
Step 4: After installation Run this which prohibts cache file

```bash
  $env:PYTHONDONTWRITEBYTECODE=1  
```

Step 5: Start the server

```bash
  python main.py
```

Step 6: Test the Functions :
 
         a. Create 
         b. Update
         c. Delete
         d. Update_task_Complete
         e. Update_task_InComplete 



## Screenshots 

###### Image 01 : Get ALL Task
![image](https://user-images.githubusercontent.com/54509629/219830119-57581430-4280-4711-86e7-c57d05149098.png)

###### Image 02 : Create Task 
![image](https://user-images.githubusercontent.com/54509629/219830194-ce5db72e-33cb-4104-b480-a7014f6061bb.png)

###### Image 03 : Update Task Status 
![image](https://user-images.githubusercontent.com/54509629/219830315-aa25705f-4af3-400b-bdbb-0facdc17a4a4.png)

###### Image 04 : Delete Task 
![image](https://user-images.githubusercontent.com/54509629/219830361-416bf696-266f-4e29-854d-82e2fce094fd.png)

###### Image 05 : Update_Task_Complete
![image](https://user-images.githubusercontent.com/54509629/219830404-2623ad68-786b-4705-a37a-543cc9bd456d.png)

###### Image 06 : Update_Task_Incomplete
![image](https://user-images.githubusercontent.com/54509629/219830481-2500e49d-c9c4-4321-8f50-36bcbcdbc548.png)

###### Image 06 : Create Multiple Task
![image](https://user-images.githubusercontent.com/54509629/219830528-fb169f16-3b05-4026-83fc-9dd63db0202e.png)


###### Image 07 : Final Data by using getall
![image](https://user-images.githubusercontent.com/54509629/219830578-bf7731b3-1417-4d51-a3f3-ae88a7a011d2.png)


###### Image 07 : Terminal Image Request Records 
![image](https://user-images.githubusercontent.com/54509629/219830900-82346746-e789-44a5-a8bb-007946ba0758.png)



# Run API Using Docker Image

#### `Check-Point` :
  a. Make Sure You have docker installed in your local machine

Docker Hub Repo Link : https://hub.docker.com/r/saurabhgupta2929/flaskapp

Step 1: Pull the Docker Image 

```bash
  docker pull saurabhgupta2929/flaskapp
```

Step 2: Specify the Port according to your port avalability or leave as it is

```bash
  docker run -p 5000:5000 saurabhgupta2929/flaskapp
```

Step 3: Test the API on Exported Port as you get the http link.

Step 4: Test the Functions :
 
         a. Create 
         b. Update
         c. Delete
         d. Update_task_Complete
         e. Update_task_InComplete 
         
 ## Screenshots : 
 
 ### 🚀🚀 (Just If you want to know how to push the docker image to docker hub)
 
 ###### Image 01 : Pushing Docker Image form Local to docker hub 
 
 ![image](https://user-images.githubusercontent.com/54509629/219855418-5497ae2b-44f9-4719-8356-2de1c21115bf.png)
 
 ![image](https://user-images.githubusercontent.com/54509629/219855436-2ab014ad-db8d-4457-b635-2a9209fbc1c7.png)
 
  ###### Image 02 : Pulling the repo from Docker hub for running (see setps how to run )
  
  ![image](https://user-images.githubusercontent.com/54509629/219855561-f8c10b0c-b002-4c82-8ee8-b9bc49531ea3.png)
  
  ###### Image 03 :Testing the Exposed Port  :

 ![image](https://user-images.githubusercontent.com/54509629/219855631-1e265761-a7d1-42d0-b6e9-9844e0b06ed2.png)


## Tech Stack

**Client:** Python

**Server:** Flask 

**Container:** Docker 

## Authors

#### Saurabh Kumar
- [Resume](https://drive.google.com/file/d/1IVS-E_wNaUecqiVlsEOZWiotnNtUEkCz/view?usp=share_link)
- [py3-coder](https://www.github.com/py3-coder)
  
 






