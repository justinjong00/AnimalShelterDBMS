"""with added contact

Revision ID: e9405970e459
Revises: fd40fb881deb
Create Date: 2022-12-01 01:13:48.665000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9405970e459'
down_revision = 'fd40fb881deb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'contact', ['info_id'], ['id'])

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'contact', ['info_id'], ['id'])

    with op.batch_alter_table('foster', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'foster_date'])

    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['diagnosis_id', 'operation_type', 'date'])

    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['treatment', 'diagnosis_id'])

    with op.batch_alter_table('vaccination', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['animal_id', 'vaccine_type', 'date'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vaccination', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('treatment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('surgery', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('foster', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###