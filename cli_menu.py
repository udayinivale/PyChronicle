import click

@click.command()
def menu():
    """Display the PyChronicle CLI menu."""

    click.echo("\n========== PyChronicle CLI ==========")
    click.echo("1. Run Trace        - Trace a Python script")
    click.echo("2. View Trace       - View the latest trace")
    click.echo("3. Replay Trace     - Replay a previous trace")
    click.echo("4. Exit")
    click.echo("=====================================")

if __name__ == "__main__":
    menu()