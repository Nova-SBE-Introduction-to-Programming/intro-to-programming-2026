import tempfile
import unittest
from pathlib import Path

from build import materials_list


class MaterialsListTests(unittest.TestCase):
    def test_decks_and_briefs_have_distinct_labels(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'index.md').write_text('# Week')
            (root / 'class-5.html').write_text('<title>Class 5</title>')
            (root / 'class-4.pdf').write_bytes(b'pdf')
            (root / '01-brief.html').write_text('<title>Plot Twist BRD · Nova SBE</title>')
            html = materials_list(root)
            self.assertEqual(html.count('Open presentation'), 2)
            self.assertIn('<a href="01-brief.html">Plot Twist BRD</a>', html)
            self.assertNotIn('index.md', html)

    def test_document_titles_are_escaped_and_missing_titles_fall_back(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'brief.html').write_text('<title>A &amp; B &lt;example&gt;</title>')
            (root / 'notes.html').write_text('<p>No title</p>')
            html = materials_list(root)
            self.assertIn('A &amp; B &lt;example&gt;', html)
            self.assertIn('>notes</a>', html)

    def test_markdown_downloads_and_subfolders(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'plan.md').write_text('---\ntitle: First feature\n---\n# Plan')
            (root / 'starter.zip').write_bytes(b'zip')
            (root / 'assets').mkdir()
            (root / '.private').write_text('hidden')
            html = materials_list(root)
            self.assertIn('href="plan.html">First feature', html)
            self.assertIn('href="starter.zip" download', html)
            self.assertNotIn('assets', html)
            self.assertNotIn('.private', html)


if __name__ == '__main__':
    unittest.main()
