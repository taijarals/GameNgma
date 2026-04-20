def get_user_profile(user_id):
    response = supabase.table("usuario2") \
        .select("*") \
        .eq("id_usuario", user_id) \
        .execute()

    if response.data:
        return response.data[0]
    
    return None