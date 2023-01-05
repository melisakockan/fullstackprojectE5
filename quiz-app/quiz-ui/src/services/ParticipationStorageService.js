export default {
  clear() {
    window.localStorage.clear();
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("username", playerName);
  },
  getPlayerName() {
    return window.localStorage.getItem("username");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("score", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("score");
  }
};