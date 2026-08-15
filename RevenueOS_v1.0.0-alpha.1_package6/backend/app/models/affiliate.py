from datetime import datetime
from decimal import Decimal
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.app.db.base import Base

class AffiliateProgram(Base):
    __tablename__ = "affiliate_programs"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    network: Mapped[str] = mapped_column(String(100))
    signup_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    commission_rate: Mapped[Decimal] = mapped_column(Numeric(6, 3), default=Decimal("0"))
    status: Mapped[str] = mapped_column(String(30), default="active")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    links = relationship("AffiliateLink", back_populates="program", cascade="all, delete-orphan")

class AffiliateLink(Base):
    __tablename__ = "affiliate_links"
    id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(ForeignKey("affiliate_programs.id"), index=True)
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.id"), nullable=True, index=True)
    url: Mapped[str] = mapped_column(Text)
    label: Mapped[str | None] = mapped_column(String(200), nullable=True)
    clicks: Mapped[int] = mapped_column(default=0)
    conversions: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    program = relationship("AffiliateProgram", back_populates="links")
    product = relationship("Product")
