async function carregarAnimais(){
    // axios.get("http://localhost:8000/animais")
    // .then(response => console.log(response.data))

    const response = await axios.get("http://localhost:8000/animais")
    // precisa ser async para usar await

    const animais = response.data

    const lista = document.getElementById('lista_animais') //transformando o <ul> em uma variável, pegando pelo id
    
    lista.innerHTML = '' //limpa as li da ul, antes de gerar de novo, para caso tenha auteração, não duplicar a lista

    animais.forEach(animal => {

        const item = document.createElement('li')
        const linha = `${animal.nome} - idade: ${animal.idade} - cor: ${animal.cor}`

        item.innerText = linha

        lista.appendChild(item)    
    });    
}

function manipularFormulario(){
    const form_animal = document.getElementById('form_animal') //criação de um obj para o form (pelo id dele)
    const input_nome = document.getElementById('nome') //criação de um obj para o dado que estiver dentro do input_nome (pelo id dele)

    form_animal.onsubmit = async (event)=>{ //função que vai rodar "onsubmit" do input do form
        event.preventDefault() 
        const nome_animal = input_nome.value //obj que vai receber o valor do obj input criado acima

        axios.post("http://localhost:8000/animais",{ //enviando um obj js para o back utililzando o método post
            nome: nome_animal, //os parâmetro no estilo json que o back precisa consumir
            idade: 1,                //obs: por ser um obj, as chaves não ficam dentro de aspas q nem num json ou um dicionário
            sexo: "m",
            cor: "amarela"
        })

        carregarAnimais() //recarregando a lista de animais na ul

        alert(`${nome_animal} cadastrado`) //mensagem para o usuário
    }
}

async function obterAnimal() {
    const form = document.getElementById('obter_animal_get')
    const lista_animais = await axios.get("http://localhost:8000/animais")
    const animais = lista_animais.data
    
    form.onsubmit = (event)=>{
        event.preventDefault()

        const input_id_animal = document.getElementById('id_animal')
        const id_animal = input_id_animal.value
        
        animais.forEach(animal => {
            if(animal.id == id_animal){
                
                const texto = `
                id: ${animal.id},
                nome: ${animal.nome},
                idade: ${animal.idade},
                sexo: ${animal.sexo},
                cor: ${animal.cor}`
                
                const item = document.createElement('p')
                item.innerText = texto
                document.body.appendChild(item)
            }
        });

    }
}

async function deletarAnimal() {
    const form = document.getElementById("deletar_animal")

    form.onsubmit = async (event) =>{
        event.preventDefault()
        const input_id_animal = document.getElementById("id_animal_delet")
        const id_animal = input_id_animal.value

        try{
            await axios.delete(`http://localhost:8000/animais/${id_animal}`)
            alert("animal deletado com sucesso")
        }
        catch{
            console.log("Não foi possível deletar o animal")
        }
    }

}

function app(){
    console.log("App iniciada")
    carregarAnimais()
    manipularFormulario()
    obterAnimal()
    deletarAnimal()
}

app()