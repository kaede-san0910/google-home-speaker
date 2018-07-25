const googlehome = require('google-home-notifier');
const lang = 'en';

word = process.argv[2];

googlehome.ip('192.168.0.6'); //ここで指定
googlehome.device('Google-Home', lang);
googlehome.notify(word, function(res){
    console.log(res);
});
