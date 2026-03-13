async function carregarAnimais(){
    // axios.get("http://localhost:8000/animais")
    // .then(response => console.log(response.data))

    const response = await axios.get("http://localhost:8000/animais")
    // precisa ser async para usar await

    const animais = response.data

    const lista = document.getElementById('lista_animais') //transformando o <ul> em uma variável, pegando pelo id
    
    animais.forEach(animal => {

        const item = document.createElement('li')
        item.innerText = animal.nome

        lista.appendChild(item)    
    });    

    

}

function app(){
    console.log("App iniciada")
    carregarAnimais()
}

app()