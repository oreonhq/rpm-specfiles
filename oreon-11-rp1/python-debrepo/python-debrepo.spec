%global source0_hash 4b19ddbe4b0732b6b24e577b33687f5587c7e91b5bb3bc4578d7cbf33a2c74a3

%global srcname debrepo

Name:           python-%{srcname}
Version:        0.0.3
Release:        38%{?dist}
Summary:        Inspect and compare Debian repositories
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pagure.io/debrepo
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildArch:      noarch

%description
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       python3-debian
# https://bugs.debian.org/858906
Requires:       python3-chardet
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
debrepo is a library for inspecting composes of Debian repositories and
their elements, including package archives. It includes classes capable
of reading compose, repository, and package data from the filesystem,
and methods to compare the data between different versions. To this end,
the debrepodiff tool provides a command line interface for comparing
composes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%{py3_build}

%install
%py3_install
sed -i -e 's|#!/usr/bin/env python|#!%{__python3}|' \
   %{buildroot}%{_bindir}/debrepodiff

%files -n python3-%{srcname}
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_bindir}/debrepodiff

%changelog
%autochangelog
