from supabase import create_client
from config.settings import settings
from repositories.usuario_repo import get_user_profile

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

def login_user(email, senha):
    try:response = supabase.auth.sign_up({
        "email": email,
        "password": senha
    })
    except Exception as e:
        print(e)

    if response.user:
        return response.user
    
    return None


def register_user(email, senha, nick):
    # 1. cria no auth
    response = supabase.auth.sign_up({
        "email": email,
        "password": senha
    })

    if not response.user:
        return None

    user_id = response.user.id

    # 2. cria perfil
    supabase.table("usuario2").insert({
        "id_usuario": user_id,
        "nick_usuario": nick
    }).execute()

    return response.user

def get_user_full(user):
    profile = get_user_profile(user.id)

    return {
        "id": user.id,
        "email": user.email,
        "nick": profile["nick_usuario"] if profile else "Usuário"
    }