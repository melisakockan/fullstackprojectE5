<template>

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>
    <Login @logged="loggedHandler" v-else/>

    <!-- Admin -->
    <div v-if="logged">

        <!-- Create a question -->

        <button @click="create = true" v-if="!create & (currentQuestion == null) & !edit">Create a question</button>

        <div v-if="create">
            <QuestionEdit :question_number="-1" @edit="EditHandler" @question_created="QuestionNumberHandler"/>
        </div>

        <div v-else-if="(currentQuestion == null) & !edit">
            <QuestionsList @question_number="QuestionNumberHandler"/>
        </div>
    
        <div v-else-if="(currentQuestion != null) & !edit">
            <QuestionAdminView :question_number="currentQuestion" @question_number="QuestionNumberHandler" @edit="EditHandler"/>
        </div>

        <div v-else-if="edit">
            <QuestionEdit :question_number="currentQuestion" @edit="EditHandler"/>
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
            edit: false,
            create: false
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
            this.create = false;
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