from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(
        enchantment_type: str
        ) -> Callable:
    def enchanter(item_name: str) -> str:
        return f'{enchantment_type} {item_name}'
    return enchanter


def memory_vault() -> dict:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, 'Memory not found')

    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
