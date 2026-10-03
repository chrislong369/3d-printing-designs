"""Regression checks for cleanup: UTF-8 paths and safe intake in temporary folders."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

checker = load(ROOT / 'scripts/check_3d_library.py')
intake = load(ROOT / 'tools/file_organizer/organizer.py')

class WorkspaceChecks(unittest.TestCase):
    def test_unicode_tracked_path_is_not_git_quoted(self):
        result = type('Result', (), {'stdout': 'Personal/Hænger_milwaukee.3mf\0'.encode()})()
        with patch.object(checker.subprocess, 'run', return_value=result):
            self.assertEqual(checker.all_tracked_files(), ['Personal/Hænger_milwaukee.3mf'])
        self.assertEqual(checker.validate_path('Personal/Hænger_milwaukee.3mf')[0], [])

    def test_source_extensions_and_launcher(self):
        for path in ['run_organizer.bat', 'Personal/design.step', 'In_Progress/design.blend', 'Final_Products/.gitkeep']:
            self.assertEqual(checker.validate_path(path)[0], [])

    def test_intake_preview_collisions_and_duplicates(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'
            source = Path(folder) / 'incoming'
            root.mkdir()
            source.mkdir()
            model = source / 'sample.stl'
            model.write_bytes(b'intake test fixture')
            config = Path(folder) / 'config.json'
            config.write_text(json.dumps({'destination': 'Needs_Review', 'extensions': ['.stl']}))
            args = ['intake', '--source', str(source), '--config', str(config)]
            with patch.object(intake, 'ROOT', root), patch.object(sys, 'argv', args):
                intake.main()
            self.assertTrue(model.exists())
            self.assertFalse((root / 'Needs_Review').exists())
            destination = root / 'Needs_Review'
            destination.mkdir()
            (destination / 'sample.stl').write_bytes(b'different known keeper')
            with patch.object(intake, 'ROOT', root), patch.object(sys, 'argv', args + ['--apply']):
                intake.main()
            self.assertEqual((destination / 'sample.stl').read_bytes(), b'different known keeper')
            self.assertEqual((destination / 'sample__intake2.stl').read_bytes(), b'intake test fixture')
            model.write_bytes(b'different known keeper')
            with patch.object(intake, 'ROOT', root), patch.object(sys, 'argv', args + ['--apply']):
                intake.main()
            self.assertTrue(model.exists())

    def test_intake_rejects_repo_scan_and_destination_escape(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / 'repo'
            source = Path(folder) / 'incoming'
            root.mkdir()
            source.mkdir()
            config = Path(folder) / 'config.json'
            config.write_text(json.dumps({'destination': '../outside', 'extensions': ['.stl']}))
            for scan in [root, source]:
                with patch.object(intake, 'ROOT', root), patch.object(sys, 'argv', ['intake', '--source', str(scan), '--config', str(config)]):
                    with self.assertRaises(SystemExit):
                        intake.main()

if __name__ == '__main__':
    unittest.main()
