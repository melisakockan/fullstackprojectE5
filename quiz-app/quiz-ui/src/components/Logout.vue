<template>

    <!-- Disconnect -->
    <div id="disconnect">
        <button @click="disconnect" class="fas fa-sign-out-alt"></button>
    </div>
    
  
</template>

<script>
import AdminStorageService from "@/services/AdminStorageService";


export default {
    name: 'Logout',

    emits : ['logged'],

    methods: {
        disconnect() {
            AdminStorageService.removeToken();
            this.$emit('logged', false);
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

#disconnect button{
    background-color: #d63031;
    border-radius: 10px;
    border: none;
    color: #fff;
    font-size: 1.5em;
    cursor: pointer;
}

#disconnect button:hover{
    background-color: #ef4d4d;
}

</style>