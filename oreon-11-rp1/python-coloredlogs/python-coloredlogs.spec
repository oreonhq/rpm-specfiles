%global source0_hash e8161222671bb129f7936cd220c275a3cbc0a6c22313bd4483114b9526e5695f
%global srcname coloredlogs
Name:           python-%{srcname}
Version:        15.0.1
Release:        1%{?dist}
Summary:        Colored terminal output for Python's logging module
License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          https://github.com/xolox/%{name}/pull/120.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-coloredlogs = %{version}-%{release}
# /oreon:deps
%description
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal.

%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python%{python3_pkgversion}-sphinx
%description doc
HTML documentation for the '%{srcname}' Python module.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Colored terminal output for Python's logging module
BuildRequires:  /usr/bin/script
BuildRequires:  python%{python3_pkgversion}-capturer >= 2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-verboselogs >= 1.7
%description -n python%{python3_pkgversion}-%{srcname}
The coloredlogs package enables colored terminal output for Python's logging
module. The ColoredFormatter class inherits from logging.Formatter and uses
ANSI escape sequences to render your logging messages in color. It uses only
standard colors so it should work on any UNIX terminal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Don't install tests.py
mv %{srcname}/tests.py ./tests.py

%build

%pyproject_wheel
sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo
%install
%pyproject_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/coloredlogs* usr/lib64/python3*/site-packages/coloredlogs* usr/bin/*

%check

mkdir -p fakesite
echo "import site; site.addsitedir(site.USER_SITE)" > fakesite/sitecustomize.py
PATH=%{buildroot}%{_bindir}:$PATH \
    PYTHONPATH=$PWD/fakesite \
    PYTHONUSERBASE=%{buildroot}%{_prefix} \
    PYTHONUNBUFFERED=1 \
    py.test-%{python3_version} \
    tests.py
%files
%files -n python-coloredlogs-doc -f %{oreon_filedir}/python-coloredlogs-doc.list
%files -n python3-coloredlogs -f %{oreon_filedir}/python3-coloredlogs.list

%changelog

%autochangelog
