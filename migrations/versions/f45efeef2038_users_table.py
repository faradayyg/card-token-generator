"""users table

Revision ID: f45efeef2038
Revises: 3ce29500b8dd
Create Date: 2020-04-24 04:17:26.191296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f45efeef2038'
down_revision = '3ce29500b8dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('secret_key', sa.String(length=12), nullable=True))
    op.add_column('user', sa.Column('token', sa.String(length=12), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token')
    op.drop_column('user', 'secret_key')
    # ### end Alembic commands ###