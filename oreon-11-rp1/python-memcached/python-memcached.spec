%global source0_hash 2877f0885ade0c4c6871c863914838d23c955621f1a9f56a9b941dd1facb250a

Name:           python-memcached
Version:        1.62
Release:        3%{?dist}
Summary:        A Python memcached client library

# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            https://github.com/linsomniac/python-memcached
Source0:        https://github.com/linsomniac/python-memcached/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
# Required for running test suite
BuildRequires:  %{_bindir}/memcached
BuildRequires:  python3-pytest

%global _description\
This software is a 100% Python interface to the memcached memory cache\
daemon.  It is the client side software which allows storing values in one\
or more, possibly remote, memcached servers.  Search google for memcached\
for more information.

%description %_description

%package -n python3-memcached
Summary: %summary
%{?python_provide:%python_provide python3-memcached}

%description -n python3-memcached %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
pidfile=$(mktemp)
memcached -d -P $pidfile

%pytest

kill $(cat $pidfile)

%files -n python3-memcached
%doc ChangeLog README.md SECURITY.md
%attr(755,root,root) %{python3_sitelib}/memcache.py
%license PSF.LICENSE
%{python3_sitelib}/memcache.py
%{python3_sitelib}/__pycache__/memcache.*
%{python3_sitelib}/*.dist-info

%changelog
%autochangelog
