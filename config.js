// change these two variables
let channel = process.env.TWITCH_CHANNEL || "Dischord";
let programName =
  process.env.CONFIG_PROGRAM_NAME || "Mabinogi";
  
// List of commands to check for
let commands = [
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "0",
  "minus",
  "equals",
  "equal",
  
  "esc",
  
  "w",
  "a",
  "s",
  "d",
  "up",
  "down",
  "left",
  "right",
  "inv",
  "target",
  "attack",
  
  "f1",
  "f2",
  "f3",
  "f4",
  "f5",
  "f6",
  "f7",
  "f8",
  "f9",
  "f10",
  "f11",
  "f12",
  
  "whold",
  "ahold",
  "shold",
  "dhold",
  "uphold",
  "lefthold",
  "downhold",
  "righthold",
  "wh",
  "ah",
  "sh",
  "dh",
  "uph",
  "lefth",
  "downh",
  "righth",
  
  
  "brionac",
  "fighter",
  "chains",
  "chain",
  "music",
  "bard",
  "alch",
  "alchemy",
  
  "hp",
  "mp",
  "sp",
  "health",
  "mana",
  "stamina",
  
  "self",
];

let filteredCommands = [];
let throttledCommands = [];

module.exports = {
  // all commands to print out
  commands,
  // twitch channel to connect to
  channel,
  // Title of the window of the program (ex: 'Desmume' or 'VBA')
  programName,

  // If you need to filter the commands sent to the program
  // Ex: democracy/anarchy since they don't affect the program itself
  // Ex: ["democracy","anarchy"]
  filteredCommands,

  // If you want to prevent people from using from command too often
  // Ex: ["start"]
  throttledCommands,

  // Throttle time in seconds
  // Ex: you can limit 'start' so it's only used every 10 sec
  timeToWait: 10000,

  // Delay between each possible keypress in milliseconds (can't be too fast)
  // To change on Windows, change `key.py`
  delay: 100,
};