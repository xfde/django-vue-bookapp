# BookStore application
 - App made with django as backend and vue-js as frontend
[![DEMO VIDEO](https://img.youtube.com/vi/avik12MpSB4/0.jpg)](https://www.youtube.com/watch?v=avik12MpSB4)

# Usage
Users can create an account/ login using their credentials and see a full list of books. They can add books to their favorites list or remove them.
They can also create new entries of books that will show up in the list of books.

#Tehchnology
django handles the api endpoints creating/storing/editing lists and books while also create and authenticating users.

*Book Model:*
- author
- title
- description
- poster image

The relation between users and books is a `ManytoManyField` handled by an auxiliary model `Profile`.

##### FrontEnd:
- **Vue.js 3** project made with vue cli
- Form validation for login
- Uses **Vuex** for storing lists and user status and **Vue router** to navigate the SPA
- Uses **Element UI** (Element Plus for vue 3) as front-end design framework
-  Use **Axios** in order to communicate with api

##### Backend:
- Uses **django-webpack-loader** to serve vuejs
- Uses **django-rest-framework** to create the apis
- Uses Django's default **users model** for authentication
- handles **cors** for a more secure login/register  


