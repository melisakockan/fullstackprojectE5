export default {
    clear() {
      window.localStorage.clear();
    },
    
    saveToken(token) {
      window.localStorage.setItem("token", token);
    },
  
    getToken() {
      window.localStorage.getItem("token");
    }
  };