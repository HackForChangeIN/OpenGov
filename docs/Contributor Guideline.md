# Contributor Guidelines
  This document contains information for anyone wishing to contribute to the project. If you are looking to help with a code contribution to our project, here's a quick rundown!

  1. Find an issue that you are interested in addressing or a feature that you would like to add.  
  2. Fork the repository associated with the issue to your local GitHub organization. This means that you will have a copy of the repository under **your-GitHub-username/repository-name**.  
  3. Clone the repository to your local machine using git clone  
  ```
    https://github.com/HackForChangeIN/OpenGov.git
    cd OpenGov
  ```
  4. Create an python environment with  
  ```  
  python -m venv venv  
  or  
  virtualenv venv 
  ```    
  5. activate it with (windows: ```venv\Scripts\activate```, Mac/Linux: ```source venv/bin/activate```)  
  6. Install required packages:  ```pip install -r requirements.txt```     
  7. Apply migration by using the following commands  
  ```  
  python manage.py migrate  
  ```  
  9. create superuser for the project by using following commands  
  ```  
  python manage.py createsuperuser  
  ```  
  10. To run the server locally use the following commands  
  ```  
  python manage.py runserver  
  ```  
  11. To open the project in the browser go to     
  ``` 
  127.0.0.1:8000  
  ```  
  12. To populate the intial data use the followwing commands  
  ```  
  ```  
  13. Make the appropriate changes for the issue you are trying to address or the feature that you want to add.  
  14. Create a new branch for your fix using  
  ```   
  git checkout -b branch-name-here  
  ```    
  15. Use the following commands to add the file contents of the changed files to the "snapshot" git uses to manage the state of the project, also known as the index.   
  ```  
  git add insert-paths-of-changed-files-here  
  ```  
     
  16. Use the following command to store the contents of the index with a descriptive message.
  ```  
  git commit -m "Insert a short message of the changes made here"  
  ```     
  17. Push the changes to the remote repository using 
  ```  
  git push origin branch-name-here  
  ```    
  18. Submit a pull request to the **contrib** branchof the repository.  
  19.  Title the pull request with a short description of the changes made and the issue or bug number associated with your change. For example, you can title an issue like so "Added more log outputting to resolve #252".  
  20. In the description of the pull request, explain the changes that you made, any issues you think exist with the pull request you made, and any questions you have for the maintainer.  
  21. Wait for the pull request to be reviewed by a maintainer.  
  22. Make changes to the pull request if the reviewing maintainer recommends them.  
  23. Celebrate your success after your pull request is merged!  
  

