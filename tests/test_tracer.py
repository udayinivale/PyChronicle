import unittest

from pychronicle.tracer import PyChronicleTracer


class TestTracer(unittest.TestCase):

    def test_step_counter(self):

        tracer = PyChronicleTracer()

        self.assertEqual(tracer.next_step(), 1)
        self.assertEqual(tracer.next_step(), 2)
        self.assertEqual(tracer.next_step(), 3)


if __name__ == "__main__":
    unittest.main()