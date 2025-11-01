from flask import Flask, render_template, request, url_for, redirect

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print ("yo, index")
    if request.method== "POST":
        name= request.form.get("name")
        print(name)
        door=request.form.get("door")
        if request.form.get("door") == "oak":
            return render_template("oak.html", name = name)


    else:
        return render_template("index.html")

@app.route("/oak",methods=["POST"])
def oak():
    if request.method== "POST":
        name= request.form.get("name")
        route=request.form.get("route")
        if route == "run":
            return render_template("run.html", name = name, route= route)
        else:
            return render_template("walk.html", name=name, route=route)

@app.route("/spruce",methods=["POST"])
def spruce():
    if request.method== "POST":
        name = request.form.get("name")
        action = request.form.get("action")
        if action == "sword":
            return render_template("sword.html", name=name,action=action)
        elif action == "closest":
            return render_template("closest.html", name=name, action=action)
        elif action == "freeze":
            return render_template("freeze.html", name=name, action=action)
        else:
            return render_template("talk.html", name=name, action=action)

@app.route("/run", methods=["POST"])
def run():
    if request.method=="POST":
        name = request.form.get("name")
        art = request.form.get("art")
        if art == "brush":
            return render_template("brush.html", name=name, art=art)
        if art == "pigment":
            return render_template("pigment.html", name=name, art=art)
        if art == "painting":
            return render_template("painting.html", name=name, art=art)

@app.route("/pigment", methods=["POST"])
def pigment():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.getlist("paints")

        paints= f'{", ".join(paints)}'

        return render_template("next.html", name=name, paints=paints)

@app.route("/walk",methods=["POST"])
def walk():
    if request.method== "POST":
        name= request.form.get("name")

@app.route("/brush",methods=["POST"])
def brush():
    if request.method== "POST":
        name= request.form.get("name")

@app.route("/painting", methods=["POST"])
def painting():
    if request.method=="POST":
        name = request.form.get("name")
        shade = request.form.get("shade")
        if shade == "talker":
            return render_template("talker.html", name=name, shade=shade)
        if shade == "unsheath":
            return render_template("unsheath.html", name=name, shade=shade)

@app.route("/talker", methods=["POST"])
def talker():
    if request.method=="POST":
        name = request.form.get("name")
        hand = request.form.get("hand")
        if hand == "yes":
            return render_template("yes.html", name=name, hand=hand)
        if hand == "no":
            return render_template("no.html", name=name, hand=hand)



@app.route("/unsheath", methods=["POST"])
def unsheath():
    if request.method=="POST":
        name = request.form.get("name")
        killer = request.form.get("killer")
        if killer == "crawl":
            return render_template("crawl.html", name=name, killer=killer)
        if killer == "brush":
            return render_template("brush.html", name=name, killer=killer)


@app.route("/yes", methods=["POST"])
def yes():
    if request.method=="POST":
        name = request.form.get("name")
        friendly = request.form.get("friendly")
        if friendly == "crawl2":
            return render_template("crawl2.html", name=name, friendly=friendly)
        if friendly == "brush":
            return render_template("brush.html", name=name, friendly=friendly)


@app.route("/no", methods=["POST"])
def no():
    if request.method=="POST":
        name = request.form.get("name")
        come_on = request.form.get("come_on")
        if come_on == "brush":
            return render_template("brush.html", name=name, come_on=come_on)
        if come_on == "unsheath":
            return render_template("unsheath.html", name=name, come_on=come_on)


@app.route("/crawl", methods=["POST"])
def crawl():
    if request.method=="POST":
        name = request.form.get("name")
        throne_room = request.form.get("throne_room")
        if throne_room == "pick_up":
            return render_template("pick_up.html", name=name, throne_room=throne_room)
        if throne_room == "sit":
            return render_template("sit_killer.html", name=name, throne_room=throne_room)
        if throne_room == "walk_out":
            return render_template("walk_out.html", name=name, throne_room=throne_room)


