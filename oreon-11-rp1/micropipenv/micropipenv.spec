%global source0_hash e5abd5af3a49eeb7e886f2ff9b5525717642ac2fb202b214b63ff5e990a779b9

# some test dependencies are unwanted in RHEL
%if 0%{?rhel}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           micropipenv
Version:        1.10.0
Release:        %autorelease
Summary:        A simple wrapper around pip to support Pipenv and Poetry files

License:        LGPL-3.0-or-later
URL:            https://github.com/thoth-station/%{name}
Source0:        https://github.com/thoth-station/micropipenv/archive/refs/tags/v1.10.0.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%py_provides    python3-%{name}

Recommends:     micropipenv+toml

%description
A lightweight wrapper for pip to support Pipenv and Poetry lock files or
converting them to pip-tools compatible output.

%pyproject_extras_subpkg -n %{name} toml

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
# Remove shebang line from the module
sed -i '1{\@^#!/usr/bin/env python@d}' %{name}.py
# Remove virtualenv requirement from tox.ini
sed -i '/requires = virtualenv/d' tox.ini
# Do not install wheel in testing venvs
sed -i 's/[^ ]*wheel==0.45.1.*/pass/' tests/conftest.py

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-t} -x toml

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}

%check
%if %{with tests}
# skipped tests requires internet or checks pip version
%pytest -m "not online" -k "not test_check_pip_version and not test_install_invalid_toml_file"
%else
%pyproject_check_import
%endif

%files -f %pyproject_files
%doc README.rst
%{_bindir}/micropipenv

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.0-1
- Prepare for Oreon 11 (RP1)
