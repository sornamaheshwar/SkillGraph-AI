import sys
from pathlib import Path

# Add the backend directory to Python's module search path
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BACKEND_DIR))

from app.core.database import db


# ============================================================
# SEED DATA
# ============================================================

SKILLS = [
    # Programming & Fundamentals
    {
        "id": "python",
        "name": "Python",
        "category": "Programming",
    },
    {
        "id": "javascript",
        "name": "JavaScript",
        "category": "Programming",
    },
    {
        "id": "sql",
        "name": "SQL",
        "category": "Data",
    },
    {
        "id": "git",
        "name": "Git",
        "category": "Fundamentals",
    },
    {
        "id": "dsa",
        "name": "Data Structures & Algorithms",
        "category": "Fundamentals",
    },
    {
        "id": "oop",
        "name": "Object-Oriented Programming",
        "category": "Programming",
    },

    # Backend
    {
        "id": "rest-apis",
        "name": "REST APIs",
        "category": "Backend",
    },
    {
        "id": "fastapi",
        "name": "FastAPI",
        "category": "Backend",
    },
    {
        "id": "database-design",
        "name": "Database Design",
        "category": "Backend",
    },
    {
        "id": "authentication",
        "name": "Authentication",
        "category": "Backend",
    },
    {
        "id": "system-design",
        "name": "System Design",
        "category": "Backend",
    },
    {
        "id": "nodejs",
        "name": "Node.js",
        "category": "Backend",
    },

    # AI / ML
    {
        "id": "machine-learning",
        "name": "Machine Learning",
        "category": "AI/ML",
    },
    {
        "id": "deep-learning",
        "name": "Deep Learning",
        "category": "AI/ML",
    },
    {
        "id": "nlp",
        "name": "Natural Language Processing",
        "category": "AI/ML",
    },
    {
        "id": "llms",
        "name": "Large Language Models",
        "category": "AI/ML",
    },
    {
        "id": "embeddings",
        "name": "Embeddings",
        "category": "AI/ML",
    },
    {
        "id": "vector-databases",
        "name": "Vector Databases",
        "category": "AI/ML",
    },
    {
        "id": "rag",
        "name": "Retrieval-Augmented Generation",
        "category": "AI/ML",
    },
    {
        "id": "model-deployment",
        "name": "Model Deployment",
        "category": "AI/ML",
    },

    # Data
    {
        "id": "data-analysis",
        "name": "Data Analysis",
        "category": "Data",
    },
    {
        "id": "statistics",
        "name": "Statistics",
        "category": "Data",
    },
    {
        "id": "data-visualization",
        "name": "Data Visualization",
        "category": "Data",
    },
    {
        "id": "pandas",
        "name": "Pandas",
        "category": "Data",
    },

    # Cloud & DevOps
    {
        "id": "docker",
        "name": "Docker",
        "category": "Cloud & DevOps",
    },
    {
        "id": "cloud-deployment",
        "name": "Cloud Deployment",
        "category": "Cloud & DevOps",
    },
    {
        "id": "ci-cd",
        "name": "CI/CD",
        "category": "Cloud & DevOps",
    },

    # Frontend
    {
        "id": "html-css",
        "name": "HTML & CSS",
        "category": "Frontend",
    },
    {
        "id": "react",
        "name": "React",
        "category": "Frontend",
    },
    {
        "id": "state-management",
        "name": "State Management",
        "category": "Frontend",
    },
]


JOB_ROLES = [
    {
        "id": "ai-engineer",
        "name": "AI Engineer",
        "description": "Builds and deploys AI-powered applications and intelligent systems.",
    },
    {
        "id": "ml-engineer",
        "name": "Machine Learning Engineer",
        "description": "Builds, trains, deploys, and maintains machine learning systems.",
    },
    {
        "id": "backend-engineer",
        "name": "Backend Engineer",
        "description": "Designs and builds scalable server-side applications and APIs.",
    },
    {
        "id": "data-scientist",
        "name": "Data Scientist",
        "description": "Analyzes data and builds models to generate insights and predictions.",
    },
    {
        "id": "fullstack-developer",
        "name": "Full Stack Developer",
        "description": "Builds complete web applications across frontend and backend systems.",
    },
]


