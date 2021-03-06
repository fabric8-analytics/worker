"""add column source and telemetry_id to component_analyses_request.

Revision ID: ad4686cd22a6
Revises: 30d1b65971a2
Create Date: 2021-03-02 16:33:16.987879

"""

# revision identifiers, used by Alembic.
revision = 'ad4686cd22a6'
down_revision = '30d1b65971a2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    """Upgrade the database to a newer revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('component_analyses_requests',
                  sa.Column('source', sa.String(length=256), nullable=True))
    op.add_column('component_analyses_requests',
                  sa.Column('telemetry_id', postgresql.UUID(as_uuid=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('component_analyses_requests', 'telemetry_id')
    op.drop_column('component_analyses_requests', 'source')
    # ### end Alembic commands ###
