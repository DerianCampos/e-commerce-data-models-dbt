with source as (
    select * from {{ source('raw', 'bands') }}
),

renamed as (
    select
        id as band_id,
        name as band_name,
        country,
        genre,
        created_at,
        updated_at
    from source
)

select * from renamed
