"""create test example table

Revision ID: c126b5ecd721
Revises: a63e70e0b501
Create Date: 2022-12-27 11:18:12.749754

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "c126b5ecd721"
down_revision = "9d22d8e29821"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "test_example",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("title", sa.String(100), nullable=False),
        sa.Column("partner_example_id", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(
            ("partner_example_id",),
            ["partner_example.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("test_example")
