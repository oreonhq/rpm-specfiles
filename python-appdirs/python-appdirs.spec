Name:          python-appdirs
Version:       1.4.4
Release:       %autorelease
Summary:       Python module for determining platform-specific directories

# https://spdx.org/licenses/MIT.html
License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source:        %{pypi_source appdirs}

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
