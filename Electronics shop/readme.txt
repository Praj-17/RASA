## Step 1 -
 Create a nlu.md file as already prepared in this direcotry, this is similar to the intents.json file that we had already created in the previous project.

 - While creating intents you need to specify weather a particular word in a setence is an entity or not. As like shown in the readme.txt

 - Be aware of the class imbalance factor, try to keep the number of intents in each of the intents more or less equal. If there is a huge gap within the number of intents for entities then the one with more intetns will dominate the others and the model will get biased towards it.

 - Punctuations and emojis are simply ignored

 - Make sure to have all the words in the intents in the lower case 

 ##Step 2 - 
 Create a config.yml file to store all the preprocessing, NLP or Machine learnning that you are applying in a listed format, Rasa will take all your input patterns through this steps
 This is the training file that we created on our own.
 It is just without code.

 ##step 3 - go to your command prompt, cd to the current folder and run the command 
  -- Python -m rasa train nlu

##Step 4 - Now, once your model is trained try to edit your model, by adding some data or changing the config file and now once you are good to go type
-- Python -m rasa shell nlu
This command will enable you to type in your message and it will respoond you with a dictionary of the classified intent, its confidence level , the entities that it has extracted them from , the confidence of entities etc.

##Step 5- synonyms- You can also define synonnyms of a particular word,by using synonym keywords

## You can add multiple categories to a entity by creating a  entity.ext file as like in the nlu.md to create mulitple categories of an entity.


##step -6 Now, once the user input is classfied into an intent, here comes the responses part, for your bot to give a response, you also need to provide a set of RESPONSES  which either be Actions or Utterences , Actions are functions that are to be executed and Utterences are Responses or hard codded text messages that are needed to be sent.

 - Here in the file actions.py we have defined the functions that are needed to be executed in the desired class