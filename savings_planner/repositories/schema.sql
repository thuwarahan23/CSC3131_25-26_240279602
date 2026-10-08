users(id, email, password_hash)

goals(
    id, user_id, name,
    target_amount_pence,    -- store money as integers
    deadline DATE,
    monthly_target_pence,   -- nullable, computed or user-set
    status,                 -- active | completed | paused | abandoned
    created_at
)

contributions(
    id, goal_id, amount_pence, contributed_on DATE, note
)