with users as (
    select * from {{ ref('stg_users') }}
),

final as (
    select
        user_id,
        email,
        first_name || ' ' || last_name as full_name,
        role,
        is_active,
        created_at,
        updated_at
    from users
)

select * from final
