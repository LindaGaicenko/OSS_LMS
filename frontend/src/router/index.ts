import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    children: [
      {
        path: "",
        redirect: "/items",
      },
      {
        path: "login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
      },
      {
        path: "register",
        name: "Register",
        component: () => import("@/views/Register.vue"),
      },
      {
        path: "account",
        name: "Account",
        component: () => import("@/views/Account.vue"),
      },
      {
        path: "items",
        name: "Items",
        component: () => import("@/views/AllItems.vue"),
      },
      {
        path: "/checkout",
        name: "Checkout",
        component: () => import("@/views/Checkout.vue"),
        props: true,
      },
      {
        path: "/success",
        name: "Success",
        component: () => import("@/views/Success.vue"),
        props: true,
      },
      {
        path: "/:categorySlug/:itemSlug",
        name: "Item",
        component: () => import("@/views/Item.vue"),
        props: true,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