TECHNOLOGIES = [
    {
        "id": "fastapi-tech",
        "name": "FastAPI",
        "type": "Framework",
    },
    {
        "id": "react-tech",
        "name": "React",
        "type": "Frontend Framework",
    },
    {
        "id": "nodejs-tech",
        "name": "Node.js",
        "type": "Runtime",
    },
    {
        "id": "postgresql",
        "name": "PostgreSQL",
        "type": "Database",
    },
    {
        "id": "docker-tech",
        "name": "Docker",
        "type": "Container Platform",
    },
    {
        "id": "aws",
        "name": "AWS",
        "type": "Cloud Platform",
    },
    {
        "id": "github-actions",
        "name": "GitHub Actions",
        "type": "CI/CD Platform",
    },
    {
        "id": "scikit-learn",
        "name": "Scikit-learn",
        "type": "Machine Learning Library",
    },
    {
        "id": "pytorch",
        "name": "PyTorch",
        "type": "Deep Learning Framework",
    },
    {
        "id": "pandas-tech",
        "name": "Pandas",
        "type": "Data Library",
    },
    {
        "id": "langchain",
        "name": "LangChain",
        "type": "AI Framework",
    },
    {
        "id": "chromadb",
        "name": "ChromaDB",
        "type": "Vector Database",
    },
    {
        "id": "faiss",
        "name": "FAISS",
        "type": "Vector Search Library",
    },
    {
        "id": "hugging-face",
        "name": "Hugging Face",
        "type": "AI Platform",
    },
    {
        "id": "neo4j-driver",
        "name": "Neo4j Python Driver",
        "type": "Database Driver",
    },
]


PROJECTS = [
    {
        "id": "rag-document-assistant",
        "name": "RAG Document Assistant",
        "description": "An AI application that answers questions using information retrieved from uploaded documents.",
        "difficulty": "Advanced",
    },
    {
        "id": "ai-resume-analyzer",
        "name": "AI Resume Analyzer",
        "description": "An AI-powered application that analyzes resumes and extracts relevant skills and insights.",
        "difficulty": "Intermediate",
    },
    {
        "id": "image-classification-system",
        "name": "Image Classification System",
        "description": "A deep learning application for classifying images into predefined categories.",
        "difficulty": "Advanced",
    },
    {
        "id": "recommendation-engine",
        "name": "Recommendation Engine",
        "description": "A machine learning system that recommends relevant items based on user behavior and preferences.",
        "difficulty": "Intermediate",
    },
    {
        "id": "fraud-detection-system",
        "name": "Fraud Detection System",
        "description": "A machine learning system for identifying potentially fraudulent transactions.",
        "difficulty": "Advanced",
    },
    {
        "id": "scalable-rest-api",
        "name": "Scalable REST API",
        "description": "A production-style backend API with authentication, database integration, and containerization.",
        "difficulty": "Intermediate",
    },
    {
        "id": "url-shortener-service",
        "name": "URL Shortener Service",
        "description": "A backend service for generating and managing shortened URLs.",
        "difficulty": "Intermediate",
    },
    {
        "id": "ecommerce-backend",
        "name": "E-Commerce Backend",
        "description": "A backend system supporting products, users, authentication, and order management.",
        "difficulty": "Advanced",
    },
    {
        "id": "sales-analytics-dashboard",
        "name": "Sales Analytics Dashboard",
        "description": "A data analytics application for exploring sales performance and business trends.",
        "difficulty": "Intermediate",
    },
    {
        "id": "customer-churn-prediction",
        "name": "Customer Churn Prediction",
        "description": "A machine learning project for predicting customers likely to leave a service.",
        "difficulty": "Intermediate",
    },
    {
        "id": "collaborative-task-manager",
        "name": "Collaborative Task Manager",
        "description": "A full-stack application for managing tasks, users, and team collaboration.",
        "difficulty": "Intermediate",
    },
    {
        "id": "realtime-analytics-platform",
        "name": "Real-Time Analytics Platform",
        "description": "A web platform for displaying and analyzing continuously updated application data.",
        "difficulty": "Advanced",
    },
]


