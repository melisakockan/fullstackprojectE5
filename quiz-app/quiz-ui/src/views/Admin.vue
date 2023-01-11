<template>

     <!-- import Font Awesome -->
     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css" integrity="sha512-MV7K8+y+gLIBoVD59lQIYicR65iaqukzvf/nwasF0nqhPay5w/9lJmVM2hMDcnK1OnMGCdVK+iQrJ7lzPJQd1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
 

    <!-- Disconnect -->
    <Logout @logged="loggedHandler" v-if="logged"/>
    <Login @logged="loggedHandler" v-else/>

    <!-- Admin -->
    <div v-if="logged">

        <!-- Create a question -->
        <button id="addQuestion" @click="create = true" v-if="!create & (currentQuestion == null) & !edit & !sound"><i class="fas fa-plus"></i></button>

        <!-- Themes -->
        <button id="manageThemes" @click="sound = true" v-if="!create & (currentQuestion == null) & !edit & !sound"><i class="fas fa-music"></i></button>

        <div v-if="sound & theme_id == null">
            <SoundList @back="sound = false" @theme="themeHandler"/>
        </div>

        <div v-else-if="sound & theme_id != null">
            <SoundAdminView :theme_id="theme_id" @back="theme_id = null" @theme="theme_id = null"/>
        </div>


        <div v-if="create">
            <QuestionEdit :question_number="-1" @edit="EditHandler" @question_created="QuestionNumberHandler"/>
        </div>

        <div v-else-if="(currentQuestion == null) & !edit & !sound">
            <QuestionsList @question_number="QuestionNumberHandler"/>
        </div>
    
        <div v-else-if="(currentQuestion != null) & !edit ">
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
import SoundList from "@/components/SoundList.vue";
import SoundAdminView from "@/components/SoundAdminView.vue";


export default {
    name: 'Admin',

    data() {
        return {
            logged: null,
            currentQuestion: null,
            edit: false,
            create: false,
            sound: false,
            theme_id: null
        }
    },

    components: {
        Login,
        Logout,
        QuestionsList,
        QuestionAdminView,
        QuestionEdit,
        SoundList,
        SoundAdminView
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
        },

        themeHandler(theme_id) {
            this.theme_id = theme_id;
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

#addQuestion, #manageThemes{
    box-sizing: border-box;
    font-size: 20px;
    width: 100px;
    height: 40px;

    background-color: #4CAF50;

    border: none;

    cursor: pointer;
    margin: 10px 0px;
    display: flex;
    justify-content: center;
    align-items: center;

    margin: auto;
    
}

#manageThemes{
    margin-top: 20px;
    background-color: #af4c8b;
    font-size: 20px;
    color: white;
}

#manageThemes:hover {
    background-color: #893e8e;
    color: white;
}

#addQuestion i {
    color: white;
    font-size: 20px;
}

#addQuestion:hover {
    background-color: #3e8e41;
    color: white;
}

</style>