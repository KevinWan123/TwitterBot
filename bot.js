require('dotenv').config();

const Twitter = require('twitter');

// Make an ENV file and set your api_key to your twitter developer env key
myKey = process.env.API_KEY

secrectKey = process.env.SECRECT_KEY
accessToken = process.env.ACCESES_TOKEN
accessSecret = process.env.ACCESS_SECRET
bearer_token = process.env.BEAR
console.log(myKey,secrectKey)
const client = new Twitter({
    consumer_key: myKey,
    consumer_secret: secrectKey,
    access_token_key: accessToken,
    access_token_secret: accessSecret,
    bearer_token: bearer_token,
    
  });


  const fs = require('fs');

  client.get('search/tweets', { q: 'ai' }, function(error, tweets, response) {
    if (!error) {
      // Write the list of tweets to a JSON file
      fs.writeFileSync('tweets.json', JSON.stringify(tweets));
    }
    else{
        console.error(error)
    }
  });

// Send out a twitter tweet


//   client.post('statuses/update', { status: 'Testing Twitter API, ignore this tweet' },(error, tweet, response) => {
//     if (error) {
//         console.error(error)}
//     else {
//         console.log(tweet)
//     }
    
//   }

//   )