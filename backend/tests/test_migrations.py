import os
import tempfile
import pytest
from sqlalchemy import create_engine, inspect
from alembic.config import Config
from alembic import command

def test_alembic_migration_lifecycle():
    """
    End-to-end regression test for Alembic migrations:
    1. Applies 'upgrade head' on a completely fresh temporary SQLite database.
    2. Inspects that all domain tables and columns exist with proper schemas.
    3. Executes 'downgrade base' to verify complete schema teardown.
    4. Re-applies 'upgrade head' to verify re-application idempotency.
    """
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    alembic_ini_path = os.path.join(backend_dir, "alembic.ini")
    assert os.path.exists(alembic_ini_path), f"Missing alembic.ini at {alembic_ini_path}"

    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp_db:
        tmp_db_path = tmp_db.name

    try:
        db_url = f"sqlite:///{tmp_db_path}"
        
        # Configure Alembic
        alembic_cfg = Config(alembic_ini_path)
        alembic_cfg.set_main_option("sqlalchemy.url", db_url)
        alembic_cfg.set_main_option("script_location", os.path.join(backend_dir, "alembic"))

        # 1. Apply all migrations up to HEAD on fresh database
        command.upgrade(alembic_cfg, "head")

        # 2. Inspect created schema
        engine = create_engine(db_url)
        inspector = inspect(engine)
        tables = set(inspector.get_table_names())
        
        expected_tables = {
            "users",
            "companies",
            "job_applications",
            "interview_stages",
            "application_notes",
            "alembic_version"
        }
        assert expected_tables.issubset(tables), f"Missing tables after upgrade head: {expected_tables - tables}"

        # Check company columns (ensure notes is absent, industry is present)
        company_cols = {c["name"] for c in inspector.get_columns("companies")}
        assert "industry" in company_cols, "Missing 'industry' column in companies table"
        assert "notes" not in company_cols, "'notes' column should not exist on public company table"

        # Check job_applications columns
        app_cols = {c["name"] for c in inspector.get_columns("job_applications")}
        assert {"user_id", "company_id", "status", "job_title"}.issubset(app_cols)

        # 3. Test downgrade to base
        command.downgrade(alembic_cfg, "base")
        inspector_after_down = inspect(engine)
        tables_after_down = set(inspector_after_down.get_table_names())
        
        # Application tables should be removed
        for t in ["users", "companies", "job_applications", "interview_stages", "application_notes"]:
            assert t not in tables_after_down, f"Table '{t}' was not dropped during downgrade base"

        # 4. Re-apply upgrade head to confirm clean re-execution
        command.upgrade(alembic_cfg, "head")
        inspector_reup = inspect(engine)
        reup_tables = set(inspector_reup.get_table_names())
        assert expected_tables.issubset(reup_tables), "Failed re-applying migrations after downgrade"

        engine.dispose()
    finally:
        if os.path.exists(tmp_db_path):
            try:
                os.remove(tmp_db_path)
            except OSError:
                pass
