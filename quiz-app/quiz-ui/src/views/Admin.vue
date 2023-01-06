<template>

    <!-- Disconnect -->
    <div v-show="logged" id="disconnect">
        <button @click="disconnect">Se déconnecter</button>
    </div>
    

    <Login @logged="loggedHandler" v-show="!logged"/>

  
  
</template>

<script>
import Login from "@/components/Login.vue";
import AdminStorageService from "@/services/AdminStorageService";


export default {
    name: 'Admin',

    data() {
        return {
            logged: false
        }
    },

    components: {
        Login
    },

    methods: {
        loggedHandler(logged) {
            this.logged = logged;
        },

        disconnect() {
            this.logged = false;
            AdminStorageService.removeToken();
        }
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