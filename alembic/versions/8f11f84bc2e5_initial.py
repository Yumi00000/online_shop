"""initial

Revision ID: 8f11f84bc2e5
Revises: 7384430dc36a
Create Date: 2024-01-28 00:30:28.865142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f11f84bc2e5'
down_revision: Union[str, None] = '7384430dc36a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('rating', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'feedback', ['rating'], ['rating'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'rating')
    # ### end Alembic commands ###
