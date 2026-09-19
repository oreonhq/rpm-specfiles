%global source0_hash 27bf9bd1bbc1e20f83633208620d56de50f14185055e49504f4f5e94e94aff94

# Created by pyp2rpm-1.0.1
%global pypi_name pymemcache

Name:           python-%{pypi_name}
Version:        4.0.0
Release:        13%{?dist}
Summary:        A comprehensive, fast, pure Python memcached client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/Pinterest/pymemcache
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Skip-unit-tests-resolving-domain-names.patch
Patch0002:      0002-Unpin-test-requirements-packages.patch
BuildArch:      noarch

%global _description\
pymemcache supports the following features:\
\
* Complete implementation of the memcached text protocol.\
* Configurable timeouts for socket connect and send/recv calls.\
* Access to the "noreply" flag, which can significantly increase the speed of\
  writes.\
* Flexible, simple approach to serialization and deserialization.\
* The (optional) ability to treat network and memcached errors as cache misses.

%description %_description

%package -n python3-%{pypi_name}
Summary:        A comprehensive, fast, pure Python memcached client
BuildRequires:  git-core
%{?python_enable_dependency_generator}

%generate_buildrequires
%pyproject_buildrequires -t

%description -n python3-%{pypi_name}
pymemcache supports the following features:

* Complete implementation of the memcached text protocol.
* Configurable timeouts for socket connect and send/recv calls.
* Access to the "noreply" flag, which can significantly increase the speed of
  writes.
* Flexible, simple approach to serialization and deserialization.
* The (optional) ability to treat network and memcached errors as cache misses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
py.test-3 ./pymemcache/test/

%files -n python3-%{pypi_name}
%doc README.rst LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
