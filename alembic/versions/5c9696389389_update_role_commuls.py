"""update role commuls

Revision ID: 5c9696389389
Revises: a9127f6787b6
Create Date: 2019-04-06 10:45:42.869244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9696389389'
down_revision = 'a9127f6787b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_role', sa.Column('description', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_role', 'description')
    # ### end Alembic commands ###
