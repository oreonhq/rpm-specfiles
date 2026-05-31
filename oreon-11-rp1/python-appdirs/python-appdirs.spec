%global source0_hash 7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41

Name:          python-appdirs
Version:       1.4.4
Release:       %autorelease
Summary:       Python module for determining platform-specific directories

# https://spdx.org/licenses/MIT.html
License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source:        https://files.pythonhosted.org/packages/source/a/appdirs/appdirs-1.4.4.tar.gz
BuildArch:     noarch

BuildRequires: python3-devel

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".


%package -n python3-appdirs
Summary:        %{summary}

%description -n python3-appdirs
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n appdirs-%{version}
sed -i -e '1{\@^#!/usr/bin/env python@d}' appdirs.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files appdirs


%check
# upstream's tox.ini just wraps this command with no extra deps
# see https://github.com/ActiveState/appdirs/pull/134
# we don't use %%tox here to avoid a dependency loop: tox->platformdirs->appdirs
%{py3_test_envvars} %{python3} -m unittest discover


%files -n python3-appdirs -f %{pyproject_files}
%doc README.rst CHANGES.rst


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.4-1
- Prepare for Oreon 11 (RP1)
