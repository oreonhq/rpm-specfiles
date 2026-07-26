%global source0_hash ca4fcdfe600cc8d7d65d072917f5002334005929e48d95b78fb43e1a7a9f4acb

%global pypi_name pyaib
%global commit 73a141f28503657874dd748776b9f9c06a474604

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        22%{?dist}
Summary:        Python Framework for writing IRC Bots using gevent

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://github.com/facebook/pyaib
# The PyPI tarball doesn't include docs and examples, use the repo one instead
Source0:        %{url}/archive/%{commit}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python Async IrcBot framework (pyaib) is an easy to use framework for writing
IRC bots. pyaib uses gevent for its Asynchronous bits.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%if 0%{?fedora} < 33 || 0%{?rhel} < 9
%py_provides    python3-%{pypi_name}
%endif

%description -n python3-%{pypi_name}
Python Async IrcBot framework (pyaib) is an easy to use framework for writing
IRC bots. pyaib uses gevent for its Asynchronous bits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{commit}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Remove unneeded shebangs
sed -e "\|#!/usr/bin/env python|d" -i %{pypi_name}/*.py %{pypi_name}/*/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.markdown example
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
