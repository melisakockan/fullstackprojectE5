import axios from "axios";

import AdminStorageService from "@/services/AdminStorageService";

const instance = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        return({ status: error.response.status, data: error.response.data })
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");

  },
  getQuestion(id) {
    return this.call("get", `questions/${id}`);
  },

  addParticipation(name, choices){
    return this.call("post", "participations", {"playerName" : name, "answers" : choices});
  },

  login(password){
    return this.call("post", "login", {"password" : password});
  },

  getAllQuestions(){
    return this.call("get", "questions/all");
  },

  deleteQuestion(id){
    const token = AdminStorageService.getToken();
    return this.call("delete", `questions/${id}`, null, token);
  },

  addQuestion(question){
    const token = AdminStorageService.getToken();
    return this.call("post", "questions", question, token);
  },

  updateQuestion(question, id){
    const token = AdminStorageService.getToken();
    return this.call("put", `questions/${id}`, question, token);
  },

  getQuestionByPosition(position){
    return this.call("get", `questions?position=${position}`);
  },

  createQuestion(question){
    const token = AdminStorageService.getToken();
    return this.call("post", "questions", question, token);
  },

  getTheme(name){
    return this.call('get', `themes/${name}`);
  },

  getThemeById(id){
    return this.call('get', `themes/id/${id}`);
  },

  getAllThemes(){
    return this.call('get', 'themes/all');
  },

  updateTheme(theme){
    const token = AdminStorageService.getToken();
    return this.call('put', `themes/${theme.id}`, theme, token);
  },

  createTheme(theme){
    const token = AdminStorageService.getToken();
    return this.call('post', `themes`, theme, token);
  },

  deleteTheme(id){
    const token = AdminStorageService.getToken();
    return this.call('delete', `themes/${id}`, null, token);
  }

};