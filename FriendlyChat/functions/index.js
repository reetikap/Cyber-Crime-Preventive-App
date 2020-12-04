const functions = require('firebase-functions');
const fetch = require("node-fetch");
const admin = require('firebase-admin');
admin.initializeApp();

exports.myFunction = functions.firestore
  .document('messages/{messageId}')
  .onCreate( async (snap, context) => {
const newValue = snap.data();
const name = newValue.name;
const text = newValue.text;

let response = await fetch('http://sentimentanalysis-env.eba-reu7wtes.us-east-1.elasticbeanstalk.com/',
{method: 'POST',header: 
{'Content-Type': 'application/json;charset=utf-8'}, 
body: text });
let res = await response.json();
//var result = JSON.stringify(res);
var result = JSON.stringify(res, function (key, value) {
  if (key === "sentiment") {
	if(value === "negative") {
    		return snap.ref.set({
        text: "Message deleted"
      }, {merge: true});
	}
  } else {
    return value;
  }
});
console.log(result);
});
