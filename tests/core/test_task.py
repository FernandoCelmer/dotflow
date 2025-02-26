"""Test context of task"""

import unittest

from dotflow.core.context import Context
from dotflow.core.models.status import Status
from dotflow.core.task import Task

from tests.mocks import (
    action_step,
    simple_callback
)


class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task(
            task_id=0,
            step=action_step,
            callback=simple_callback
        )
        self.content = {"foo": "bar"}

    def test_instantiating_class(self):
        Task(
            task_id=0,
            initial_context=Context(
                storage=self.content
            ),
            step=action_step,
            callback=simple_callback
        )

    def test_task_id(self):
        task = Task(
            task_id=0,
            initial_context=Context(
                storage=self.content
            ),
            step=action_step,
            callback=simple_callback
        )

        self.assertEqual(task.task_id, 0)

    def test_initial_context(self):
        task = Task(
            task_id=0,
            initial_context=Context(
                storage=self.content
            ),
            step=action_step,
            callback=simple_callback
        )

        self.assertEqual(
            task.initial_context.storage,
            self.content
        )

    def test_set_status(self):
        expected_value = Status.COMPLETED

        self.task.set_status(value=expected_value)
        self.assertEqual(self.task.status, expected_value)

    def test_set_duration(self):
        expected_value = 42

        self.task.set_duration(value=expected_value)
        self.assertEqual(self.task.duration, expected_value)

    def test_set_current_context(self):
        expected_value = Context(storage=self.content)

        self.task.set_current_context(value=expected_value)
        self.assertEqual(self.task.current_context, expected_value)

    def test_set_previous_context(self):
        expected_value = Context(storage=self.content)

        self.task.set_previous_context(value=expected_value)
        self.assertEqual(self.task.previous_context, expected_value)
