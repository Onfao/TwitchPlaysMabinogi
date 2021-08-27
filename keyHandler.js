let exec = require("child_process").exec,
  config = require("./config.js"),
  lastTime = {},
  windowID = "unfilled",
  throttledCommands = config.throttledCommands,
  regexThrottle = new RegExp("^(" + throttledCommands.join("|") + ")$", "i"),
  regexFilter = new RegExp(
    "^(" + config.filteredCommands.join("|") + ")$",
    "i"
  );

let isWindows = process.platform === "win32";

(function setWindowID() {
  if (!isWindows & windowID === "unfilled") {
    exec("xdotool search --onlyvisible --name " + config.programName, function (
      error,
      stdout
    ) {
      windowID = stdout.trim();
      // console.log(key, windowID);
    });
  }
})();

for (let i = 0; i < throttledCommands.length; i++) {
  lastTime[throttledCommands[i]] = new Date().getTime();
}

let defaultKeyMap = config.keymap || {
  1: "1",
  2: "2",
  3: "3",
  4: "4",
  5: "5",
  6: "6",
  7: "7",
  8: "8",
  9: "9",
  0: "0",
  minus: "minus",
  equals: "equals",
  equal: "equals",
  
  esc: "Esc",
  w: "W",
  a: "A",
  s: "S",
  d: "D",
  up: "W",
  down: "S",
  left: "A",
  right: "D",
  inv: "I",
  target: "Target",
  attack: "Attack",
  f1: "F1",
  f2: "F2",
  f3: "F3",
  f4: "F4",
  f5: "F5",
  f6: "F6",
  f7: "F7",
  f8: "F8",
  f9: "F9",
  f10: "F10",
  f11: "F11",
  f12: "F12",
  
  whold: "whold",
  ahold: "ahold",
  shold: "shold",
  dhold: "dhold",
  uphold: "whold",
  lefthold: "ahold",
  downhold: "shold",
  righthold: "dhold",
  self: "self",
  wh: "whold",
  ah: "ahold",
  sh: "shold",
  dh: "dhold",
  uph: "whold",
  lefth: "ahold",
  downh: "shold",
  righth: "dhold",
  
  brionac: "brionac",
  fighter: "fighter",
  chains: "chains",
  chain: "chains",
  music: "music",
  bard: "music",
  alch: "alch",
  alchemy: "alch",
  
  
  hp: "H",
  mp: "J",
  sp: "K",
  health: "H",
  mana: "J",
  stamina: "K",
  
  terminate: "terminate",
};

function sendKey(command) {
  //if doesn't match the filtered words
  if (!command.match(regexFilter)) {
    let allowKey = true;
    let key = defaultKeyMap[command] || command;
    if (allowKey) {
		exec("python key.py" + "  " + config.programName + " " + key);
    }
  }
}

exports.sendKey = sendKey;
