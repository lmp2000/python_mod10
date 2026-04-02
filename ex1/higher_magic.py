from typing import Callable


def spell_combiner(
        spell1: Callable, spell2: Callable
        ) -> Callable:
    def combined(*args) -> tuple:
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(
        base_spell: Callable, multiplier: int
        ) -> Callable:
    def power_spell(*args) -> int:
        return base_spell(*args) * multiplier
    return power_spell


def conditional_caster(
        condition: Callable, spell: Callable
        ) -> Callable:
    def caster(*args) -> int | str:
        if condition(*args):
            return spell(*args)
        else:
            return 'Spell fizzled'
    return caster


def spell_sequence(spells: list) -> Callable:
    def sequence(*args) -> list:
        results: list = []
        for function in spells:
            results.append(function(*args))
        return results
    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def base_damage(target: str) -> int:
        return 10

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon")
    print(
        f"Combined spell result: {combined_result[0]}, {combined_result[1]}"
        )

    print("\nTesting power amplifier...")
    mega_spell = power_amplifier(base_damage, 3)
    original = base_damage("Dragon")
    amplified = mega_spell("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")
