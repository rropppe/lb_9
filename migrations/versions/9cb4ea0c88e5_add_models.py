"""add models

Revision ID: 9cb4ea0c88e5
Revises: 
Create Date: 2023-06-20 21:25:50.100297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cb4ea0c88e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SEA_divisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SEA_employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('patronymic', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SEA_positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('SEA_job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staffer_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.Column('division_id', sa.Integer(), nullable=True),
    sa.Column('date_of_employment', sa.String(), nullable=False),
    sa.Column('date_of_dismissal', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['division_id'], ['SEA_divisions.id'], ),
    sa.ForeignKeyConstraint(['position_id'], ['SEA_positions.id'], ),
    sa.ForeignKeyConstraint(['staffer_id'], ['SEA_employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('SEA_job')
    op.drop_table('SEA_positions')
    op.drop_table('SEA_employees')
    op.drop_table('SEA_divisions')
    # ### end Alembic commands ###
