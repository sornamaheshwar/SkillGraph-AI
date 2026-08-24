REQUIRED_SKILLS_QUERY = """
MATCH (u:User {id: $user_id})-[:TARGETS]->(role:JobRole)
MATCH (role)-[req:REQUIRES]->(skill:Skill)

RETURN
    u.name AS user_name,
    role.name AS target_role,
    skill.id AS skill_id,
    req.weight AS weight
"""


USER_SKILLS_QUERY = """
MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

RETURN skill.id AS skill_id
"""