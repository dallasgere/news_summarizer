# news_summarizer

- attempting to build a news summarizer from kaggle CNN article dataset

# My method to all this

**What I wanted from this and what I got**

- Okay so I was going to preprocess my data and then use BART to train a model, but apparently BART has a version thats pre trained on CNN-Daily mail dataset so thats silly of me
  - I think i'll just go through with the experiment anyways and deploy the model. Either way I still learned stuff
  - While I am using pretrained data on the same data set, this is still valuabel process to learn

**Transfer Learning**

- If this was using BART on pre trained CNN-Daily Mail data set and then I used a different data set, That would be considered transfer learning

**Some experiments I could Run to obtain more value from this project**

- I think I am going to try and train more than just BART and then assess performance of each
  - T5(Text-to-Text Transfer Transformer)
  - PEGASUS(Pre-training with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models)
  - BERT(Bidirectional Encoder Representations from Transformers)

# Python Version

- I want to use PyTorch for this and you need to use python 3.12 for this, I was on 3.13 but that is not supported by pytorch yet

# Dataset

- I obtained the data from this dataset
  - https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail/data
