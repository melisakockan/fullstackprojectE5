<template>

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>

    <Login @logged="loggedHandler" v-else/>

  
  
</template>

<script>
import Login from "@/components/Login.vue";
import Logout from "@/components/Logout.vue";
import AdminStorageService from "@/services/AdminStorageService";


export default {
    name: 'Admin',

    data() {
        return {
            logged: false
        }
    },

    components: {
        Login,
        Logout
    },

    methods: {
        loggedHandler(logged) {
            this.logged = logged;
        },

    }
};
</script>


<style>

#disconnect{
    width: 100%;
    display: flex;
    justify-content: flex-end;
    margin: 10px 0px;
    align-items: center;
}

</style>