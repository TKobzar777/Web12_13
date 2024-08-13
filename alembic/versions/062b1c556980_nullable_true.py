"""nullable True

Revision ID: 062b1c556980
Revises: 035e530d8d6f
Create Date: 2024-08-12 23:54:08.378011

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '062b1c556980'
down_revision: Union[str, None] = '035e530d8d6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'avatar',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'avatar',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
