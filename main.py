from fastapi import FastAPI, HTTPException

app = FastAPI(title="API sem Injeção de Dependência")

class BancoDeDadosFalso:
    def __init__(self):
        self.conectado = False

    def conectar(self):
        print("🔌 Abrindo conexão com o banco de dados...")
        self.conectado = True

    def fechar(self):
        print("❌ Fechando conexão com o banco de dados...")
        self.conectado = False

    def buscar_usuario(self, user_id: int):
        if not self.conectado:
            raise Exception("Banco não conectado!")
        if user_id == 1:
            return {"id": 1, "nome": "Sidney"}
        return None

@app.get("/usuarios/{user_id}")
def obter_usuario(user_id: int):
    db = BancoDeDadosFalso()
    db.conectar()
    
    try:
        usuario = db.buscar_usuario(user_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        db.fechar()
        return usuario
    except Exception as e:
        raise e
    