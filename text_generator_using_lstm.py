# -*- coding: utf-8 -*-
"""text generator using LSTM

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mn0-dSXMTfJc4fmS4dTVi99bVJtjFwsm
"""

# Import libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the text
with open('/content/story.txt', 'r') as file:
    story = file.read()

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer()

tokenizer.fit_on_texts([story])

len(tokenizer.word_index)

input_sequences = []
for sentence in story.split('\n'):
  tokenized_sentence = tokenizer.texts_to_sequences([sentence])[0]

  for i in range(1,len(tokenized_sentence)):
    input_sequences.append(tokenized_sentence[:i+1])

input_sequences

max_len = max([len(x) for x in input_sequences])

from tensorflow.keras.preprocessing.sequence import pad_sequences
padded_input_sequences = pad_sequences(input_sequences, maxlen = max_len, padding='pre')

padded_input_sequences

X = padded_input_sequences[:,:-1]

y = padded_input_sequences[:,-1]

X.shape

y.shape

from tensorflow.keras.utils import to_categorical
y = to_categorical(y,num_classes=8932)

y.shape

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

model = Sequential()
model.add(Embedding(8932 ,100, input_length=20))
model.add(LSTM(500))
model.add(LSTM(500))
model.add(Dense(8932 ,activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])

model.summary()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Define the model
model = Sequential()

# Add the embedding layer
model.add(Embedding(input_dim=8932, output_dim=19, input_length=20))

# Add LSTM layers
model.add(LSTM(500, return_sequences=True))  # Use return_sequences=True for stacking LSTM
model.add(LSTM(500))

# Add Dense layer with softmax activation
model.add(Dense(8932, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Display the model summary
model.summary()