import sys
from pathlib import Path

# Add the backend directory to Python's module search path
BACKEND_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BACKEND_DIR))

from app.core.database import db


def test_connection():
    try:
        print("Connecting to CognoDB...")

        db.verify_connection()

        with db.get_session() as session:
            result = session.run(
                "RETURN $message AS message",
                message="SkillGraph AI successfully connected to CognoDB!"
            )

            record = result.single()
            print(record["message"])

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    test_connection()