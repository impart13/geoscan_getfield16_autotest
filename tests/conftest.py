import pytest
import subprocess
import os
from pathlib import Path

@pytest.fixture(scope="session")
def binary_path():
    project_root = Path(__file__).parent.parent
    binary = project_root / "src" / "bin" / "getfield16"
    if not binary.exists():
        pytest.fail(f"Бинарный файл не найден: {binary}")
    if not os.access(binary, os.X_OK):
        pytest.fail(f"Файл не исполняемый: {binary}")
    return str(binary)

@pytest.fixture
def run_getfield16(binary_path):
    def _run(hex_string, start_bit):
        try:
            result = subprocess.run(
                [binary_path, str(hex_string), str(start_bit)],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip() + result.stderr.strip()
        except subprocess.TimeoutExpired:
            pytest.fail("TimeOut")
        except Exception as e:
            pytest.fail(f"Прочие ошибки: {e}")
    return _run
