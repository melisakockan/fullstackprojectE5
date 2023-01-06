export default {
    removeToken() {
      window.localStorage.removeItem("token");
    },
    
    saveToken(token) {
      window.localStorage.setItem("token", token);
    },
  
    getToken() {
      return window.localStorage.getItem("token");
    },

    isTokenValid() {
      if (localStorage.hasOwnProperty("token") == true) {
          if (this.getToken() != null){
            return true;
          }
      }

      return false;
    }
  };