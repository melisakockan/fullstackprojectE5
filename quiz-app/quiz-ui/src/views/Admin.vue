<template>

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>
    <Login @logged="loggedHandler" v-else/>

    <!-- Admin -->

    <div v-if="logged">
        <QuestionsList @question_number="QuestionsListHandler"/>
    </div>

  
  
</template>

<script>
import Login from "@/components/Login.vue";
import Logout from "@/components/Logout.vue";
import QuestionsList from "@/components/QuestionsList.vue";
import AdminStorageService from "@/services/AdminStorageService";


export default {
    name: 'Admin',

    data() {
        return {
            logged: null
        }
    },

    components: {
        Login,
        Logout,
        QuestionsList
    },

    methods: {
        loggedHandler(logged) {
            this.logged = logged;
        },

        QuestionsListHandler(index) {
            alert(index);
        }

    },

    async created() {
        this.logged = await (AdminStorageService.checkToken());
       
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