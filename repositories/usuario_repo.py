from repositories.usuario_repo import get_user_profile

def get_user_full(user):
    profile = get_user_profile(user.id)

    return {
        "id": user.id,
        "email": user.email,
        "nick": profile["nick_usuario"] if profile else "Usuário"
    }