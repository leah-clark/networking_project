# setup

`pip install -r requirements.txt
`
# endpoint 

http://127.0.0.1:5000/api/ip_type

json as 

    
    {
        "ip_type": "private"
    }

# run server on windows

in root directory

    $env:FLASK_APP = "app.py"  
    python -m flask run
 
# run server on mac
 
in root directory

`flask run`
 
# run frontend on windows/mac

    cd frontend 
    yarn start

