"""update products skus

Revision ID: d6c7aa01fdd0
Revises: 2ec42edc50cd
Create Date: 2019-08-19 14:46:38.941194

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd6c7aa01fdd0'
down_revision = '2ec42edc50cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_product', sa.Column('description', sa.String(length=128), nullable=True, comment='SKU描述'))
    op.add_column('tb_product', sa.Column('keywords', sa.String(length=128), nullable=True, comment='关键词'))
    op.add_column('tb_product', sa.Column('name', sa.String(length=128), nullable=True, comment='产品标题'))
    op.add_column('tb_product', sa.Column('price', sa.DECIMAL(precision=5, scale=2), nullable=True, comment='商品最低价格,保留2位小数'))
    op.add_column('tb_product', sa.Column('rating', sa.Float(precision=2), nullable=True, comment='商品评分'))
    op.add_column('tb_product', sa.Column('review_count', sa.Integer(), nullable=True, comment='评论数量'))
    op.add_column('tb_product', sa.Column('sales_volume', sa.Integer(), nullable=True, comment='销售量'))
    op.add_column('tb_product', sa.Column('status', sa.SmallInteger(), nullable=True, comment='是否在售'))
    op.add_column('tb_product', sa.Column('thumbnail', sa.String(length=255), nullable=True, comment='缩略图'))
    op.alter_column('tb_product', 'title',
               existing_type=mysql.VARCHAR(length=64),
               comment='url_标题',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tb_product', 'title',
               existing_type=mysql.VARCHAR(length=64),
               comment=None,
               existing_comment='url_标题',
               existing_nullable=False)
    op.drop_column('tb_product', 'thumbnail')
    op.drop_column('tb_product', 'status')
    op.drop_column('tb_product', 'sales_volume')
    op.drop_column('tb_product', 'review_count')
    op.drop_column('tb_product', 'rating')
    op.drop_column('tb_product', 'price')
    op.drop_column('tb_product', 'name')
    op.drop_column('tb_product', 'keywords')
    op.drop_column('tb_product', 'description')
    # ### end Alembic commands ###