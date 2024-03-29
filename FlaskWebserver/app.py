# Importing the required modules

from flask import Flask, render_template, request, jsonify
import json
# Creating Globals (So i can acces these variables everywhere)
global isLogin
global loginFile
global run

isLogin = None
loginFile = open('lif.lginfo','w')
run = 0

# Creating the Flask object

app = Flask(__name__)

# Listening For connections on the Main directory

@app.route("/",methods=['GET'])

def main():
    
    # Rendering the index file

    return render_template('Login.html')
@app.route("/",methods=['POST'])
def Login():

    uname = request.form['uname']
    passw = request.form['pass']

    try:

        user = [line.rstrip('\n') for line in open('{}')].format(uname)

        if passw == user[1] and uname == user[0]:

            isLogin = True


            loginFile.write('True')

            run = 1

            return render_template('index.html')
        else:
            return render_template('Fail.html')

    except:

        print('Fail')

        return render_template('Fail.html')
    

    
@app.route("/index",methods=['GET','POST'])

def maain():
    
    if isLogin != False:
    # Rendering the index file

        return render_template('index.html')
    else:

        return render_template('noLogin.html')

# Listening For connections on the /procces directory (Only for test)

@app.route("/procces",methods=['POST'])
def sendJson():
    
    # Letting the Code to recive the JSON code

    data = request.get_json()


    # Returning the daba value

    return jsonify({'value':'succes'})

# Listening For connections on the /getNames directory


@app.route("/getNames",methods=['GET'])
def GetNames():

    return jsonify({'resault':'succes'})
@app.route("/anmelden", methods=['POST'])
def Anmelden():

    data = request.get_data().decode()

    card, status = data.split('&')

    Misc, Number = card.split('=')

    Misc, Location = status.split("=")

    print('Rfid Code : ' + Number)
    
    print('Current Location : ' + Location)

    return data

@app.route('/abmelden',methods=['POST'])
def Abmelden():

    data = request.get_json()

    return jsonify({'No':'ErrorsAccoured'})


@app.route("/bin/server.get",methods=['POST'])
def get_cuurent_send_Json():

    data = request.get_json()

    return jsonify(data)


@app.route('/bin',methods=['GET'])
def return_bins():
    return jsonify({''})


@app.route('/nsa/<string:id>/<string:fname>/<string:lname>/<string:kl>/<string:erw1>/<string:erw2>/<string:n1>/<string:n2>',methods=['POST'])
def nsa_nsa(id,fname,lname,kl,erw1,erw2,n1,n2):

    data = request.get_json()

    return jsonify({'....':'....'})


@app.route("/raspberrypi/test/gui",methods=['GET'])
def test_Gui_Raspberrypi():

    return render_template('Raspberrypitest.html')


@app.route("/raspberrypi",methods=['GET'])
def raspberrypi_json_test():

    return jsonify({'JSON':'TEST.rpi'})


@app.route("/test")
def test():

    return "<h1>TEST test </h1>"


@app.route("/sst",methods=['POST'])
def sst():
    data = request.get_data().decode()

    card, status = data.split('&')

    Misc, Number = card.split('=')

    Misc, Status = status.split("=")

    Status,misc = Status.split("%")

    print(f"Debug.Log(Number : {Number}, Status : {Status})")

    return data


@app.route("/del/<string:name>", methods=['DELETE'])
def delete(name):

    print(f'Deleted: {name} and is a Rfid number')

    return jsonify({'...':'...'})

@app.route("/closeServer",methods=['POST'])
def clsServer():

    import os

    os.system('sudo shutdown now')

@app.route("/notfall",methods=['GET'])
def notfall():

    data=request.get_data().decode()

    id = data

    misc, Use = data.split('=')

    print(id)

    print('Identifier = ' + Use)

    return jsonify({'test':'123'})
        
# Getting data from raspberrypis

@app.route('/Data',methods=['POST'])
def Data():

    data = request.get_data()

    print(data)

    data = data.decode()

    Rfid, Status = data.split("&")

    Status, Misc = Status.split('%')

    del Misc

    print(Rfid)
    print(Status)

    return jsonify({'ok':'ok'})

@app.route('/Form')
def maion():
    if isLogin == True:
        return render_template("Online_Reg.html")
    else:

        return render_template('noLogin.html')

@app.route('/Form',methods=['POST'])
def GetValue():
    if isLogin == True:
        name = request.form['firstname']
        lname = request.form['lastname']
        db = request.form['dofb']
        id = request.form['id']

        print(name)
        print(lname)
        print(db)
        print(id)
        return render_template('procces_done.html')
    else:

        return render_template('noLogin.html')

    
@app.route('/Del')
def Delete():
    if isLogin == True:
        return render_template("Del.html")
    else:

        return render_template('noLogin.html')

@app.route("/Del",methods=['POST'])
def Deleite():
    if isLogin == True:
        id = request.form['id']

        print(id)

        return render_template('Done.html')
    else:

        return render_template('noLogin.html')

@app.route("/ea")
def ea():

    return render_template("Te.html")
@app.route("/ea",methods=['POST'])
def eas():

    name = request.form['name']
    lname = request.form['lname']
    email = request.form['email']
    uname = request.form['uname']
    password = request.form['pass']

    for x in (name,lname,email,uname,password):

        print(x)
    return render_template('Done2.html')
@app.route("/an")
def an():


     
    return render_template('noLogin.html')
@app.route("/an", methods=['POST'])
def ani():

    if isLogin == True:

        id = request.form['id']

        print(id)

        return render_template('Done3.html')
    else:
        return render_template('noLogin.html')
@app.route('/ab')
def ad_def():

    return render_template('Abmelden.html')
@app.route("/ab", methods=['POST'])
def ania():

    if isLogin == True:

        id = request.form['id']

        print(id)

        return render_template('Done4.html')
    else:
        return render_template('noLogin.html')

#End/Startup options


from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 


if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=80)