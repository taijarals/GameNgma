from supabase import create_client
from config.settings import settings
from repositories.usuario_repo import get_user_profile

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

# LOGIN
def login_user(email, senha):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": senha
        })
    except Exception as e:
        print("Erro no login:", e)
        return None

    if response.user:
        return response.user

    return None


# CADASTRO
def register_user(email, senha, nick):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": senha
        })
    except Exception as e:
        print("Erro no cadastro:", e)
        return None

    if not response.user:
        return None

    user_id = response.user.id

    try:
        supabase.table("usuario2").insert({
            "id_usuario": user_id,
            "nick_usuario": nick
        }).execute()
    except Exception as e:
        print("Erro ao criar perfil:", e)

    return response.user


# USER COMPLETO
def get_user_full(user):
    profile = get_user_profile(user.id)

    return {
        "id": user.id,
        "email": user.email,
        "nick": profile["nick_usuario"] if profile else "Usuário"
    }