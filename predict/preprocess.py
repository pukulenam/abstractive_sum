from traceback import print_tb
import regex as re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import tensorflow as tf
from tensorflow.keras import  preprocessing as kprocessing #(2.6.0)
import numpy as np


def predict(news):

  stopword = stopwords.words("indonesian")

  input = re.sub("[-()\"#/@;:<>{}`+=~|.!?,]", "", news)

  temp=""
  text=news.split(" ")
  for word in text:
    if word not in stopword:
      temp = temp+" "+word
  input = temp

  list_x_inp = []
  list_x_inp.append(input.strip())
  list_y_inp = []
  list_y_inp.append("xstartx xendx")

  num_word = 10000
  tokenizer = kprocessing.text.Tokenizer(num_words=num_word, lower=True, split=' ', oov_token=None)
  tokenizer.fit_on_texts(list_x_inp)
  tokenizer.fit_on_texts(list_y_inp)
  art_text2seq = tokenizer.texts_to_sequences(list_x_inp)
  y_input = tokenizer.texts_to_sequences(list_y_inp)
  ## padding sequence
  x = kprocessing.sequence.pad_sequences(art_text2seq, 
                                              maxlen=500, padding='post', truncating="post")
  y = kprocessing.sequence.pad_sequences(y_input, 
                                              maxlen=1, padding='post', truncating="post")


  list_x=x.tolist()
  list_y=y.tolist()


  # Load JSON vocabulary
  import json
    
  # Opening JSON file
  f = open('data.json')
    
  # returns JSON object as 
  # a dictionary
  vocab = json.load(f)


  x = x.reshape(1,-1)

  ## encode X
  # encoder_out, state_h, state_c = encoder_model.predict(x) #Call encoder model

  new_x=x.tolist()

  try:
    encoder_model = tf.keras.models.load_model('my_model_encoder')
    decoder_model = tf.keras.models.load_model('my_model_decoder')
    # Check its architecture

  except Exception as e:    
    print (str(e))


  encoder_out, state_h, state_c = encoder_model.predict(x)
  special_tokens = ("xstartx", "xendx")
  ## prepare loop
  ## sum_input = np.zeros(shape=(300, 0, 0, 0))
  y_inp = np.array([tokenizer.word_index[special_tokens[0]]])
  y_expand=np.expand_dims(y_inp,axis=1)
  predicted_text = ""
  stop = False
  while not stop:
      ## predict dictionary probability distribution
      probs, new_state_h, new_state_c = decoder_model.predict(
                        [y_expand, encoder_out, state_h, state_c])
      
      ## get predicted word
      voc_idx = np.argmax(probs[0,-1,:],axis=0)
      if voc_idx == 0:
        break
      # print(voc_idx)
      pred_word = vocab[str(voc_idx)]
      
      ## check stop
      if (pred_word != special_tokens[1]) and (len(predicted_text.split()) < 15):
        predicted_text = predicted_text +" "+ pred_word
        # print(predicted_text)
      else:
        stop = True
      
      ## next
      y_inp = np.array([voc_idx])
      y_expand=np.expand_dims(y_inp,axis=1)
      state_h, state_c = new_state_h, new_state_c

  try:
    return(predicted_text)
    # Check its architecture

  except Exception as e:   
    return(str(e))


