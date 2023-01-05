export default {
  clear() {
    window.localStorage.clear();// todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("username", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("username");// todo : implement
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("score", participationScore);
  },
  getParticipationScore() {
    let name = getPlayerName();
    return window.localStorage.getItem("score");
  }
};