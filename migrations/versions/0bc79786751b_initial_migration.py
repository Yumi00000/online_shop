"""initial migration

Revision ID: 0bc79786751b
Revises: 3aacdd268767
Create Date: 2024-01-10 12:46:54.482121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bc79786751b'
down_revision = '3aacdd268767'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('description', sa.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###