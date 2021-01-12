import Vue from 'vue'
import Router from 'vue-router'
import First from "../components/First";
import Second from "../components/Second";
import AddBook from "../components/AddBook";
import ChangeBook from "../components/ChangeBook";
import Login from "../components/Login";


Vue.use(Router)

export default new Router({
  routes: [
    {path: "/first", component: First},
    {path: "/second/:id", component: Second},
    {path:"/add_book",component:AddBook},
    {path:"/change/:id",component:ChangeBook},
    {path:"/login",component:Login},
  ]
})
