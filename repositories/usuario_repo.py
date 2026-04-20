from supabase import create_client
from config.settings import settings

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_KEY
)

def get_user_profile(user_id):
    response = supabase.table("usuario2") \
        .select("*") \
        .eq("id_usuario", user_id) \
        .execute()

    if response.data:
        return response.data[0]

    return None