%global source0_hash 37820c93b44f211db5de5ce854f77e8a1e967b7bf9f55a241956624a5605591b

Name: python-nitrate
Version: 1.9.0
Release: 10%{?dist}

Summary: Python API for the Nitrate test case management system
License: LGPL-2.1-only

URL: https://github.com/psss/python-nitrate
Source0: %{url}/releases/download/%{version}/%{name}-%{version}.tar.bz2

# Depending on the distro, we set some defaults.
# Note that the bcond macros are named for the CLI option they create.
# "%%bcond_without" means "ENABLE by default and create a --without option"

# Fedora or RHEL 8+
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with oldreqs
%bcond_with englocale
%else
# The automatic runtime dependency generator doesn't exist yet
%bcond_without oldreqs
# The C.UTF-8 locale doesn't exist, Python defaults to C (ASCII)
%bcond_without englocale
%endif

# For older Fedora and RHEL build python2-nitrate as well
%if 0%{?fedora} > 31 || 0%{?rhel} > 7
%bcond_with python2
%else
%bcond_without python2
%endif

BuildArch: noarch
BuildRequires: git-core
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-six
%if %{with python2}
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-six
%endif

%{?python_enable_dependency_generator}

%global _description %{expand:
A Python interface to the Nitrate test case management system.
The package consists of a high-level Python module (provides
natural object interface), a low-level driver (allows to directly
access Nitrate XMLRPC API) and a command line interpreter (useful
for fast debugging and experimenting).}

%description %_description

# Python 2
%if %{with python2}
%package -n python2-nitrate
Summary: %{summary}
%{?python_provide:%python_provide python2-nitrate}
%if %{with oldreqs}
%if 0%{?rhel} > 7
Requires: python2-gssapi
Requires: python2-psycopg2
%else
Requires: python-gssapi
Requires: python-psycopg2
%endif
Requires: python2-six
%endif

%description -n python2-nitrate %_description
%endif

# Python 3
%package -n python%{python3_pkgversion}-nitrate
Summary: %{summary}
%{?python_provide:%python_provide python3-nitrate}
%if %{with oldreqs}
Requires: python%{python3_pkgversion}-gssapi
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-six
%endif
Conflicts: python2-nitrate < 1.5-3

%description -n python%{python3_pkgversion}-nitrate %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

%build
%if %{with englocale}
export LANG=en_US.utf-8
%endif
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with englocale}
export LANG=en_US.utf-8
%endif
%if %{with python2}
%py2_install
%endif
%py3_install
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 docs/*.1.gz %{buildroot}%{_mandir}/man1

# https://fedoraproject.org/wiki/Changes/Python3.12#pathfix.py_tool_will_be_removed
%py3_shebang_fix %{buildroot}%{_bindir}/nitrate

%if %{with python2}
%files -n python2-nitrate
%{python2_sitelib}/nitrate/
%{python2_sitelib}/nitrate-*.egg-info/
%license LICENSE
%endif

%files -n python%{python3_pkgversion}-nitrate
%{python3_sitelib}/nitrate/
%{python3_sitelib}/nitrate-*.egg-info/
%{_mandir}/man1/*
%{_bindir}/nitrate
%doc README.rst examples
%license LICENSE

%changelog
%autochangelog