@app.route("/crawl2", methods=["POST"])
def crawl2():
    if request.method=="POST":
        name = request.form.get("name")
        throne_room_friendly = request.form.get("throne_room_friendly")
        if throne_room_friendly == "pick_up":
            return render_template("pick_up.html", name=name, throne_room_friendly=throne_room_friendly)
        if throne_room_friendly == "sit_friendly":
            return render_template("sit.html", name=name, throne_room_friendly=throne_room_friendly)
        if throne_room_friendly == "walk_out":
            return render_template("walk_out.html", name=name, throne_room_friendly=throne_room_friendly)


@app.route("/next", methods=["POST"])
def next():
    if request.method=="POST":
        name = request.form.get("name")
        next = request.form.get("next")
        paints = request.form.get("paints")
        if next == "brush":
            return render_template("brush.html", name=name, next=next, paints=paints)
        if next == "painting_paints":
            return render_template("painting_paints.html", name=name, next=next, paints=paints)

@app.route("/nextkid", methods=["POST"])
def nextkid():
    if request.method=="POST":
        name = request.form.get("name")
        pigments_shade = request.form.get("pigments_shade")
        paints = request.form.get("paint")
        if pigments_shade == "brush":
            return render_template("brush.html", name=name, pigments_shade=pigments_shade, paints=paints)
        if pigments_shade == "back_shade":
            return render_template("back_shade.html", name=name, pigments_shade=pigments_shade, paints=paints)


@app.route("/back_shade", methods=["POST"])
def back_shade():
    if request.method=="POST":
        name = request.form.get("name")
        onwards = request.form.get("onwards")
        paints = request.form.get("paint")
        paints = request.form.get("paints")
        return render_template("crawl2.html", name=name, onwards=onwards, paints=paints)

@app.route("/next_killer", methods=["POST"])
def next_killer():
    if request.method=="POST":
        name = request.form.get("name")
        next_killer = request.form.get("next_killer")
        paints = request.form.get("paint")
        paints = request.form.get("paints")
        if next_killer == "through":
            return render_template("crawl.html", name=name, next_killer=next_killer, paints=paints)


@app.route("/walk_out", methods=["POST"])
def walk_out():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paint")
        paints = request.form.get("paints")


@app.route("/painting_paints", methods=["POST"])
def painting_paints():
    if request.method=="POST":
        name = request.form.get("name")
        real = request.form.get("real")
        paints = request.form.get("paints")
        if real == "unsheath1":
            return render_template("unsheath_painting.html", name=name, real=real, paints=paints)
        if real == "talker2":
            return render_template("talker_painting.html", name=name, real=real, paints=paints)


@app.route("/crawl_killer_painting", methods=["POST"])
def crawl_killer_painting():
    if request.method=="POST":
        name = request.form.get("name")
        throne_room_paints_killer = request.form.get("throne_room_paints_killer")
        paints = request.form.get("paints")
        if throne_room_paints_killer == "sit":
            return render_template("sit_killer_paints.html", name=name, throne_room_paints_killer=throne_room_paints_killer, paints=paints)
        if throne_room_paints_killer == "walk_out":
            return render_template("walk_out_paints.html", name=name, throne_room_paints_killer=throne_room_paints_killer, paints=paints)


@app.route("/talker_painting", methods=["POST"])
def talker_painting():
    if request.method=="POST":
        hand_paints = request.form.get("hand_paints")
        name = request.form.get("name")
        paints = request.form.get("paints")
        if hand_paints == "yes":
            return render_template("yes_paints.html", name=name, hand_paints=hand_paints, paints=paints)
        if hand_paints == "no":
            return render_template("no_paints.html", name=name, hand_paints=hand_paints, paints=paints)


@app.route("/no_paints", methods=["POST"])
def no_paints():
    if request.method=="POST":
        come_on_paints = request.form.get("come_on_paints")
        name = request.form.get("name")
        paints = request.form.get("paints")
        if come_on_paints == "brush":
            return render_template("brush.html", name=name, come_on_paints=come_on_paints, paints=paints)
        if come_on_paints == "unsheath":
            return render_template("unsheath_painting.html", name=name, come_on_paints=come_on_paints, paints=paints)

@app.route("/yes_paints", methods=["POST"])
def yes_paints():
    if request.method=="POST":
        friendly_painting = request.form.get("friendly_painting")
        name = request.form.get("name")
        paints = request.form.get("paints")
        if friendly_painting == "crawl3":
            return render_template("crawl2_paints.html", name=name, friendly_painting=friendly_painting, paints=paints)
        if friendly_painting == "brush3":
            return render_template("brush.html", name=name, friendly_painting=friendly_painting, paints=paints)


