from flask import Flask,jsonify,request
app=Flask(__name__)

list=[
    {
        'id':1,
        'Name':u'jack',
        'Contact':u'none',
        'done':False,

    },
    {
        'id':2,
        'Name':u'john',
        'Contact':u'random',
        'done':False
    }
]


@app.route("/add-data",methods=["POST"])
def add_Task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide data",

        },400)
    
    contact={
        'id':list[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact'," "),
        'done':False

    }




    list.append(contact)
    return jsonify({
        "status":"success",
        "message":"task added succesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":list,

    })

if(__name__=="__main__"):
    app.run(debug=True)
    
    
    

