<template>

<h1>Veuillez vous connecter</h1>

<form id="login_form" @submit.prevent>
    <label for="password">Entrez le mot de passe</label>
    <input name="password" type="password" v-model="password" autocomplete="on">
    <button @click="connect">Se connecter</button>
</form>
  
  
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import AdminStorageService from "@/services/AdminStorageService";

export default {
    name: 'Admin',
    data() {
        return {
            password: null
        }
    },

    methods: {
        async connect() {
            const response = await quizApiService.login(this.password);
            if (response.status === 200) {
                AdminStorageService.setToken(response.data.token);
                alert("Logged !");
            }
            else{
                alert("Mot de passe incorrect");
            }
        }
    }
    
};
</script>


<style>

#login_form{
    margin: 50px 0px;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

#login_form input{
    width: 200px;
    margin: 10px 0px;
    padding : 10px;
    border-radius: 5px;
    font-size: 1.2em;
    color: grey;
}



</style>