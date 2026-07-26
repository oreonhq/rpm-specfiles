%global source0_hash 56d2c45cdaf3a51e0946e5701dfc76d38262d42c47d077680c2b56210acfd485

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif
%global pypi_name murano-pkg-check
%global library muranopkgcheck

%global with_docs 0

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        40%{?dist}
Summary:        Murano package validator tool

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://docs.openstack.org/developer/murano/
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0001:      0001-Use-unittest.mock-instead-of-third-party-mock.patch
Patch0002:      0002-Fix-py38-ut.patch
Patch0003:      0003-Drop-lower-constraints.txt-and-its-testing.patch
BuildArch:      noarch

BuildRequires:  git

%description
Murano package validator tool

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        Murano package validator tool
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-coverage
BuildRequires:  python2-subunit
BuildRequires:  python2-sphinx
BuildRequires:  python2-oslotest
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-reno
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
# Required for tests
BuildRequires:  python2-semantic_version
BuildRequires:  python2-oslo-i18n
BuildRequires:  python2-yaql
BuildRequires:  python2-stevedore
Requires:       python2-pbr >= 1.6
Requires:       python2-pyyaml >= 3.10
Requires:       python2-yaql >= 1.1.0
Requires:       python2-six >= 1.9.0
Requires:       python2-stevedore >= 1.16.0
Requires:       python2-semantic_version >= 2.3.1
Requires:       python2-oslo-i18n >= 2.1.0
Requires:       python2-setuptools

%description -n python2-%{pypi_name}
Murano package validator tool
%endif

%if 0%{?with_docs}
%package -n python-%{pypi_name}-doc
Summary:        murano-pkg-check documentation
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery) = 3.1.0
Provides:       bundled(js-searchtools)
Provides:       bundled(js-underscore) = 1.3.1
Provides:       bundled(js-websupport)

%description -n python-%{pypi_name}-doc
Documentation for murano-pkg-check
%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        Murano package validator tool
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-coverage
BuildRequires:  python3-subunit
BuildRequires:  python3-sphinx
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-reno
BuildRequires:  python3-setuptools
# Required for tests
BuildRequires:  python3-semantic_version
BuildRequires:  python3-oslo-i18n
BuildRequires:  python3-yaql
BuildRequires:  python3-stevedore
Requires:       python3-pbr >= 1.6
Requires:       python3-PyYAML >= 3.10
Requires:       python3-yaql >= 1.1.0
Requires:       python3-six >= 1.9.0
Requires:       python3-stevedore >= 1.16.0
Requires:       python3-semantic_version >= 2.3.1
Requires:       python3-oslo-i18n >= 2.1.0
Requires:       python3-setuptools

%description -n python3-%{pypi_name}
Murano package validator tool
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -S git
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Let's handle requirements from the RPM side
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%if 0%{?with_docs}
%if %{with python3}
# generate html docs
sphinx-build-3 -b html doc/source doc/build/html
# generate man page
sphinx-build-3 -b man doc/source doc/build/man
%else
# generate html docs
sphinx-build -b html doc/source doc/build/html
# generate man page
sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
%endif
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if %{with python3}
%py3_install
mv %{buildroot}/%{_bindir}/murano-pkg-check %{buildroot}/%{_bindir}/murano-pkg-check-3
ln -s ./murano-pkg-check-3 %{buildroot}%{_bindir}/murano-pkg-check
%endif

%if %{with python2}
%py2_install
mv %{buildroot}/%{_bindir}/murano-pkg-check %{buildroot}/%{_bindir}/murano-pkg-check-2
ln -s ./murano-pkg-check-2 %{buildroot}%{_bindir}/murano-pkg-check
%endif

%if 0%{?with_docs}
install -p -D -m 644 doc/build/man/murano-pkg-check.1 %{buildroot}%{_mandir}/man1/murano-pkg-check.1
%endif

%check
%if %{with python2}
PYTHON=python2 %{__python2} setup.py test
%endif
%if %{with python3}
rm -rf .testrepository
PYTHON=python3 %{__python3} setup.py test
%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/murano-pkg-check
%{_bindir}/murano-pkg-check-2
%{_mandir}/man1/murano-pkg-check.1.gz
%{python2_sitelib}/%{library}
%exclude %{python2_sitelib}/%{library}/tests
%{python2_sitelib}/murano_pkg_check-*.egg-info
%endif

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc doc/build/html
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/murano-pkg-check-3
%{_bindir}/murano-pkg-check
%if 0%{?with_docs}
%{_mandir}/man1/murano-pkg-check.1.gz
%endif
%{python3_sitelib}/%{library}
%exclude %{python3_sitelib}/%{library}/tests
%{python3_sitelib}/murano_pkg_check-*.egg-info
%endif

%changelog
%autochangelog
