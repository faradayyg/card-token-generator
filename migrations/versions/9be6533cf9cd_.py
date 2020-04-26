"""empty message

Revision ID: 9be6533cf9cd
Revises: 7eb82d844e18
Create Date: 2020-04-26 05:51:50.841434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9be6533cf9cd'
down_revision = '7eb82d844e18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('iv_string', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'iv_string')
    # ### end Alembic commands ###
