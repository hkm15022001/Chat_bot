const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
// read from json file
const rawData = fs.readFileSync('data/content.json');
const data = JSON.parse(rawData);
//generate test data
const getRandomPatterns = (data) => {
  const dataIntents = data.intents;

  const testIntent = dataIntents.map((dataIntent, index) => {
    const patternCount = dataIntent.patterns.length;
    const testPatterns = []
    let i = 0
    //test data = 1/5 total data
    while (i < Math.round((dataIntent.patterns.length) / 5)) {
      const randomPattern = dataIntent.patterns[Math.floor(Math.random() * patternCount)];
      if (!testPatterns.includes(randomPattern)) {
        testPatterns.push(randomPattern);
        ++i;
      }
    }
    return {
      tag: dataIntent.tag,
      patterns: testPatterns,
      response: dataIntent.responses
    }
  });
  return testIntent;
}
//substract file
const subData = (data, subData) => {
  const dataIntents = data.intents;
  const subDataIntents = subData.intents;
  dataIntents.forEach((dataIntent) => {
    subDataIntents.forEach((subDataIntent) => {
      if (dataIntent.tag === subDataIntent.tag) {
        dataIntent.patterns = dataIntent.patterns.filter((ele) => !subDataIntent.patterns.includes(ele))
        // console.log("trong vong lap",dataIntents)
      }
    })
  })
  return dataIntents
}
//save to file
const saveJsonFlie = (fileName, jsonString) => {
  fs.writeFile(fileName, jsonString, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    } else {
      console.log('JSON object has been saved to ', fileName);
    }
  });
}
// number of test you want
const testIntents = getRandomPatterns(data);
const testData = {
  intents: testIntents
}
//get data file after substract test file
const trainIntents = subData(data, testData)
const dataTrain = {
  intents: trainIntents
}
const testJson = JSON.stringify(testData);
const trainJson = JSON.stringify(dataTrain);

saveJsonFlie("data/test_content.json", testJson);
saveJsonFlie("data/train_content.json", trainJson);
