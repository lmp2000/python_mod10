from functools import reduce, partial
from functools import lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(
        spells: list, operation: str
        ) -> int:
    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': lambda x, y: x if x > y else y,
        'min': lambda x, y: x if x < y else y
    }

    if operation not in operations:
        raise ValueError(
            f'Operation invalid: {operation}'
        )

    return reduce(operations[operation], spells)


def partial_enchanter(
        base_enchantment: Callable
        ) -> dict:
    return {
        'fire_enchant': partial(
            base_enchantment, power=50, element='fire'
        ),
        'ice_enchant': partial(
            base_enchantment, power=50, element='ice'
        ),
        'lightning_enchant': partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def cast_spell(spell: Any) -> str:
        return f'Unknown spell: {type(spell)}'

    @cast_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} points of damage"

    @cast_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast_spell.register(list)
    def _(spell: list) -> str:
        spell_agregator = ', '.join(spell)
        return f'Multi spell: {spell_agregator}'

    return cast_spell


if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
