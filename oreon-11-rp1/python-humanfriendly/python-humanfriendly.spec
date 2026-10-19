%global source0_hash a7f6ee6aa93933ffdf716a44163a8b1d17e8c95b3badb25efa37d562b2b93393
%bcond bootstrap 0
%bcond tests %{without bootstrap}
%global srcname humanfriendly
Name:           python-%{srcname}
Version:        10.0
Release:        1%{?dist}
Summary:        Human friendly output for text interfaces using Python
License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Patch0:         %{name}-10.0-mock.patch
Patch1:         https://github.com/xolox/%{name}/pull/75.patch
Patch2:         https://github.com/xolox/%{name}/pull/65.patch
# oreon:deps
BuildRequires:  python3-capturer
BuildRequires:  python3-coloredlogs
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.

%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx
%description doc
HTML documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Human friendly output for text interfaces using Python
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-capturer >= 2.1
BuildRequires:  python%{python3_pkgversion}-coloredlogs >= 2.0
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%description -n python%{python3_pkgversion}-%{srcname}
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
rm build/lib/%{srcname}/tests.py
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?with_tests}
PYTHONUNBUFFERED=1 py.test-%{python3_version} %{srcname}/tests.py
%else
%py3_check_import %{srcname}
%endif
%files -f %{oreon_filedir}/main.list
%files -n python-humanfriendly-doc -f %{oreon_filedir}/python-humanfriendly-doc.list
%files -n python3-humanfriendly -f %{oreon_filedir}/python3-humanfriendly.list

%changelog

%autochangelog
