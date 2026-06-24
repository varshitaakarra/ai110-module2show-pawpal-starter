"""PawPal+ core domain classes.

Skeleton generated from diagrams/uml.mmd. Method bodies are stubs (no logic yet)
to be filled in incrementally.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Pet:
    name: str
    species: str
    age: int

    def describe(self) -> str:
        """Return a short human-readable summary of the pet."""
        raise NotImplementedError


@dataclass
class Owner:
    name: str
    available_minutes: int

    def has_time_for_task(self, task: "Task") -> bool:
        """Return True if the owner has enough free minutes for the given task."""
        raise NotImplementedError


@dataclass
class Task:
    title: str
    duration_mins: int
    priority: str
    category: str

    def is_high_priority(self) -> bool:
        """Return True if this task is high priority."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


@dataclass
class Schedule:
    pet: Pet
    owner: Owner
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the schedule."""
        raise NotImplementedError

    def remove_task(self, task: Task) -> None:
        """Remove a task from the schedule."""
        raise NotImplementedError

    def total_duration(self) -> int:
        """Return the total duration (minutes) of all tasks."""
        raise NotImplementedError

    def fits_in_budget(self) -> bool:
        """Return True if total task duration fits the owner's available minutes."""
        raise NotImplementedError


class Scheduler:
    """Stateless planner that turns a Schedule into a daily plan."""

    def sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Return tasks ordered by priority."""
        raise NotImplementedError

    def filter_to_time_budget(self, tasks: list[Task], owner: Owner) -> list[Task]:
        """Return the subset of tasks that fit within the owner's time budget."""
        raise NotImplementedError

    def build_plan(self, schedule: Schedule) -> list[Task]:
        """Produce the final ordered, budget-respecting daily plan."""
        raise NotImplementedError

    def explain(self, schedule: Schedule) -> str:
        """Explain the reasoning behind the generated plan."""
        raise NotImplementedError
