import quizApiService from "@/services/QuizApiService";

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
    },

    async checkToken() {
      const response = await quizApiService.call("get", "checktoken", null, this.getToken());

      if (response.status === 200) {
        return true;
      } 
      else {
        return false;
      }
    }

  };