DEMO_USER = {
    "id": "demo-user",
    "name": "Demo User",
}

# ============================================================
# RELATIONSHIP DATA
# ============================================================

PREREQUISITES = [
    # AI / ML path
    {"from": "python", "to": "machine-learning", "strength": "required"},
    {"from": "statistics", "to": "machine-learning", "strength": "required"},
    {"from": "machine-learning", "to": "deep-learning", "strength": "recommended"},
    {"from": "machine-learning", "to": "embeddings", "strength": "recommended"},
    {"from": "deep-learning", "to": "nlp", "strength": "recommended"},
    {"from": "nlp", "to": "llms", "strength": "recommended"},
    {"from": "embeddings", "to": "vector-databases", "strength": "required"},
    {"from": "vector-databases", "to": "rag", "strength": "required"},
    {"from": "llms", "to": "rag", "strength": "required"},

    # Backend path
    {"from": "python", "to": "rest-apis", "strength": "recommended"},
    {"from": "rest-apis", "to": "fastapi", "strength": "required"},
    {"from": "database-design", "to": "system-design", "strength": "recommended"},
    {"from": "fastapi", "to": "authentication", "strength": "recommended"},
    {"from": "fastapi", "to": "system-design", "strength": "helpful"},

    # DevOps path
    {"from": "git", "to": "ci-cd", "strength": "recommended"},
    {"from": "docker", "to": "cloud-deployment", "strength": "recommended"},
    {"from": "ci-cd", "to": "cloud-deployment", "strength": "recommended"},

    # Frontend path
    {"from": "html-css", "to": "javascript", "strength": "required"},
    {"from": "javascript", "to": "react", "strength": "required"},
    {"from": "react", "to": "state-management", "strength": "recommended"},
]


