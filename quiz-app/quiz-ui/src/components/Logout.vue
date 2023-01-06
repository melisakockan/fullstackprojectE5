<template>

    <!-- Disconnect -->
    <div id="disconnect">
        <button @click="disconnect">Se déconnecter</button>
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

</style>