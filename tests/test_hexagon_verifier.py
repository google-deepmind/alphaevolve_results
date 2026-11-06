# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Regression tests for the notebook's hexagon packing verifier.

Run with `python -m unittest discover -s tests`. Only NumPy is required;
these tests execute the verifier cell without plotting or unrelated sections.
"""

import ast
import contextlib
import copy
import io
import json
import unittest
from pathlib import Path

import numpy as np


def load_hexagon_verifier():
    """Execute the actual notebook definitions, excluding the plotting import."""
    path = Path(__file__).resolve().parents[1] / "mathematical_results.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", []))
        if cell["cell_type"] != "code" or "def hexagon_vertices(" not in source:
            continue
        tree = ast.parse(source, filename=str(path))
        tree.body = [
            node
            for node in tree.body
            if not (
                isinstance(node, ast.Import)
                and any(alias.name.startswith("matplotlib") for alias in node.names)
            )
        ]
        namespace = {}
        exec(compile(tree, str(path), "exec"), namespace)
        return namespace, notebook
    raise AssertionError("Hexagon verifier cell not found")


class HexagonVerifierTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.namespace, cls.notebook = load_hexagon_verifier()
        cls.verify = staticmethod(cls.namespace["verify_construction"])

    def setUp(self):
        self.output = io.StringIO()
        redirect = contextlib.redirect_stdout(self.output)
        redirect.__enter__()
        self.addCleanup(redirect.__exit__, None, None, None)

    def test_rejects_nonfinite_inner_coordinates_and_angles(self):
        for invalid in (np.nan, np.inf, -np.inf):
            for field in range(3):
                with self.subTest(invalid=invalid, field=field):
                    inner = [[0.0, 0.0, 0.0]]
                    inner[0][field] = invalid
                    with self.assertRaises(AssertionError):
                        self.verify(inner, (0.0, 0.0), 0.1, 0.0)

    def test_rejects_nonfinite_outer_center(self):
        for invalid in (np.nan, np.inf, -np.inf):
            for axis in range(2):
                with self.subTest(invalid=invalid, axis=axis):
                    center = [0.0, 0.0]
                    center[axis] = invalid
                    with self.assertRaises(AssertionError):
                        self.verify([(0.0, 0.0, 0.0)], center, 3.0, 0.0)

    def test_rejects_nonfinite_outer_angle(self):
        for invalid in (np.nan, np.inf, -np.inf):
            with self.subTest(invalid=invalid):
                with self.assertRaises(AssertionError):
                    self.verify([(0.0, 0.0, 0.0)], (0.0, 0.0), 3.0, invalid)

    def test_rejects_nonfinite_or_nonpositive_outer_side(self):
        for side in (np.nan, np.inf, -np.inf, 0.0, -1.0):
            for inner in ([], [(0.0, 0.0, 0.0)]):
                with self.subTest(side=side, inner=inner):
                    with self.assertRaises(AssertionError):
                        self.verify(inner, (0.0, 0.0), side, 0.0)

    def test_rejects_nonfinite_outer_parameters_with_no_inner_hexagons(self):
        for center, angle in (((np.nan, 0.0), 0.0), ((0.0, 0.0), np.nan)):
            with self.subTest(center=center, angle=angle):
                with self.assertRaises(AssertionError):
                    self.verify([], center, 3.0, angle)

    def test_preserves_geometric_rejections(self):
        with self.assertRaisesRegex(AssertionError, "intersect"):
            self.verify([(0.0, 0.0, 0.0)] * 2, (0.0, 0.0), 3.0, 0.0)
        with self.assertRaisesRegex(AssertionError, "contained"):
            self.verify([(0.0, 0.0, 0.0)], (0.0, 0.0), 0.1, 0.0)

    def test_valid_inputs_and_point_iterators_remain_supported(self):
        inner = [(-1.5, 0.0, 15.0), (1.5, 0.0, -15.0)]
        original = copy.deepcopy(inner)
        self.verify(inner, (0.0, 0.0), 4.0, 0.0)
        self.assertEqual(inner, original)
        self.verify(iter(inner), (0.0, 0.0), 4.0, 0.0)
        self.verify(np.asarray(inner), np.array([0.0, 0.0]), np.float64(4), 0.0)
        self.verify(np.asarray(inner, dtype=object), (0.0, 0.0), 4.0, 0.0)
        self.verify([], (0.0, 0.0), 1.0, 0.0)
        self.verify([(0.0, 0.0, 0.0)], (0.0, 0.0), 1.0, 0.0)
        self.assertEqual(self.output.getvalue().count("Construction is valid."), 6)

    def test_both_published_constructions_still_pass(self):
        count = 0
        for cell in self.notebook["cells"]:
            source = "".join(cell.get("source", []))
            if cell["cell_type"] != "code" or not source.startswith(
                "#@title Construction"
            ):
                continue
            if "inner_hex_data =" not in source:
                continue
            namespace = {"np": np}
            exec(compile(source, "published hexagon construction", "exec"), namespace)
            self.verify(
                namespace["inner_hex_data"],
                namespace["outer_hex_center"],
                namespace["outer_hex_side_length"],
                namespace["outer_hex_angle_degrees"],
            )
            count += 1
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
