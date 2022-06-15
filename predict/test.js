const axios = require('axios');
let config = {
    headers: {
        'x-api-key': '0fa082af97380ffdecee051edb6b0b80',
    }
}

let data = {
    'news': 'Selain nikel, kata Bamsoet, Indonesia juga kaya material komponen penting untuk industri baterai, seperti alumunium sebesar 1,2 miliar ton, tembaga 51 miliar ton, dan mangan 43 miliar ton.'
}

axios.post('https://pukulenamapi-ntklgukjta-uc.a.run.app/api/summarize', data, config)
    .then(res => {
        // console.log(`statusCode: ${res.status}`);
        console.log(res.data.summarized);
    })
    .catch(error => {
        console.error(error);
    });








// ####################################




// var axios = require('axios');
// var data = JSON.stringify({
//     "news": "Selain nikel, kata Bamsoet, Indonesia juga kaya material komponen penting untuk industri baterai, seperti alumunium sebesar 1,2 miliar ton, tembaga 51 miliar ton, dan mangan 43 miliar ton."
// });

// var config = {
//     method: 'post',
//     url: 'https://predictapi-ntklgukjta-uc.a.run.app/api/summarize',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     data: data
// };

// axios(config)
//     .then(function (response) {
//         console.log(JSON.stringify(response.data));
//     })
//     .catch(function (error) {
//         console.log(error);
//     });

