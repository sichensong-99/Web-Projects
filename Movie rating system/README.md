# Movie Rating System
<img width="960" alt="image" src="https://github.com/sichensong-99/Web-Projects/assets/64934563/4a79ccd4-e586-4b63-a410-e79ea5fb6f05">

## Project Description  

The goal of this project is to develop a web-based application utilizing MongoDB as the backend. The frontend will retrieve data from the MongoDB database, and the webpage will offer a graphical user interface (GUI) for performing CRUD operations on items.Through the frontend website, users can rate movies and add comments to each movie, with the backend database automatically updating in real-time to reflect the latest ratings and user comments.  

The MongoDB database consists of three collections: the "movie_list" collection, storing detailed movie information; the "movies" collection, storing user-posted movie comments; and the "users" collection, storing user information. 
## Feature
### Sign-in/Sign-up  
- Logged in successfully
  
Users will be directed to their dashboard
- Unsuccessful login
  
If users incorrectly enter their password on the sign-in page, they have the option to navigate to another page to reset the password or proceed to the sign-up page to create a new account. As a result, new account information or updated password resets will be automatically saved in the backend MongoDB.

<img width="956" alt="image" src="https://github.com/sichensong-99/Web-Projects/assets/64934563/1bc0e10b-7a3d-476e-a3df-e9909f8d5c45">


### Movie Info
- Logged-out State

Users can only view movie details and will be automatically redirected to the sign-in/sign-up page when they click the "add comments" button.
- Logged-in State

Users can view movie details and post comments freely  

<img width="948" alt="image" src="https://github.com/sichensong-99/Web-Projects/assets/64934563/34c0aab4-6ec0-45d1-885e-6b64bf154cd6">

### Movie Comments
- Logged-out State
  
Users can search for comments by movie name, user name, post date, or movie rating level. Clicking the "modify comments" button will automatically direct them to the sign-in/sign-up page  

<img width="960" alt="image" src="https://github.com/sichensong-99/Web-Projects/assets/64934563/d29a81d9-dd90-4c41-a4a6-9915e1cc0db8">

- Logged-in State
  
Users can search for comments by movie name, user name, post date, or movie rating level. They can also remove or update their comments. Accordingly, modified comments will be automatically updated in the backend MongoDB.  

<img width="946" alt="image" src="https://github.com/sichensong-99/Web-Projects/assets/64934563/5345c4a5-2e92-4202-9405-3547a48fd515">
