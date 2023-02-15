



We don't have to have a fully fledged GPT at the start. There is no reason why our product needs to be able to make stories up. It just needs to be really good at figuring out the API call positions, executing them, and giving intuitive feedback to the user.


Basic Product Usage Loop:
Audio to text whisper
        |
        V
Text to toolformer
        |
        V
toolformer to text
        |
        V
Text to audio


In depth product workflow:
open app
type your need
buddy will parse text into tokens
tokens go into toolformer
toolformer finds api call position
figures out what params are needed
goes into user information and retrieves params
if no info, then it will ask you
user inputs info
info is saved
model does the api call with params
api call returns status
status is then outputted to user






hey buddy
listening
can you do XYZ
    |
    |
    V
audio is recorded and turned into text
text is then fed into huggingface GPT-J
    |
    |
    V
sure thing, ill try and do xyz
GPT-J does inference
this text is added to dataset for future training
    |
    |
    V



