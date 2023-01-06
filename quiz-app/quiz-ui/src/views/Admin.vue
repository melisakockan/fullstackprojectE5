<template>

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>
    <Login @logged="loggedHandler" v-else/>

    <!-- Admin -->
    <div v-if="logged">
        <div v-if="currentQuestion == null & edit == null">
            <QuestionsList @question_number="QuestionNumberHandler"/>
        </div>
    
        <div v-else-if="currentQuestion != null & edit == null">
            <QuestionAdminView :question_number="currentQuestion" @question_number="QuestionNumberHandler" @edit="EditHandler"/>
        </div>

        <div v-else-if="edit != null">
            <QuestionEdit :question_number="edit" @edit="EditHandler"/>
        </div>

    </div>

    

  
  
</template>

<script>
import Login from "@/components/Login.vue";
import Logout from "@/components/Logout.vue";
import QuestionsList from "@/components/QuestionsList.vue";
import QuestionAdminView from "@/components/QuestionAdminView.vue";
import QuestionEdit from "@/components/QuestionEdit.vue";
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
        QuestionAdminView,
        QuestionEdit
    },

    methods: {
        loggedHandler(logged) {
            this.logged = logged;
        },

        QuestionNumberHandler(index) {
            this.currentQuestion = index;
        },

        EditHandler(edit) {
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