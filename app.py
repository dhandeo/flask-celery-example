from os import path, environ
import json
from flask import Flask, Blueprint, abort, jsonify, request, session
import settings
from celery import Celery, current_task
from tasks import add
from time import sleep
from flask import render_template

app = Flask(__name__)
app.config.from_object(settings)

@app.route("/")
def hello_world(x=16, y=16):
    x = int(request.args.get("x", x))
    y = int(request.args.get("y", y))
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    task = "wait for %d seconds and then return %d" % (x, y)
    goto = "{}".format(context['id'])
    return render_template("task.html", task=task, goto="http://127.0.0.1:5000/result/", task_id=str(context['id']))

@app.route("/result/<task_id>")
def show_result(task_id):
    ret = add.AsyncResult(task_id)
    return render_template("result.html", result=ret)

if __name__ == "__main__":
    print app.url_map
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
