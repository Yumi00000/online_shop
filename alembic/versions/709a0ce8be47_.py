"""empty message

Revision ID: 709a0ce8be47
Revises: e783a91e9b82
Create Date: 2024-01-27 15:05:22.709044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '709a0ce8be47'
down_revision: Union[str, None] = 'e783a91e9b82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
