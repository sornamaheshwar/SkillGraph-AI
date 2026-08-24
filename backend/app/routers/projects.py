from fastapi import APIRouter, HTTPException

from backend.app.core.database import db
from backend.app.schemas.project import (
    ProjectRecommendation,
    ProjectDetails,
    ImplementationStep,
)


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)


# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

@router.get(
    "/recommendations",
    response_model=list[ProjectRecommendation]
)
def get_project_recommendations():
    projects_query = """
    MATCH (u:User {id: $user_id})-[:TARGETS]->(role:JobRole)

    MATCH (role)-[:REQUIRES]->(required_skill:Skill)

    MATCH (project:Project)-[:RELEVANT_TO]->(role)

    MATCH (project)-[:DEMONSTRATES]->(skill:Skill)

    RETURN
        project.id AS id,
        project.name AS name,
        project.description AS description,
        project.difficulty AS difficulty,
        COLLECT(DISTINCT required_skill.id) AS required_skill_ids,
        COLLECT(DISTINCT skill.id) AS project_skill_ids,
        COLLECT(DISTINCT skill.name) AS project_skill_names
    """

    user_skills_query = """
    MATCH (u:User {id: $user_id})-[:HAS_SKILL]->(skill:Skill)

    RETURN COLLECT(skill.id) AS user_skill_ids
    """

    try:
        with db.get_session() as session:

            # Get projects relevant to the user's target role
            result = session.run(
                projects_query,
                user_id="demo-user"
            )

            projects = [
                dict(record)
                for record in result
            ]

            # Get skills already possessed by the user
            user_result = session.run(
                user_skills_query,
                user_id="demo-user"
            )

            user_record = user_result.single()

            if user_record is None:
                raise HTTPException(
                    status_code=404,
                    detail="User not found."
                )

            user_skill_ids = set(
                user_record["user_skill_ids"]
            )

        recommendations = []

        for project in projects:

            required_skill_ids = set(
                project["required_skill_ids"]
            )

            project_skills = dict(
                zip(
                    project["project_skill_ids"],
                    project["project_skill_names"]
                )
            )

            # Find skills that are:
            # 1. Required for the target role
            # 2. Missing from the user's profile
            # 3. Demonstrated by this project
            relevant_missing_skill_ids = (
                required_skill_ids
                & set(project_skills.keys())
            ) - user_skill_ids

            missing_skills_covered = sorted(
                project_skills[skill_id]
                for skill_id in relevant_missing_skill_ids
            )

            relevance_score = len(
                missing_skills_covered
            )

            if relevance_score > 0:
                recommendations.append(
                    ProjectRecommendation(
                        id=project["id"],
                        name=project["name"],
                        description=project["description"],
                        difficulty=project["difficulty"],
                        missing_skills_covered=missing_skills_covered,
                        relevance_score=relevance_score,
                    )
                )

        # Highest relevance first.
        # Project name is used as a stable secondary sort.
        recommendations.sort(
            key=lambda project: (
                -project.relevance_score,
                project.name
            )
        )

        return recommendations[:5]

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )


# ============================================================
# PROJECT DETAILS
# ============================================================

