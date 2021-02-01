"""create 'issues' table

Revision ID: 7442b38f2f16
Revises: 6ebb4bc3e02e
Create Date: 2021-01-12 01:17:53.896203

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7442b38f2f16'
down_revision = '6ebb4bc3e02e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'issues',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column(
            'reporter_id',
            sa.Integer,
            sa.ForeignKey('users.id', ondelete='cascade'),
            nullable=False,
        ),
        sa.Column(
            'assignee_id',
            sa.Integer,
            sa.ForeignKey('users.id', ondelete='cascade'),
            nullable=False,
        ),
        sa.Column('ref_number', sa.String(255), nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('date_discovered', sa.Date, nullable=False),
        sa.Column(
            'created_at',
            sa.DateTime,
            server_default=sa.text('now()'),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table('issues')