@app.route("/unsheath_painting", methods=["POST"])
def unsheath_painting():
    if request.method=="POST":
        name = request.form.get("name")
        killer_unsheath = request.form.get("killer_unsheath")
        paints = request.form.get("paints")
        if killer_unsheath == "crawl3":
            return render_template("crawl_killer_painting.html", name=name, killer_unsheath=killer_unsheath, paints=paints)
        if killer_unsheath == "brush1":
            return render_template("brush.html", name=name, killer_unsheath=killer_unsheath, paints=paints)


@app.route("/crawl2_paints", methods=["POST"])
def crawl2_paints():
    if request.method=="POST":
        name = request.form.get("name")
        throne_room_friendly_paints = request.form.get("throne_room_friendly_paints")
        paints = request.form.get("paints")
        if throne_room_friendly_paints == "sit_friendly_paints":
            return render_template("sit_paints.html", name=name, throne_room_friendly_paints=throne_room_friendly_paints, paints=paints)
        if throne_room_friendly_paints == "walk_out_paints":
            return render_template("walk_out_paints.html", name=name, throne_room_friendly_paints=throne_room_friendly_paints, paints=paints)


@app.route("/sit", methods=["POST"])
def sit():
    if request.method=="POST":
        name = request.form.get("name")
        decision = request.form.get("decision")
        if decision == "return":
            return render_template("return1.html", name=name, decision=decision)
        if decision == "alone":
            return render_template("alone.html", name=name, decision=decision)


@app.route("/sit_killer", methods=["POST"])
def sit_killer():
    if request.method=="POST":
        name = request.form.get("name")
        decision_killer = request.form.get("decision_killer")
        if decision_killer == "return_killer":
            return render_template("return_killer.html", name=name, decision_killer=decision_killer)
        if decision_killer == "cut":
            return render_template("cut.html", name=name, decision_killer=decision_killer)


@app.route("/sit_killer_paints", methods=["POST"])
def sit_killer_paints():
    if request.method=="POST":
        name = request.form.get("name")
        decision_killer_paints = request.form.get("decision_killer_paints")
        if decision_killer_paints == "return_paints":
            return render_template("return_killer_paints.html", name=name, decision_killer_paints=decision_killer_paints)
        if decision_killer_paints == "cut_paints":
            return render_template("cut_paints.html", name=name, decision_killer_paints=decision_killer_paints)


@app.route("/return_killer", methods=["POST"])
def return_killer():
    if request.method=="POST":
        name = request.form.get("name")


@app.route("/return_killer_paints", methods=["POST"])
def return_killer_paints():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paints")


@app.route("/cut_paints", methods=["POST"])
def cut_paints():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paints")


@app.route("/cut", methods=["POST"])
def cut():
    if request.method=="POST":
        name = request.form.get("name")


@app.route("/sit_paints", methods=["POST"])
def sit_paints():
    if request.method=="POST":
        name = request.form.get("name")
        decision_paints = request.form.get("decision_paints")
        paints = request.form.get("paints")
        if decision_paints == "return_paints":
            return render_template("return_paints.html", name=name, decision_paints=decision_paints, paints=paints)
        if decision_paints == "alone_paints":
            return render_template("alone_paints.html", name=name, decision_paints=decision_paints, paints=paints)
        if decision_paints == "paint_paints":
            return render_template("paint_paints.html", name=name, decision_paints=decision_paints, paints=paints)

@app.route("/return1", methods=["POST"])
def return1():
    if request.method=="POST":
        name = request.form.get("name")


@app.route("/return_paints", methods=["POST"])
def return_paints():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paints")


@app.route("/alone", methods=["POST"])
def alone():
    if request.method=="POST":
        name = request.form.get("name")


@app.route("/alone_paints", methods=["POST"])
def alone_paints():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paints")


@app.route("/paint_paints", methods=["POST"])
def paint_paints():
    if request.method=="POST":
        name = request.form.get("name")
        paints = request.form.get("paints")


if __name__ == "__main__":
    app.run()
