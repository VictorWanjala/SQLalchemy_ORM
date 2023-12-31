"""added student model

Revision ID: ba7c7c5e53ca
Revises: 658b28b82bf7
Create Date: 2023-09-28 09:41:27.885719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba7c7c5e53ca'
down_revision: Union[str, None] = '658b28b82bf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('index', sa.Integer(), nullable=True))
    op.drop_column('students', 'Index')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('Index', sa.INTEGER(), nullable=True))
    op.drop_column('students', 'index')
    # ### end Alembic commands ###
