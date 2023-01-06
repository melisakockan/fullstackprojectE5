export default {
    removeToken() {
      this.saveToken(null);
    },
    
    saveToken(token) {
      window.localStorage.setItem("token", token);
    },
  
    getToken() {
      window.localStorage.getItem("token");
    }
  };