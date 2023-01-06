<template>

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>
    <Login @logged="loggedHandler" v-else/>

    <!-- Admin -->
    <div v-if="logged">
        <div v-if="currentQuestion == null">
            <QuestionsList @question_number="QuestionNumberHandler"/>
        </div>
    
        <div v-else-if="currentQuestion != null">
            <QuestionViewer :question_number="currentQuestion" @question_number="QuestionNumberHandler" @edit="EditHandler"/>
        </div>
    </div>

    

  
  
</template>

<script>
import Login from "@/components/Login.vue";
import Logout from "@/components/Logout.vue";
import QuestionsList from "@/components/QuestionsList.vue";
import QuestionViewer from "@/components/QuestionViewer.vue";
import AdminStorageService from "@/services/AdminStorageService";


export default {
    name: 'Admin',

    data() {
        return {
            logged: null,
            currentQuestion: null,
            edit: null
        }
    },

    components: {
        Login,
        Logout,
        QuestionsList,
        QuestionViewer
    },

    methods: {
        loggedHandler(logged) {
            this.logged = logged;
        },

        QuestionNumberHandler(index) {
            this.currentQuestion = index;
        },

        EditHandler(edit) {
            this.currentQuestion = null;
            this.edit = edit;
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