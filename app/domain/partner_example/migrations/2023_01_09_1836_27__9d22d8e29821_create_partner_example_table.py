"""create partner_example table

Revision ID: 9d22d8e29821
Revises: c126b5ecd721
Create Date: 2022-12-27 15:45:40.889279

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "9d22d8e29821"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "partner_example",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("document", sa.String(14), unique=True, index=True),
        sa.Column("name", sa.String(128)),
        sa.Column("active", sa.Boolean(), default=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True),
        sa.Column("canceled_at", sa.DateTime(), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("partner_example")
