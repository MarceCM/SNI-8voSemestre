import hashlib


md5_hash = hashlib.md5()
md5_hash.update("Em 1999 iniciaram-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.".encode('utf-8'))

print(md5_hash.hexdigest())