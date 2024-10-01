"""rename address

Revision ID: f60ed889637a
Revises: 98b850a04d8e
Create Date: 2024-10-01 15:02:01.892911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f60ed889637a'
down_revision = '98b850a04d8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###
