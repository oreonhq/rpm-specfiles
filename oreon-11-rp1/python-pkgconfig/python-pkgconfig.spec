%global source0_hash 4a5a6631ce937fafac457104a40d558785a658bbdca5c49b6295bc3fd651907f

%global srcname pkgconfig

Name:           python-%{srcname}
Version:        1.6.0
Release:        %autorelease
Summary:        Python interface to the pkg-config command line tool

License:        MIT
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source}

BuildArch:      noarch

%description
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 3.9+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%package -n python3-%{srcname}
Summary:        Python3 interface to the pkg-config command line tool
Requires:       %{_bindir}/pkg-config

BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname}
pkgconfig is a Python module to interface with the pkg-config command line
tool and supports Python 3.9+.

It can be used to

* check if a package exists
* check if a package meets certain version requirements
* query CFLAGS and LDFLAGS
* parse the output to build extensions with setup.py

If pkg-config is not on the path, raises EnvironmentError.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{srcname}-%{version}
%if 0%{?rhel}
# RHEL does not have poetry-core.
# By renaming the [build-system] section we fallback to setuptools (default per PEP 517).
# This only works because there is also a setup.py file in the sdist.
test -f setup.py
sed -i 's/\[build-system\]/[ignore-this]/' pyproject.toml
%endif

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-1
- Prepare for Oreon 11 (RP1)
