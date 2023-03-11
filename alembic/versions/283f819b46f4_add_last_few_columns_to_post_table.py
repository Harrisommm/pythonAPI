"""add last few columns to post table

Revision ID: 283f819b46f4
Revises: ddce106be738
Create Date: 2023-03-11 21:37:00.394172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283f819b46f4'
down_revision = 'ddce106be738'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
