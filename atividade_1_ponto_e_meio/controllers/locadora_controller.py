from flask import Blueprint, redirect, render_template, request, url_for

from models import ClienteLocadora, Locacao, Veiculo, db

locadora_bp = Blueprint("locadora", __name__, url_prefix="/locadora")


@locadora_bp.route("/")
def index():
    locacoes = Locacao.listar_com_detalhes()
    return render_template("locadora/lista.html", locacoes=locacoes)


@locadora_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    clientes = ClienteLocadora.listar()
    veiculos = Veiculo.listar()

    if request.method == "POST":
        from datetime import datetime
        loc = Locacao(
            cliente_id=int(request.form["cliente_id"]),
            veiculo_id=int(request.form["veiculo_id"]),
            data_inicio=datetime.strptime(request.form["data_inicio"], "%Y-%m-%d").date(),
            data_fim=datetime.strptime(request.form["data_fim"], "%Y-%m-%d").date(),
            valor_total=float(request.form["valor_total"]),
        )
        db.session.add(loc)
        db.session.commit()
        return redirect(url_for("locadora.index"))

    return render_template("locadora/formulario.html", clientes=clientes, veiculos=veiculos)


@locadora_bp.route("/clientes")
def listar_clientes():
    clientes = ClienteLocadora.listar()
    return render_template("locadora/clientes.html", clientes=clientes)


@locadora_bp.route("/clientes/cadastrar", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        cliente = ClienteLocadora(
            nome=request.form["nome"],
            cpf=request.form["cpf"],
            cnh=request.form["cnh"],
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("locadora.listar_clientes"))
    return render_template("locadora/formulario_cliente.html")


@locadora_bp.route("/veiculos")
def listar_veiculos():
    veiculos = Veiculo.listar()
    return render_template("locadora/veiculos.html", veiculos=veiculos)


@locadora_bp.route("/veiculos/cadastrar", methods=["GET", "POST"])
def cadastrar_veiculo():
    if request.method == "POST":
        veiculo = Veiculo(
            placa=request.form["placa"],
            modelo=request.form["modelo"],
            diaria=float(request.form["diaria"]),
        )
        db.session.add(veiculo)
        db.session.commit()
        return redirect(url_for("locadora.listar_veiculos"))
    return render_template("locadora/formulario_veiculo.html")
