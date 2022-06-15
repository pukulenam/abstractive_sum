# Machine Learning Model Deployment

Deploy ML Model using flask framework

## Installation
1. Clone This Repo.
2. Install virtualenv
```bash
pip install virtualenv
```
3. Create virtualenv inside predict folder

```bash
virtualenv venv
```
4. Activate virtualenv 

```bash
/venv/Scripts/activate
```


5. Install Requirements 

```bash
pip install -r requirements.txt
```
6. Run main.py

```bash
python main.py
```

## API Request

URL : [https://pukulenamapi-ntklgukjta-uc.a.run.app/api/summarize](https://pukulenamapi-ntklgukjta-uc.a.run.app/api/summarize) 

Method : POST

Header: 'x-api-key' : '0fa082af97380ffdecee051edb6b0b80' 


body : "news": "String berita"

Example API Request using NodeJS-Axios
```javascript
var axios = require('axios');
var data = JSON.stringify({
  "news": "your news here"
});

var config = {
  method: 'post',
  url: 'https://pukulenamapi-ntklgukjta-uc.a.run.app/api/summarize',
  headers: { 
    'Content-Type': 'application/json', 
    'x-api-key': '0fa082af97380ffdecee051edb6b0b80'
  },
  data : data
};

axios(config)
.then(function (response) {
  // get summarized news 
  console.log(response.data.summarized)
})
.catch(function (error) {
  //   error code
  console.log(error.code);
  // eror message
  console.log(error.response.data.message);
});
```