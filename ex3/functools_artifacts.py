from functools import reduce, partial
from functools import lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(
        spells: list[int], operation: str
        ) -> int:
    def greater(left: int, right: int) -> int:
        if operator.gt(left, right):
            return left
        return right

    def lower(left: int, right: int) -> int:
        if operator.lt(left, right):
            return left
        return right

    operations = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': greater,
        'min': lower
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
            base_enchantment, 50, 'fire'
        ),
        'ice_enchant': partial(
            base_enchantment, 50, 'ice'
        ),
        'lightning_enchant': partial(
            base_enchantment, 50, 'lightning'
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
