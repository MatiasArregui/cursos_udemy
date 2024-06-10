palabra = "montaña oz"
#indices   0123456789
#palabra[inicio:fin:paso]
# print(palabra[:7:-1])
#Quitar el @ del mail
mail = "marregui-99@gmail.com"
mail_new = mail.rstrip("@aqzwsxedcrfvtgbyhnujmikolpñ.")
posicion_arroba = mail.find("@")
# mail_new_slice = mail[0:posicion_arroba]
mail_new_slice = mail[0:mail.find("@")]
# print(mail_new)
# print(mail_new_slice)
# print(mail[:mail.index("@")])
dominio = mail[mail.index("@")+1:]
# print(dominio)
print(f"El usuario es: {mail_new_slice} y el dominio es: {dominio}")