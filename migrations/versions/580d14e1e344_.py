"""empty message

Revision ID: 580d14e1e344
Revises: 
Create Date: 2023-06-05 08:53:30.208112

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '580d14e1e344'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('perfil', schema=None) as batch_op:
        batch_op.alter_column('senha',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=99),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('perfil', schema=None) as batch_op:
        batch_op.alter_column('senha',
               existing_type=sa.String(length=99),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