ROLE_REQUIREMENTS = [
    # AI Engineer
    {"role": "ai-engineer", "skill": "python", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "machine-learning", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "llms", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "embeddings", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "vector-databases", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "rag", "importance": "core", "weight": 10},
    {"role": "ai-engineer", "skill": "fastapi", "importance": "important", "weight": 7},
    {"role": "ai-engineer", "skill": "rest-apis", "importance": "important", "weight": 7},
    {"role": "ai-engineer", "skill": "docker", "importance": "important", "weight": 7},
    {"role": "ai-engineer", "skill": "cloud-deployment", "importance": "important", "weight": 7},
    {"role": "ai-engineer", "skill": "git", "importance": "supporting", "weight": 4},
    {"role": "ai-engineer", "skill": "dsa", "importance": "supporting", "weight": 4},

    # Machine Learning Engineer
    {"role": "ml-engineer", "skill": "python", "importance": "core", "weight": 10},
    {"role": "ml-engineer", "skill": "machine-learning", "importance": "core", "weight": 10},
    {"role": "ml-engineer", "skill": "deep-learning", "importance": "core", "weight": 10},
    {"role": "ml-engineer", "skill": "statistics", "importance": "core", "weight": 10},
    {"role": "ml-engineer", "skill": "pandas", "importance": "important", "weight": 7},
    {"role": "ml-engineer", "skill": "model-deployment", "importance": "important", "weight": 7},
    {"role": "ml-engineer", "skill": "docker", "importance": "important", "weight": 7},
    {"role": "ml-engineer", "skill": "cloud-deployment", "importance": "important", "weight": 7},
    {"role": "ml-engineer", "skill": "data-analysis", "importance": "important", "weight": 7},
    {"role": "ml-engineer", "skill": "git", "importance": "supporting", "weight": 4},

    # Backend Engineer
    {"role": "backend-engineer", "skill": "python", "importance": "core", "weight": 10},
    {"role": "backend-engineer", "skill": "rest-apis", "importance": "core", "weight": 10},
    {"role": "backend-engineer", "skill": "fastapi", "importance": "core", "weight": 10},
    {"role": "backend-engineer", "skill": "database-design", "importance": "core", "weight": 10},
    {"role": "backend-engineer", "skill": "sql", "importance": "core", "weight": 10},
    {"role": "backend-engineer", "skill": "authentication", "importance": "important", "weight": 7},
    {"role": "backend-engineer", "skill": "docker", "importance": "important", "weight": 7},
    {"role": "backend-engineer", "skill": "system-design", "importance": "important", "weight": 7},
    {"role": "backend-engineer", "skill": "git", "importance": "supporting", "weight": 4},
    {"role": "backend-engineer", "skill": "dsa", "importance": "supporting", "weight": 4},

    # Data Scientist
    {"role": "data-scientist", "skill": "python", "importance": "core", "weight": 10},
    {"role": "data-scientist", "skill": "statistics", "importance": "core", "weight": 10},
    {"role": "data-scientist", "skill": "machine-learning", "importance": "core", "weight": 10},
    {"role": "data-scientist", "skill": "data-analysis", "importance": "core", "weight": 10},
    {"role": "data-scientist", "skill": "pandas", "importance": "important", "weight": 7},
    {"role": "data-scientist", "skill": "sql", "importance": "important", "weight": 7},
    {"role": "data-scientist", "skill": "data-visualization", "importance": "important", "weight": 7},
    {"role": "data-scientist", "skill": "git", "importance": "supporting", "weight": 4},

    # Full Stack Developer
    {"role": "fullstack-developer", "skill": "html-css", "importance": "core", "weight": 10},
    {"role": "fullstack-developer", "skill": "javascript", "importance": "core", "weight": 10},
    {"role": "fullstack-developer", "skill": "react", "importance": "core", "weight": 10},
    {"role": "fullstack-developer", "skill": "state-management", "importance": "important", "weight": 7},
    {"role": "fullstack-developer", "skill": "rest-apis", "importance": "core", "weight": 10},
    {"role": "fullstack-developer", "skill": "database-design", "importance": "important", "weight": 7},
    {"role": "fullstack-developer", "skill": "authentication", "importance": "important", "weight": 7},
    {"role": "fullstack-developer", "skill": "git", "importance": "supporting", "weight": 4},
    {"role": "fullstack-developer", "skill": "docker", "importance": "supporting", "weight": 4},
]


USER_SKILLS = [
    "python",
    "sql",
    "git",
    "machine-learning",
    "dsa",
    "rest-apis",
    "fastapi",
    "pandas",
]


