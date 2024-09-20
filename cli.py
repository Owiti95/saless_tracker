import click
from sqlalchemy.orm import Session
from models import Expense, SessionLocal

@click.group()
def cli():
    """Simple Expense Tracker CLI"""
    pass

@cli.command()
@click.argument('name')
@click.argument('amount', type=float)
def add(name, amount):
    """Add a new expense"""
    db: Session = SessionLocal()
    expense = Expense(name=name, amount=amount)
    db.add(expense)
    db.commit()
    db.close()
    click.echo(f"Added expense: {name} - ${amount:.2f}")

@cli.command()
def list():
    """List all expenses"""
    db: Session = SessionLocal()
    expenses = db.query(Expense).all()
    db.close()
    for expense in expenses:
        click.echo(f"{expense.id}: {expense.name} - ${expense.amount:.2f}")

if __name__ == '__main__':
    cli()
