export default {
    removeToken() {
      window.localStorage.saveToken(null);
    },
    
    saveToken(token) {
      window.localStorage.setItem("token", token);
    },
  
    getToken() {
      window.localStorage.getItem("token");
    }
  };