USER_TARGET_ROLE = "ai-engineer"
PROJECT_SKILLS = [
    # RAG Document Assistant
    {"project": "rag-document-assistant", "skill": "python", "level": "primary"},
    {"project": "rag-document-assistant", "skill": "llms", "level": "primary"},
    {"project": "rag-document-assistant", "skill": "embeddings", "level": "primary"},
    {"project": "rag-document-assistant", "skill": "vector-databases", "level": "primary"},
    {"project": "rag-document-assistant", "skill": "rag", "level": "primary"},
    {"project": "rag-document-assistant", "skill": "fastapi", "level": "secondary"},
    {"project": "rag-document-assistant", "skill": "docker", "level": "secondary"},

    # AI Resume Analyzer
    {"project": "ai-resume-analyzer", "skill": "python", "level": "primary"},
    {"project": "ai-resume-analyzer", "skill": "nlp", "level": "primary"},
    {"project": "ai-resume-analyzer", "skill": "llms", "level": "primary"},
    {"project": "ai-resume-analyzer", "skill": "fastapi", "level": "secondary"},
    {"project": "ai-resume-analyzer", "skill": "rest-apis", "level": "secondary"},

    # Image Classification
    {"project": "image-classification-system", "skill": "python", "level": "primary"},
    {"project": "image-classification-system", "skill": "machine-learning", "level": "primary"},
    {"project": "image-classification-system", "skill": "deep-learning", "level": "primary"},
    {"project": "image-classification-system", "skill": "model-deployment", "level": "secondary"},

    # Recommendation Engine
    {"project": "recommendation-engine", "skill": "python", "level": "primary"},
    {"project": "recommendation-engine", "skill": "machine-learning", "level": "primary"},
    {"project": "recommendation-engine", "skill": "data-analysis", "level": "primary"},
    {"project": "recommendation-engine", "skill": "pandas", "level": "secondary"},
    {"project": "recommendation-engine", "skill": "sql", "level": "secondary"},

    # Fraud Detection
    {"project": "fraud-detection-system", "skill": "python", "level": "primary"},
    {"project": "fraud-detection-system", "skill": "machine-learning", "level": "primary"},
    {"project": "fraud-detection-system", "skill": "statistics", "level": "primary"},
    {"project": "fraud-detection-system", "skill": "data-analysis", "level": "secondary"},
    {"project": "fraud-detection-system", "skill": "sql", "level": "secondary"},

    # Scalable REST API
    {"project": "scalable-rest-api", "skill": "python", "level": "primary"},
    {"project": "scalable-rest-api", "skill": "fastapi", "level": "primary"},
    {"project": "scalable-rest-api", "skill": "rest-apis", "level": "primary"},
    {"project": "scalable-rest-api", "skill": "authentication", "level": "primary"},
    {"project": "scalable-rest-api", "skill": "database-design", "level": "secondary"},
    {"project": "scalable-rest-api", "skill": "docker", "level": "secondary"},

    # URL Shortener
    {"project": "url-shortener-service", "skill": "rest-apis", "level": "primary"},
    {"project": "url-shortener-service", "skill": "database-design", "level": "primary"},
    {"project": "url-shortener-service", "skill": "sql", "level": "primary"},
    {"project": "url-shortener-service", "skill": "system-design", "level": "secondary"},
    {"project": "url-shortener-service", "skill": "docker", "level": "secondary"},

    # E-Commerce Backend
    {"project": "ecommerce-backend", "skill": "fastapi", "level": "primary"},
    {"project": "ecommerce-backend", "skill": "rest-apis", "level": "primary"},
    {"project": "ecommerce-backend", "skill": "authentication", "level": "primary"},
    {"project": "ecommerce-backend", "skill": "database-design", "level": "primary"},
    {"project": "ecommerce-backend", "skill": "sql", "level": "secondary"},

    # Sales Analytics
    {"project": "sales-analytics-dashboard", "skill": "python", "level": "primary"},
    {"project": "sales-analytics-dashboard", "skill": "sql", "level": "primary"},
    {"project": "sales-analytics-dashboard", "skill": "data-analysis", "level": "primary"},
    {"project": "sales-analytics-dashboard", "skill": "pandas", "level": "primary"},
    {"project": "sales-analytics-dashboard", "skill": "data-visualization", "level": "primary"},

    # Customer Churn
    {"project": "customer-churn-prediction", "skill": "python", "level": "primary"},
    {"project": "customer-churn-prediction", "skill": "machine-learning", "level": "primary"},
    {"project": "customer-churn-prediction", "skill": "statistics", "level": "primary"},
    {"project": "customer-churn-prediction", "skill": "pandas", "level": "secondary"},
    {"project": "customer-churn-prediction", "skill": "data-visualization", "level": "secondary"},

    # Task Manager
    {"project": "collaborative-task-manager", "skill": "react", "level": "primary"},
    {"project": "collaborative-task-manager", "skill": "javascript", "level": "primary"},
    {"project": "collaborative-task-manager", "skill": "rest-apis", "level": "primary"},
    {"project": "collaborative-task-manager", "skill": "authentication", "level": "secondary"},
    {"project": "collaborative-task-manager", "skill": "database-design", "level": "secondary"},

    # Real-Time Analytics
    {"project": "realtime-analytics-platform", "skill": "react", "level": "primary"},
    {"project": "realtime-analytics-platform", "skill": "rest-apis", "level": "primary"},
    {"project": "realtime-analytics-platform", "skill": "fastapi", "level": "primary"},
    {"project": "realtime-analytics-platform", "skill": "database-design", "level": "secondary"},
    {"project": "realtime-analytics-platform", "skill": "docker", "level": "secondary"},
    {"project": "realtime-analytics-platform", "skill": "cloud-deployment", "level": "secondary"},
]


