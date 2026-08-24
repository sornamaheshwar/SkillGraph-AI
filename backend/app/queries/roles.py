GET_ALL_ROLES = """
MATCH (role:JobRole)

RETURN
    role.id AS id,
    role.name AS name,
    role.description AS description

ORDER BY role.name
"""