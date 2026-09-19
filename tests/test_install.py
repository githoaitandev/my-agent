from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def assert_profile_installed(self, target: Path) -> None:
        self.assertTrue((target / "AGENTS.md").is_file())
        self.assertTrue((target / ".codex" / "config.toml").is_file())
        self.assertTrue(
            (target / ".agents" / "skills" / "my-agent" / "SKILL.md").is_file()
        )

    def test_shell_launcher_uses_lf_line_endings(self) -> None:
        content = (ROOT / "install.sh").read_bytes()

        self.assertNotIn(b"\r\n", content)

    @unittest.skipUnless(shutil.which("bash"), "Bash is not available")
    def test_shell_launcher_installs_profile(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT) as temp_dir:
            target = Path(temp_dir)

            result = subprocess.run(
                ["bash", "./install.sh", target.name],
                check=False,
                capture_output=True,
                cwd=ROOT,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_profile_installed(target)

    @unittest.skipUnless(
        shutil.which("powershell") or shutil.which("pwsh"),
        "PowerShell is not available",
    )
    def test_powershell_launcher_installs_profile(self) -> None:
        powershell = shutil.which("powershell") or shutil.which("pwsh")

        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)

            result = subprocess.run(
                [
                    powershell,
                    "-NoProfile",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(ROOT / "install.ps1"),
                    str(target),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_profile_installed(target)

    def test_python_installer_installs_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir)

            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "install.py"), str(target)],
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assert_profile_installed(target)


if __name__ == "__main__":
    unittest.main()
