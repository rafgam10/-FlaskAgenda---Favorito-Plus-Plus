from flask import Flask, render_template, redirect, url_for, request, flash
from database.util import *

app = Flask(__name__)
app.secret_key = "favorito++"

@app.route("/", methods=["GET"])
def index():
    contatos = Lista_contatos()
    return render_template("index.html", contatos=contatos)

@app.route("/novo", methods=["GET","POST"])
def novo_contato():
    if request.method == "POST":
        # Captura os dados do formulário
        nome_contato = request.form.get('nomeCont')
        telefone_contato = request.form.get('telefoneCont')
        email_contato = request.form.get('emailCont')
        favorito_contato = 1 if request.form.get('checkCont') else 0

        # Validação básica (nome e telefone obrigatórios)
        if not nome_contato or not telefone_contato:
            flash("Erro: Nome e telefone são obrigatórios.")
            return redirect(url_for('novo_contato'))

        try:
            Add_contato(nome_contato, telefone_contato, email_contato, favorito_contato)
            flash("Contato salvo com sucesso na agenda.")
            return redirect(url_for('index'))
        except Exception as erro:
            flash(f"Erro ao salvar: {erro}")
            return redirect(url_for('novo_contato'))
    
    return render_template("contato_form.html")

@app.route("/editar/<int:id>", methods=["GET", "PUT"])
def editar_contato(id):
    pass


@app.route("/deletar/<int:id>", methods=["GET", "DELETE"])
def deletar_contato(id):
    Deletar_contato(id)
    flash("Contato Deletado com Sucesso!")
    return redirect(url_for("index"))

@app.route("/favorito", methods=["GET"])
def favoritos():
    
    contatos_favoritos = Lista_Favoritos()
    return render_template('favoritos.html', contatos=contatos_favoritos)


if __name__ == "__main__":
    app.run(debug=True)