from unit_converter.app import Application
from unit_converter.registry import UnitRegistry


def main() -> None:
    registry = UnitRegistry.default()
    app = Application(registry=registry)
    app.run()


if __name__ == "__main__":
    main()
