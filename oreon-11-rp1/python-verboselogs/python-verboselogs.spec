%global source0_hash bdf765f43f2cd44ef42d06e8b9d141e8fa0bd1843a267bd9f02beba8efe04232
%global srcname verboselogs
Name:           python-%{srcname}
Version:        1.7
Release:        1%{?dist}
Summary:        Verbose logging level for Python's logging module
License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-1.7-mock.patch
Patch1:         %{name}-1.7-sphinx-theme.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
# /oreon:deps
%description
The verboselogs package extends Python's logging module to add the log levels
NOTICE, SPAM, SUCCESS and VERBOSE:

- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.
- The SUCCESS level sits between the predefined WARNING and ERROR levels.
- The VERBOSE level sits between the predefined INFO and DEBUG levels.

The code to do this is simple and short, but I still don't want to copy/paste it
to every project I'm working on, hence this package.

%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx
%description doc
HTML documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Verbose logging level for Python's logging module
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%description -n python%{python3_pkgversion}-%{srcname}
The verboselogs package extends Python's logging module to add the log levels
NOTICE, SPAM, SUCCESS and VERBOSE:

- The NOTICE level sits between the predefined WARNING and INFO levels.
- The SPAM level sits between the predefined DEBUG and NOTSET levels.
- The SUCCESS level sits between the predefined WARNING and ERROR levels.
- The VERBOSE level sits between the predefined INFO and DEBUG levels.

The code to do this is simple and short, but I still don't want to copy/paste it
to every project I'm working on, hence this package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%py3_build
rm build/lib/%{srcname}/{pylint,tests}.py
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONUNBUFFERED=1 py.test-%{python3_version} %{srcname}/tests.py \
  -k 'not test_pylint_plugin'
%files -f %{oreon_filedir}/main.list
%files -n python-verboselogs-doc -f %{oreon_filedir}/python-verboselogs-doc.list
%files -n python3-verboselogs -f %{oreon_filedir}/python3-verboselogs.list

%changelog

%autochangelog
