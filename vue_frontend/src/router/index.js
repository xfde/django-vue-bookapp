import {createWebHistory, createRouter} from 'vue-router';
import LoginPage from '../components/LoginPage'
import RegisterPage from '../components/RegisterPage'
import HomePage from '../components/HomePage'
import BooksPage from '../components/BooksPage'
import AllBooksPage from '../components/AllBooksPage'
import AddBookPage from '../components/AddBookPage'
const history = createWebHistory();
const router = createRouter({
    history,
    routes:[
        {
            path: '/login',
            component: LoginPage,
        },
        {
            path: '/register',
            component: RegisterPage,
        },
        {
            path: '/',
            component: HomePage,
        },
        {
            path:'/mybooks',
            component: BooksPage,
        },
        {
            path:'/books',
            component: AllBooksPage,
        },
        {
            path:'/addbook',
            component: AddBookPage,
        }
    ]
})
export default router