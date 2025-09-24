# home-doc-assistant
app to provide medical assisstance at home
This app provides for accurate recommendation on various medical issues that maybe resolved at home .Instances like first aid to any medical conditions or recommending initial medications for various allergies and infection kind of stuffs.

# how to run the app
step-1) clone the repo onto your local machine 

step-2) now make all the necessary changes  

> OPENAI_API_TOKEN={"your open api key"}
> 
> HOST=0.0.0.0
> 
> PORT=<port number> #enter 8080 unless it is already engaged,you can check its status from your terminal
> 
> EMBEDDER_LOCATOR=text-embedding-ada-002
> 
> EMBEDDING_DIMENSION=1536
> 
> MODEL_LOCATOR=gpt-3.5-turbo
> 
> MAX_TOKENS=200
> 
> TEMPERATURE=0.0 #set the temperature (a temperature of 0 yields static responses.for dynamic responses set it around 0.7)
> 
> DROPBOX_LOCAL_FOLDER_PATH="path of your source documents"
> 
<div style="background-color: white; padding: 10px; border: 1px solid #ddd;">
  create a ".env" file and paste the above snippet and change the open-api key and the document paths
</div>

step 4) now if you are want the dockerized app





> locate to the homedoc directory
>
> run
> * docker-compose build
> 
> * docker-compose up
>
> now open the docker desktop app to locate the containers running.Click on the local host links to view the app
>

if you want to run the app without dockerization( recommended  only for MacOs and Linux)
>locate to the homedoc directory
>
>to install the requirements
>* pip install -r requirements.txt 
>
>to run the app
>* python main.py
>
>* streamlit run ui.py
>
>access the ui from the local host link shown


<img width="696" alt="Screenshot 2024-01-03 121416" src="https://github.com/anishhello/home-doc-assistant/assets/133523672/98473ecf-2e6a-40df-b985-26a68080f04c">


# details
* using the OpenAIEmbeddingModel for creating vector embeddings from the source documents and storing them

* using the KNNIndex from pathway package for indexing and  retrieval of k nearest vectors  with respect to the query vector from the database of the embedded vectors

* using the gpt-3.5-turbo as the llm for handling the prompts and generating the responses .As this is a bot for medical assisstance I have kept the temperature 0 to prevent dynamic responses to a specific query.

* using the streamlit ui for hands on ui interface

# docs
 using authentic documents as source files
  * https://actualfirstaid.com/uploads/1/0/4/9/104966051/first_aid_notes_2019.pd

* https://main.mohfw.gov.in/sites/default/files/Notification%20and%20Report%20on%20National%20List%20of%20Essential%20Medicines%2C%202022.pdf


                                            
# home-doc-assistant
