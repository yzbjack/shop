"""empty message

Revision ID: 290d44ac7d08
Revises: 126c69911a6d
Create Date: 2018-02-25 15:28:35.996684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290d44ac7d08'
down_revision = '126c69911a6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthday', sa.DATE(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'birthday')
    # ### end Alembic commands ###
