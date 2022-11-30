"""changed contact and background so no _

Revision ID: a749771f9215
Revises: 8b31e3856934
Create Date: 2022-11-30 06:32:47.960988

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a749771f9215'
down_revision = '8b31e3856934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('background_check',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('income', sa.Integer(), nullable=False),
    sa.Column('ciminal_record', sa.String(length=150), nullable=False),
    sa.Column('credit_score', sa.Integer(), nullable=False),
    sa.Column('interview_status', sa.String(length=150), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('background_check_status', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    with op.batch_alter_table('contact__information', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('phone')

    op.drop_table('contact__information')
    op.drop_table('background__check')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('background__check',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('application_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('income', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ciminal_record', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('credit_score', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('interview_status', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('employee_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('background_check_status', mysql.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('contact__information',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('contact__information', schema=None) as batch_op:
        batch_op.create_index('phone', ['phone'], unique=False)
        batch_op.create_index('email', ['email'], unique=False)

    op.drop_table('contact_information')
    op.drop_table('background_check')
    # ### end Alembic commands ###
