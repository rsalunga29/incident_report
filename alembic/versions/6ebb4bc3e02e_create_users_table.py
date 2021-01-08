"""create 'users' table

Revision ID: 6ebb4bc3e02e
Revises: 
Create Date: 2021-01-04 17:56:15.423656

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '6ebb4bc3e02e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.Binary(), nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime,
            server_default=sa.text('now()'),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table('users')
