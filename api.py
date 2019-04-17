# -*- coding: utf-8 -*-


from flask import Flask
from flask import request, jsonify
from methods import *
from sympy import *



app = Flask(__name__)
x = Symbol('x')

@app.route("/newtons/<string:function>/<string:x0>/<int:n>/<string:epsilon>", methods=["GET"])
def newtons(function, x0, n,epsilon):
    return jsonify({"result" : newtons_method(sympify(function), float(x0), n, float(epsilon))}) 

@app.route("/secant/<string:function>/<string:a>/<string:b>/<int:n>", methods=["GET"])
def secant(function, a, b, n):
    return jsonify({"result" : float(secant_method(sympify(function), float(a), float(b), n))})

@app.route("/bisection/<string:function>/<string:a>/<string:b>/<int:n>", methods=["GET"])
def bisection(function, a, b, n):
    return jsonify({"result" : float(bisection_method(sympify(function), float(a), float(b), n))})

if __name__ == "__main__":
    app.run()