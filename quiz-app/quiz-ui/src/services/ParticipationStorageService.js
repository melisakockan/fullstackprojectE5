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
    let name = getPlayerName();
    window.localStorage.setItem("registeredScores[" + name + "]", participationScore);

    // window.localStorage.setItem("registeredScores[getPlayerName()]", participationScore);// todo : implement
  },
  getParticipationScore() {
    let name = getPlayerName();
    window.localStorage.getItem("registeredScores[" + name + "]");
  }
};