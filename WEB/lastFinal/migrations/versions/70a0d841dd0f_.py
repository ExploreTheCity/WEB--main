"""empty message

Revision ID: 70a0d841dd0f
Revises: 18a1e31cb416
Create Date: 2024-05-26 22:33:35.789967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70a0d841dd0f'
down_revision = '18a1e31cb416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant')
    op.drop_table('bar')
    op.drop_table('tourist_attraction')
    op.drop_table('cultural_place')
    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cultural_places', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('tourist_attractions', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('restaurants', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('bars', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('accommodation', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('transportation', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('city', schema=None) as batch_op:
        batch_op.drop_column('transportation')
        batch_op.drop_column('accommodation')
        batch_op.drop_column('bars')
        batch_op.drop_column('restaurants')
        batch_op.drop_column('tourist_attractions')
        batch_op.drop_column('cultural_places')

    op.create_table('cultural_place',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('city_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tourist_attraction',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('city_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bar',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('city_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('city_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
