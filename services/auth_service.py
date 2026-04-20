from repositories.usuario_repo import get_user_by_email

def login_user(email, senha):
    user = get_user_by_email(email)

    if not user:
        return None

    if user["senha"] != senha:
        return None

    return user