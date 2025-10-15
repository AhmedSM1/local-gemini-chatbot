To run this application 
<uL>
<li>1- you will need token from Google Gemini  https://aistudio.google.com/</li>
<li>2- add it in .env</li>
<li>3- install all the packages running  pip install -r requirements.txt </li>
<li> 4- run the application python3 -m uvicorn main:app  </li>
  
</uL>
                                              

Endpoints:

POST  localhost:8000/api/gemini
Request body 
{
  "prompt": "Your Prompt"

}
