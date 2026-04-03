# FuncMage Compliance Report

Scope reviewed:
- Subject: `subject.pdf`
- Evaluation sheet: `evaluation_sheet.pdf`
- Exercises: `ex0` to `ex4`

Validation done:
- `python3 -m py_compile ex0/lambda_spells.py ex1/higher_magic.py ex2/scope_mysteries.py ex3/functools_artifacts.py ex4/decorator_mastery.py`
- `python3 -m flake8 ex0 ex1 ex2 ex3 ex4`
- Manual behavior checks against evaluator checklist

## ex0 (`ex0/lambda_spells.py`)
Status: Mostly compliant.

Changes needed:
1. Update function signatures to match subject exactly:
   - `artifact_sorter(artifacts: list[dict]) -> list[dict]`
   - `power_filter(mages: list[dict], min_power: int) -> list[dict]`
   - `spell_transformer(spells: list[str]) -> list[str]`
   - `mage_stats(mages: list[dict]) -> dict`
2. Add graceful handling for empty `mages` in `mage_stats` (currently `max()/min()` and division can crash).

## ex1 (`ex1/higher_magic.py`)
Status: Compliant for evaluator behavior.

Changes needed:
1. Tighten type hints to align with subject wording:
   - `spells: list[callable]` in `spell_sequence`
2. Optional but safer for "same arguments" requirement: support both `*args` and `**kwargs` in returned closures.

## ex2 (`ex2/scope_mysteries.py`)
Status: Compliant for evaluator behavior.

Changes needed:
1. Make type hints match subject more closely:
   - `memory_vault() -> dict[str, callable]`
2. In `memory_vault.store`, allow generic values (not only `str`) to match `(key, value)` requirement.

## ex3 (`ex3/functools_artifacts.py`)
Status: Not fully compliant (functional issue found).

Changes needed:
1. Fix `partial_enchanter` partial application.
   - Current implementation passes `power` and `element` as keywords.
   - This can fail for base functions with positional signature `(power, element, target)`.
   - Use positional partials, e.g. `partial(base_enchantment, 50, 'fire')`.
2. Align `spell_reducer` with requirement "use operator module functions" for all operations.
   - `add`/`multiply` already use `operator`.
   - For `max`/`min`, avoid custom manual comparison lambdas and use operator-based comparison logic.
3. Tighten type hint to `spells: list[int]`.

## ex4 (`ex4/decorator_mastery.py`)
Status: Not fully compliant (functional issue found).

Changes needed:
1. Fix `power_validator` logic.
   - Requirement says validate the first argument (`power`).
   - Current code reads `args[-1]`, which breaks standalone decorated functions like `fn(power, target)`.
   - This was reproduced with a `TypeError` during testing.
2. Ensure decorator wrappers have complete type hints (parameters and return types), per evaluation sheet quality section.
3. Keep `MageGuild.cast_spell` behavior as is, but ensure decorator power extraction is robust for methods and normal functions.

## Global repository checklist (important for peer-eval preliminaries)
1. Ensure only requested deliverables are present in the submitted repository.
2. Remove `.DS_Store` and other non-requested files before final submission if they are tracked.

