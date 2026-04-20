from supabase import create_client
from config.settings import settings

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

def login_user(email, senha):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": senha
    })

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