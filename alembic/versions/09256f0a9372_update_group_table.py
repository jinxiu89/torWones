"""update group table

Revision ID: 09256f0a9372
Revises: 366258d6b888
Create Date: 2019-04-07 10:22:54.341574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09256f0a9372'
down_revision = '366258d6b888'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_permission_group', sa.Column('description', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_permission_group', 'description')
    # ### end Alembic commands ###