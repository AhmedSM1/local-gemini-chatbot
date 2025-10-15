To run this application 
1- you will need token from Google Gemini  https://aistudio.google.com/
2- add it in .env
3- install all the packages running  pip install -r requirements.txt 
4- run the application python3 -m uvicorn main:app                                                

Endpoints:

POST  localhost:8000/api/gemini
Request body 
{
  "prompt": "Your Prompt"

}