PROJECT_ROLES = [
    {"project": "rag-document-assistant", "role": "ai-engineer"},
    {"project": "rag-document-assistant", "role": "ml-engineer"},

    {"project": "ai-resume-analyzer", "role": "ai-engineer"},
    {"project": "ai-resume-analyzer", "role": "backend-engineer"},

    {"project": "image-classification-system", "role": "ml-engineer"},
    {"project": "image-classification-system", "role": "ai-engineer"},

    {"project": "recommendation-engine", "role": "ml-engineer"},
    {"project": "recommendation-engine", "role": "data-scientist"},

    {"project": "fraud-detection-system", "role": "data-scientist"},
    {"project": "fraud-detection-system", "role": "ml-engineer"},

    {"project": "scalable-rest-api", "role": "backend-engineer"},
    {"project": "scalable-rest-api", "role": "ai-engineer"},

    {"project": "url-shortener-service", "role": "backend-engineer"},

    {"project": "ecommerce-backend", "role": "backend-engineer"},
    {"project": "ecommerce-backend", "role": "fullstack-developer"},

    {"project": "sales-analytics-dashboard", "role": "data-scientist"},

    {"project": "customer-churn-prediction", "role": "data-scientist"},
    {"project": "customer-churn-prediction", "role": "ml-engineer"},

    {"project": "collaborative-task-manager", "role": "fullstack-developer"},

    {"project": "realtime-analytics-platform", "role": "fullstack-developer"},
    {"project": "realtime-analytics-platform", "role": "backend-engineer"},
]


SKILL_TECHNOLOGIES = [
    {"skill": "fastapi", "technology": "fastapi-tech"},
    {"skill": "react", "technology": "react-tech"},
    {"skill": "nodejs", "technology": "nodejs-tech"},
    {"skill": "sql", "technology": "postgresql"},
    {"skill": "docker", "technology": "docker-tech"},
    {"skill": "cloud-deployment", "technology": "aws"},
    {"skill": "ci-cd", "technology": "github-actions"},
    {"skill": "machine-learning", "technology": "scikit-learn"},
    {"skill": "deep-learning", "technology": "pytorch"},
    {"skill": "data-analysis", "technology": "pandas-tech"},
    {"skill": "llms", "technology": "langchain"},
    {"skill": "rag", "technology": "langchain"},
    {"skill": "vector-databases", "technology": "chromadb"},
    {"skill": "vector-databases", "technology": "faiss"},
    {"skill": "nlp", "technology": "hugging-face"},
]
# ============================================================
# NODE CREATION FUNCTIONS
# ============================================================

def seed_skills(session):
    query = """
    UNWIND $skills AS skill
    MERGE (s:Skill {id: skill.id})
    SET s.name = skill.name,
        s.category = skill.category
    """

    session.run(query, skills=SKILLS)


def seed_job_roles(session):
    query = """
    UNWIND $roles AS role
    MERGE (r:JobRole {id: role.id})
    SET r.name = role.name,
        r.description = role.description
    """

    session.run(query, roles=JOB_ROLES)


def seed_technologies(session):
    query = """
    UNWIND $technologies AS technology
    MERGE (t:Technology {id: technology.id})
    SET t.name = technology.name,
        t.type = technology.type
    """

    session.run(query, technologies=TECHNOLOGIES)


def seed_projects(session):
    query = """
    UNWIND $projects AS project
    MERGE (p:Project {id: project.id})
    SET p.name = project.name,
        p.description = project.description,
        p.difficulty = project.difficulty
    """

    session.run(query, projects=PROJECTS)


