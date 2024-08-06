# ok so im having a problem its not loading on the site but i'll continue incase the problem is my chromebook

from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase


app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCDE"
socketio = SocketIO(app)

rooms = {}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break

    return code





@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)
        #the button have empty values
        
        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)
        

        if join != False and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        #!= does not equal
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
        

        session["room"] = room
        session["name"] = name
        return redirect(url_for('room'))
        


#constant rendering of the room automated 
    return render_template("home.html")


@app.route("/room")
def room():
    room = session.get("room")
    if room is None or session.get("name") is None or room  not in rooms:
        return redirect(url_for("home"))
    


    return render_template("room.html", code=room, messages=rooms[room]["messages"])


@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return 
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")




#how to create roots 


@socketio.on("connect")
#connecting to the room

def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return

    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")

#An f-string (formatted string literal) in Python is a way to embed expressions inside string literals using curly braces {}. Introduced in Python 3.6, f-strings provide a concise and readable way to format strings

@socketio.on("disconnect")
#disconnecting
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["memebers"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")




if __name__ == "__main__":
    socketio.run(app, debug=True)