@router.get(
    "/{project_id}",
    response_model=ProjectDetails
)
def get_project_details(project_id: str):

    project_query = """
    MATCH (project:Project {id: $project_id})

    OPTIONAL MATCH
        (project)-[:DEMONSTRATES]->(skill:Skill)

    RETURN
        project.id AS id,
        project.name AS name,
        project.description AS description,
        project.difficulty AS difficulty,
        COLLECT(DISTINCT skill.name) AS skills
    """

    try:
        with db.get_session() as session:

            result = session.run(
                project_query,
                project_id=project_id
            )

            project = result.single()

            if project is None:
                raise HTTPException(
                    status_code=404,
                    detail="Project not found."
                )

            project_data = dict(project)

        # ----------------------------------------------------
        # PROJECT-SPECIFIC IMPLEMENTATION DATA
        #
        # This is intentionally kept here for now because
        # your Neo4j graph currently stores the project,
        # skills, role relationships, and metadata.
        #
        # Later, these can be moved into Neo4j nodes.
        # ----------------------------------------------------

        project_plans = {

            "rag-document-assistant": {
                "tech_stack": [
                    "Python",
                    "FastAPI",
                    "LangChain",
                    "Vector Database",
                    "OpenAI API",
                    "React"
                ],

                "key_features": [
                    "Upload PDF and text documents",
                    "Extract and preprocess document content",
                    "Generate embeddings for document chunks",
                    "Store embeddings in a vector database",
                    "Semantic search for relevant context",
                    "Answer user questions using an LLM",
                    "Display sources used for responses"
                ],

                "architecture": [
                    "User uploads document",
                    "Document text extraction",
                    "Text chunking",
                    "Embedding generation",
                    "Vector database storage",
                    "User submits question",
                    "Relevant context retrieval",
                    "LLM generates final response"
                ],

                "implementation_steps": [
                    {
                        "step": 1,
                        "title": "Set Up the Project",
                        "description": (
                            "Create the FastAPI backend and React frontend. "
                            "Configure the environment and project structure."
                        )
                    },
                    {
                        "step": 2,
                        "title": "Build Document Ingestion",
                        "description": (
                            "Allow users to upload documents and extract "
                            "their text content for processing."
                        )
                    },
                    {
                        "step": 3,
                        "title": "Chunk and Process Documents",
                        "description": (
                            "Split large documents into smaller chunks that "
                            "can be efficiently converted into embeddings."
                        )
                    },
                    {
                        "step": 4,
                        "title": "Generate Embeddings",
                        "description": (
                            "Convert document chunks into vector embeddings "
                            "using an embedding model."
                        )
                    },
                    {
                        "step": 5,
                        "title": "Create the Vector Store",
                        "description": (
                            "Store embeddings in a vector database and "
                            "implement similarity search."
                        )
                    },
                    {
                        "step": 6,
                        "title": "Build the RAG Pipeline",
                        "description": (
                            "Retrieve relevant document chunks and provide "
                            "them as context to the language model."
                        )
                    },
                    {
                        "step": 7,
                        "title": "Build the User Interface",
                        "description": (
                            "Create a clean interface for document upload "
                            "and conversational question answering."
                        )
                    },
                    {
                        "step": 8,
                        "title": "Test and Deploy",
                        "description": (
                            "Test the complete RAG workflow, handle errors, "
                            "and deploy the application."
                        )
                    }
                ]
            },

            "ai-resume-analyzer": {
                "tech_stack": [
                    "Python",
                    "FastAPI",
                    "Natural Language Processing",
                    "Large Language Models",
                    "React"
                ],

                "key_features": [
                    "Upload and parse resumes",
                    "Extract candidate skills",
                    "Identify experience and education",
                    "Compare resumes with job descriptions",
                    "Calculate skill match scores",
                    "Generate improvement suggestions"
                ],

                "architecture": [
                    "User uploads resume",
                    "Resume text extraction",
                    "Text preprocessing",
                    "Skill and entity extraction",
                    "Job description analysis",
                    "LLM or NLP-based comparison",
                    "Match score generation",
                    "Insights displayed to the user"
                ],

                "implementation_steps": [
                    {
                        "step": 1,
                        "title": "Set Up the Application",
                        "description": (
                            "Create the backend API and frontend interface "
                            "for uploading and analyzing resumes."
                        )
                    },
                    {
                        "step": 2,
                        "title": "Extract Resume Content",
                        "description": (
                            "Parse PDF or DOCX resumes and convert their "
                            "content into clean text."
                        )
                    },
                    {
                        "step": 3,
                        "title": "Build Skill Extraction",
                        "description": (
                            "Use NLP or an LLM to identify technical skills, "
                            "experience, education, and keywords."
                        )
                    },
                    {
                        "step": 4,
                        "title": "Analyze Job Descriptions",
                        "description": (
                            "Extract important requirements and skills from "
                            "the target job description."
                        )
                    },
                    {
                        "step": 5,
                        "title": "Calculate Match Scores",
                        "description": (
                            "Compare candidate skills with job requirements "
                            "and calculate a compatibility score."
                        )
                    },
                    {
                        "step": 6,
                        "title": "Generate Recommendations",
                        "description": (
                            "Provide suggestions for missing skills and "
                            "resume improvements."
                        )
                    },
                    {
                        "step": 7,
                        "title": "Build the Dashboard",
                        "description": (
                            "Display extracted information, match scores, "
                            "and actionable recommendations."
                        )
                    }
                ]
            }
        }

        # ----------------------------------------------------
        # DEFAULT PLAN
        #
        # Used for any project that does not yet have a custom
        # implementation plan.
        # ----------------------------------------------------

        default_plan = {
            "tech_stack": [
                "Python",
                "FastAPI",
                "React"
            ],

            "key_features": [
                "Core project functionality",
                "User-friendly interface",
                "Backend API integration",
                "Error handling"
            ],

            "architecture": [
                "User Interface",
                "Frontend Application",
                "Backend API",
                "Business Logic",
                "Database or External Services"
            ],

            "implementation_steps": [
                {
                    "step": 1,
                    "title": "Plan the Project",
                    "description": (
                        "Define the problem, project scope, users, "
                        "and expected functionality."
                    )
                },
                {
                    "step": 2,
                    "title": "Set Up the Backend",
                    "description": (
                        "Create the API structure and implement the "
                        "core business logic."
                    )
                },
                {
                    "step": 3,
                    "title": "Build the Frontend",
                    "description": (
                        "Create the user interface and connect it "
                        "with the backend API."
                    )
                },
                {
                    "step": 4,
                    "title": "Test and Improve",
                    "description": (
                        "Test the application, handle edge cases, "
                        "and improve the user experience."
                    )
                }
            ]
        }

        # Get the custom plan if it exists.
        # Otherwise use the generic plan.
        project_plan = project_plans.get(
            project_id,
            default_plan
        )

        implementation_steps = [
            ImplementationStep(**step)
            for step in project_plan["implementation_steps"]
        ]

        return ProjectDetails(
            id=project_data["id"],
            name=project_data["name"],
            description=project_data["description"],
            difficulty=project_data["difficulty"],
            skills=sorted(
                skill
                for skill in project_data["skills"]
                if skill is not None
            ),
            tech_stack=project_plan["tech_stack"],
            key_features=project_plan["key_features"],
            architecture=project_plan["architecture"],
            implementation_steps=implementation_steps,
        )

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}"
        )