"""Autenticação simples para uma catraca."""


USUARIOS = {
	"joao": "1234",
	"maria": "5678",
}
MAX_TENTATIVAS = 3


def autenticar():
	for tentativa in range(1, MAX_TENTATIVAS + 1):
		usuario = input("Usuário: ").strip()
		senha = input("Senha: ").strip()

		if USUARIOS.get(usuario) == senha:
			print("Acesso autorizado. Catraca liberada!")
			return True

		restantes = MAX_TENTATIVAS - tentativa
		if restantes:
			print(f"Acesso negado. Tentativas restantes: {restantes}")

	print("Acesso bloqueado.")
	return False


if __name__ == "__main__":
	autenticar()
