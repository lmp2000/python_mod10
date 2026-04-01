def artifact_sorter(artifacts: list) -> list:
    return sorted(
        artifacts, key=lambda x: x['power'], reverse=True
        )


def power_filter(mages: list, min_power: int) -> list:
    return list(
        filter(lambda m: m['power'] >= min_power, mages)
    )


def spell_transformer(spells: list) -> list:
    return list(
        map(lambda s: '* ' + s + ' *', spells)
    )


def mage_stats(mages: list) -> dict:
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    total = len(mages)
    total_power = sum(list(
        map(lambda mag: mag['power'], mages)
    ))
    avg_power = round(total_power / total, 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Dagger", "power": 78, "type": "weapon"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']}"
        f" ({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))
