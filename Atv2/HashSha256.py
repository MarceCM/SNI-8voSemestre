import hashlib


sha256_hash = hashlib.sha256()
sha256_hash.update("Em 1999 iniciaram-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.".encode('utf-8'))

print(sha256_hash.hexdigest())