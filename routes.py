from flask import Blueprint, request, jsonify

routes = Blueprint("routes", __name__)

# Lista de livros (simulação de banco de dados em memória)
livros = []
contador_id = 1

# GET - Listar livros
@routes.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

# POST - Adicionar livro
@routes.route("/livros", methods=["POST"])
def adicionar_livro():
    global contador_id
    data = request.get_json()
    novo_livro = {
        "id": contador_id,
        "titulo": data.get("titulo"),
        "autor": data.get("autor"),
        "ano": data.get("ano")
    }
    livros.append(novo_livro)
    contador_id += 1
    return jsonify(novo_livro), 201

# PUT - Atualizar livro
@routes.route("/livros/<int:livro_id>", methods=["PUT"])
def atualizar_livro(livro_id):
    data = request.get_json()
    for livro in livros:
        if livro["id"] == livro_id:
            livro["titulo"] = data.get("titulo", livro["titulo"])
            livro["autor"] = data.get("autor", livro["autor"])
            livro["ano"] = data.get("ano", livro["ano"])
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

# DELETE - Excluir livro
@routes.route("/livros/<int:livro_id>", methods=["DELETE"])
def excluir_livro(livro_id):
    global livros
    livros = [livro for livro in livros if livro["id"] != livro_id]
    return jsonify({"mensagem": "Livro excluído com sucesso"})
