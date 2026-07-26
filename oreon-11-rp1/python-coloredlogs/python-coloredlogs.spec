%global source0_hash e8161222671bb129f7936cd220c275a3cbc0a6c22313bd4483114b9526e5695f

%global srcname coloredlogs

Name:           python-%{srcname}
Version:        15.0.1
Release:        17%{?dist}
Summary:        Colored terminal output for Python's logging module

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Replace pipes.quote with shlex.quote on Python 3
# https://github.com/xolox/python-coloredlogs/pull/120
#
# Fixes:
#
# Relies on the pipes module, removed from the standard library in Python 3.13
# https://github.com/xolox/python-coloredlogs/issues/119
Patch:          https://github.com/xolox/%{name}/pull/120.patch

BuildArch:      noarch

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
Summary:        %{summary}
BuildRequires:  /usr/bin/script
BuildRequires:  python%{python3_pkgversion}-capturer >= 2.4
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-verboselogs >= 1.7

%if !0%{?rhel} || 0%{?rhel} >= 8
Suggests:       %{name}-doc = %{version}-%{release}
%endif

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build-%{python3_version} -nb html -d docs/build/doctrees docs docs/build/html
rm docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
# Some hacking to get the pth file to get processed outside
# of the build host's site dir. This sitecustomize.py needs
# to be somewhere in the path.
mkdir -p fakesite
echo "import site; site.addsitedir(site.USER_SITE)" > fakesite/sitecustomize.py

PATH=%{buildroot}%{_bindir}:$PATH \
    PYTHONPATH=$PWD/fakesite \
    PYTHONUSERBASE=%{buildroot}%{_prefix} \
    PYTHONUNBUFFERED=1 \
    py.test-%{python3_version} \
    tests.py

%files doc
%license LICENSE.txt
%doc docs/build/html

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/%{srcname}.pth
%{_bindir}/%{srcname}

%changelog
%autochangelog
