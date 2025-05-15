function login() {
  const usuario = document.querySelector("#usuario").value;
  const senha = document.querySelector("#senha").value;

  if (usuario === "admin" && senha === "1234") {
    window.location.href = "JS_13.html";
  } else {
    document.querySelector("#erro").innerText = "Meu nome não é Greta.";
  }
}

function alternarTema() {
  document.body.classList.toggle("escuro");

  const titulo = document.querySelector("#titulo");
  const msg = document.querySelector("#mensagem");

  if (document.body.classList.contains("escuro")) {
    titulo.innerText = "Modo Escuro Ativado!";
    msg.style.color = "#aaa";
  } else {
    titulo.innerText = "Bem-vindo!";
    msg.style.color = "#222";
  }
}
