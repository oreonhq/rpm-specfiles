Name:          python-appdirs
Version:       1.4.4
Release:       %autorelease
Summary:       Python module for determining platform-specific directories

# https://spdx.org/licenses/MIT.html
License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source:        %{pypi_source appdirs}
# oreon url source checksums begin
%global source0_sha256 7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41
%global source0_file appdirs-1.4.4.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/appdirs-1.4.4.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7d5d0167b2b1ba821647616af46a749d1c653740dd0d2415100fe26e27afdf41" || { echo "oreon: Source0 SHA256 mismatch for appdirs-1.4.4.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