def seed_demo_user(session):
    query = """
    MERGE (u:User {id: $user.id})
    SET u.name = $user.name
    """

    session.run(query, user=DEMO_USER)
# ============================================================
# RELATIONSHIP CREATION FUNCTIONS
# ============================================================

def seed_prerequisites(session):
    query = """
    UNWIND $relationships AS rel

    MATCH (from:Skill {id: rel.from})
    MATCH (to:Skill {id: rel.to})

    MERGE (from)-[r:PREREQUISITE_OF]->(to)

    SET r.strength = rel.strength
    """

    session.run(query, relationships=PREREQUISITES)


def seed_role_requirements(session):
    query = """
    UNWIND $requirements AS req

    MATCH (role:JobRole {id: req.role})
    MATCH (skill:Skill {id: req.skill})

    MERGE (role)-[r:REQUIRES]->(skill)

    SET r.importance = req.importance,
        r.weight = req.weight
    """

    session.run(query, requirements=ROLE_REQUIREMENTS)


def seed_user_skills(session):
    query = """
    MATCH (user:User {id: $user_id})

    UNWIND $skill_ids AS skill_id

    MATCH (skill:Skill {id: skill_id})

    MERGE (user)-[:HAS_SKILL]->(skill)
    """

    session.run(
        query,
        user_id=DEMO_USER["id"],
        skill_ids=USER_SKILLS
    )


def seed_user_target_role(session):
    query = """
    MATCH (user:User {id: $user_id})
    MATCH (role:JobRole {id: $role_id})

    MERGE (user)-[:TARGETS]->(role)
    """

    session.run(
        query,
        user_id=DEMO_USER["id"],
        role_id=USER_TARGET_ROLE
    )

def seed_project_skills(session):
    query = """
    UNWIND $relationships AS rel

    MATCH (project:Project {id: rel.project})
    MATCH (skill:Skill {id: rel.skill})

    MERGE (project)-[r:DEMONSTRATES]->(skill)

    SET r.level = rel.level
    """

    session.run(query, relationships=PROJECT_SKILLS)


def seed_project_roles(session):
    query = """
    UNWIND $relationships AS rel

    MATCH (project:Project {id: rel.project})
    MATCH (role:JobRole {id: rel.role})

    MERGE (project)-[:RELEVANT_TO]->(role)
    """

    session.run(query, relationships=PROJECT_ROLES)


def seed_skill_technologies(session):
    query = """
    UNWIND $relationships AS rel

    MATCH (skill:Skill {id: rel.skill})
    MATCH (technology:Technology {id: rel.technology})

    MERGE (skill)-[:USES]->(technology)
    """

    session.run(query, relationships=SKILL_TECHNOLOGIES)
# ============================================================
# MAIN SEED FUNCTION
# ============================================================

# ============================================================
# MAIN SEED FUNCTION
# ============================================================

def seed_database():
    try:
        print("Connecting to CognoDB...")

        db.verify_connection()

        with db.get_session() as session:

            # Nodes
            print("Seeding skills...")
            seed_skills(session)

            print("Seeding job roles...")
            seed_job_roles(session)

            print("Seeding technologies...")
            seed_technologies(session)

            print("Seeding projects...")
            seed_projects(session)

            print("Seeding demo user...")
            seed_demo_user(session)

            # Relationships
            print("Seeding prerequisite relationships...")
            seed_prerequisites(session)

            print("Seeding role requirements...")
            seed_role_requirements(session)

            print("Seeding demo user skills...")
            seed_user_skills(session)

            print("Seeding demo user target role...")
            seed_user_target_role(session)

            print("Seeding project skill relationships...")
            seed_project_skills(session)

            print("Seeding project role relationships...")
            seed_project_roles(session)

            print("Seeding skill technology relationships...")
            seed_skill_technologies(session)

        print("\nComplete SkillGraph AI graph seeded successfully!")

    except Exception as e:
        print(f"\nSeeding failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()