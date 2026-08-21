with source as (
    select * from {{ source('raw', 'users') }}
),

renamed as (
    select
        id as user_id,
        email,
        first_name,
        last_name,
        role,
        is_active,
        created_at,
        updated_at
    from source
)

select * from renamed
