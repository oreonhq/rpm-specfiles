#!/usr/bin/env python3
"""Apply kf6-kcodecs-style Qt6 qdoc packaging to KF6 framework specs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SKIP_SPECS = frozenset(
    {
        "kf6-breeze-icons.spec",
        "kf6-kapidox.spec",
        "kf6-kded.spec",
        "kf6-kimageformats.spec",
        "kf6-qqc2-desktop-style.spec",
        "kf6-kirigami-addons.spec",
    }
)

HTML_PKG = """%package\thtml
Summary:\tDeveloper Documentation files for %{name} in HTML format
BuildArch:\tnoarch
%description\thtml
Developer Documentation files for %{name} in HTML format
"""

INSTALL_SNIPPET = """# Qt6 qdoc: list all files under %{_qt6_docdir} except tags/index (-devel owns those).
: > %{_builddir}/%{framework}-qt6doc.files
if [ -d "%{buildroot}%{_qt6_docdir}" ]; then
  find "%{buildroot}%{_qt6_docdir}" -type f \\
    ! -name '*.tags' ! -name '*.index' \\
    | sed "s#^%{buildroot}##" >> %{_builddir}/%{framework}-qt6doc.files
fi
LC_ALL=C sort -u -o %{_builddir}/%{framework}-qt6doc.files %{_builddir}/%{framework}-qt6doc.files
"""

DEVEL_DOC_LINES = """%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index
"""

FILES_HTML = "%files html -f %{_builddir}/%{framework}-qt6doc.files\n"


def parse_framework(text: str) -> str | None:
    m = re.search(r"^%global\s+framework\s+(\S+)", text, re.M)
    if m:
        return m.group(1)
    m = re.search(r"^%define\s+framework\s+(\S+)", text, re.M)
    if m:
        return m.group(1)
    return None


def bump_release(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        return f"Release:\t{int(m.group(1)) + 1}{m.group(2)}"

    return re.sub(r"^Release:\s*(\d+)(%\{\?dist\}.*)$", repl, text, count=1, flags=re.M)


def already_patched(text: str) -> bool:
    return "%{framework}-qt6doc.files" in text


def insert_html_package(text: str) -> str:
    if re.search(r"^%package\s+html\s*$", text, re.M):
        return text
    m = re.search(r"(?ms)^(%description\s+devel\n.*?)(\n^%prep|\n^%package)", text)
    if not m:
        print("no devel block anchor", file=sys.stderr)
        return text
    return text[: m.end(1)] + "\n\n" + HTML_PKG + text[m.start(2) :]


def insert_install_snippet(text: str) -> str:
    if "%{framework}-qt6doc.files" in text:
        return text
    m = re.search(r"(?m)^(%cmake_install_kf6|%cmake_install)\s*$", text)
    if not m:
        print("no cmake_install", file=sys.stderr)
        return text
    pos = m.end()
    return text[:pos] + "\n" + INSTALL_SNIPPET + text[pos:]


def ensure_devel_qt6_tags(text: str) -> str:
    if "%{_qt6_docdir}/*/*.tags" in text:
        return text
    # Stop at the next %files section or %changelog, never EOF (\\Z would eat the whole file).
    m = re.search(r"(?ms)^(%files\s+devel\n)(.*?)(?=^%files\s|^%changelog)", text)
    if not m:
        print("no %files devel", file=sys.stderr)
        return text
    body = m.group(2)
    if "%{_qt6_docdir}" in body:
        return text
    new = m.group(1) + body.rstrip() + "\n" + DEVEL_DOC_LINES + "\n"
    return text[: m.start()] + new + text[m.end() :]


def insert_files_html(text: str) -> str:
    if re.search(r"^%files\s+html\b", text, re.M):
        return text
    m = re.search(r"(?m)^%changelog\n", text)
    if not m:
        print("no changelog", file=sys.stderr)
        return text
    return text[: m.start()] + FILES_HTML + "\n" + text[m.start() :]


def prepend_changelog(text: str) -> str:
    m = re.search(r"(?m)^%changelog\n", text)
    if not m:
        return text
    entry = (
        "* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>\n"
        "- Qt6 qdoc: -html file list via find, tags/index in -devel\n\n"
    )
    return text[: m.end()] + entry + text[m.end() :]


def patch_spec(path: Path) -> bool:
    if path.name in SKIP_SPECS:
        return False
    raw = path.read_text(encoding="utf-8", errors="replace")
    if already_patched(raw):
        return False
    if parse_framework(raw) is None:
        print(f"skip {path.name}: no framework", file=sys.stderr)
        return False

    t = raw
    t = insert_html_package(t)
    t = insert_install_snippet(t)
    t = ensure_devel_qt6_tags(t)
    t = insert_files_html(t)
    t = bump_release(t)
    t = prepend_changelog(t)
    if t != raw:
        path.write_text(t, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for p in sorted(ROOT.glob("kf6-*/kf6-*.spec")):
        if patch_spec(p):
            print("patched", p.name)
            n += 1
    print("total", n, file=sys.stderr)


if __name__ == "__main__":
    main()
