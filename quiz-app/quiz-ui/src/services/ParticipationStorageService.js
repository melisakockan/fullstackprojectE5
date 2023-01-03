export default {
  clear() {
    window.localStorage.clear();// todo : implement
  },
  savePlayerName(playerName) {
    window.localStorage.setItem("username", playerName);
  },
  getPlayerName() {
    window.localStorage.getItem("username");// todo : implement
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("registeredScores[getPlayerName()]", participationScore);// todo : implement
  },
  getParticipationScore() {
    window.localStorage.getItem(registeredScores[getPlayerName()]);// todo : implement
  }
};