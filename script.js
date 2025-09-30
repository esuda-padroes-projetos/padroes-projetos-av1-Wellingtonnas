// --- Somente LocalStorage (ignora backend) ---

const formLivro = document.getElementById("formLivro");
const bookList = document.getElementById("book-list");

function carregarLocal() {
  const raw = localStorage.getItem('bookshelf_books');
  return raw ? JSON.parse(raw) : [];
}

function salvarLocal(livros) {
  localStorage.setItem('bookshelf_books', JSON.stringify(livros));
}

function renderizarLista(livros) {
  if (!bookList) return;
  bookList.innerHTML = '';
  livros.forEach((l, idx) => {
    bookList.insertAdjacentHTML('beforeend', `
      <tr>
        <td>${l.titulo}</td>
        <td>${l.autor}</td>
        <td>${l.ano}</td>
      </tr>
    `);
  });
}

function adicionarLivro(livro) {
  const livros = carregarLocal();
  livros.push(livro);
  salvarLocal(livros);
  renderizarLista(livros);
}

// Se for a página de cadastro
if (formLivro) {
  formLivro.addEventListener("submit", (e) => {
    e.preventDefault();
    const titulo = document.getElementById("titulo").value.trim();
    const autor = document.getElementById("autor").value.trim();
    const ano = document.getElementById("ano").value.trim();

    const novo = { titulo, autor, ano };
    adicionarLivro(novo);
    formLivro.reset();
  });

  // carrega livros já existentes ao abrir
  renderizarLista(carregarLocal());
}

// Se for a página de listagem
if (bookList && !formLivro) 
  renderiza
