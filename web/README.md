# Main Website & API

Website to do abstractive summarization and handle API Request.

## Demo
[Demo Link](https://pukulenamapi-ntklgukjta-uc.a.run.app/)

## Installation
1. Clone This Repo.
2. Import db.sql to your local mysql server
3. Change DB configuration
4. Install virtualenv

```bash
pip install virtualenv
```
5. Create virtualenv inside web folder

```bash
virtualenv venv
```
6. Activate virtualenv 

```bash
/venv/Scripts/activate
```
7. Install Requirements 

```bash
pip install -r requirements.txt
```
8. Run main.py

```bash
python main.py
```

Note: to be able to do Abstractive summarization, you'll need to run predict app under predict folder.

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




## System Design
We use Cloud Run, Compute Engine, and VPC Connector to deploy this app. 

![alt text](https://i.ibb.co/5MdppkP/Whats-App-Image-2022-06-08-at-10-30-25-AM.jpg)


