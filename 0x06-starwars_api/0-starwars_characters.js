#!/usr/bin/node

/**
 * Prints all characters of a Star Wars movie
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;
    printCharacters(characters, 0); // Start printing characters from index 0
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) return; // Stop when all characters have been printed

  request(characters[index], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1); // Recursively print the next character
    }
  });
}
