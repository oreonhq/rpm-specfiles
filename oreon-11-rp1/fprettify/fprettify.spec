%global source0_hash 052da19a9080a6641d3202e10572cf3d978e6bcc0e7db29c1eb8ba724e89adc7

Name:           fprettify
Version:        0.3.7
Release:        19%{?dist}
Summary:        Auto-formatter for modern Fortran source code
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/pseewald/fprettify
Source0:        https://github.com/pseewald/fprettify/archive/refs/tags/v%{version}/fprettify-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(configargparse)
BuildRequires:  python3dist(setuptools)

Requires:       python3-fprettify = %{version}-%{release}

# Patch out use of /usr/bin/env python
Patch0:         fprettify-0.3.7-pyenv.patch

%description
fprettify is an auto-formatter written in Python to impose strict
whitespace formatting for modern Fortran code.

%package -n     python3-fprettify
Summary:        Python library for fprettify

Requires:       python3dist(configargparse)
Requires:       python3dist(setuptools)

%description -n python3-fprettify
fprettify is an auto-formatter written in Python to impose strict
whitespace formatting for modern Fortran code.

This package contains the Python library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fprettify-%{version}
%patch -P0 -p1 -b .pyenv
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{python3} run_tests.py

%files
%{_bindir}/fprettify

%files -n python3-fprettify
%license LICENSE
%doc README.md
%{python3_sitelib}/fprettify/
%{python3_sitelib}/fprettify-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
