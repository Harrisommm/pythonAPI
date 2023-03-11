"""content column added

Revision ID: 7c2fa03a4279
Revises: a458cc6bd495
Create Date: 2023-03-11 21:00:21.390296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2fa03a4279'
down_revision = 'a458cc6bd495'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('creted_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    
    op.drop_table('users')
    
    pass
