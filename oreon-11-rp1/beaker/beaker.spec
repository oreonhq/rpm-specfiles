%global source0_hash e21ed4812c29c5e4fe8e0efc774fe99ce8bb517b615b9e0f21340d3eb7e1e8d5

%global upstream_name beaker
# No sphinxcontrib-httpdomain rpm on EPEL10
%bcond docs %[ 0%{?fedora} || 0%{?rhel} < 10 ]

Name:           %{upstream_name}
Version:        29.2
Release:        6%{?dist}
Summary:        Full-stack software and hardware integration testing system
License:        GPL-2.0-or-later
URL:            https://beaker-project.org/

# To generate git snapshot, see beaker-snapshot.sh
Source0:        https://beaker-project.org/releases/%{upstream_name}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-httpdomain
%endif

%package common
Summary:        Common components for Beaker packages
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < 0.17.0-1

%package client
Summary:        Command-line client for interacting with Beaker
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-gssapi
BuildRequires:  python3-lxml
BuildRequires:  python3-prettytable
BuildRequires:  python3-libxml2
BuildRequires: make
Requires:       python3-six
Requires:       python3-setuptools
Requires:       python3-gssapi
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-libxml2
Requires:       python3-prettytable
Requires:       python3-jinja2
# beaker-wizard was moved from rhts-devel to here in 4.52
Conflicts:      rhts-devel < 4.52

%description
Beaker is a full stack software and hardware integration testing system, with
the ability to manage a globally distributed network of test labs.

%description common
Python modules which are used by other Beaker packages.

%description client
The bkr client is a command-line tool for interacting with Beaker servers. You
can use it to submit Beaker jobs, fetch results, and perform many other tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}
%if %{without docs}
rm -rf documentation
sed -i '/SUBDIRS.*:=/s/\s*documentation\s*/ /g' Makefile
%endif
# The server relies on a great many packages which are intended to be bundled
# source, and its documentation greatly inflates the number of BR packages
# required. Until those are packaged separately, building those subpackages is
# unnnecessary
rm -r Server IntegrationTests LabController #documentation/server-api

%build
export BKR_PY3=1
make

%install
export BKR_PY3=1
DESTDIR=%{buildroot} make install

rm -rf %{buildroot}%{_datadir}/beaker-integration-tests/
rm -rf %{buildroot}%{python3_sitelib}/bkr/inttest
rm -rf %{buildroot}%{python3_sitelib}/beaker_integration_tests*
# These are for lab-controller stuff, which depends on server
rm -rf %{buildroot}%{_mandir}/man8/

%check
export BKR_PY3=1
#make check
# Running the checks generates some .pyc files - burn them!
find %{buildroot} -name '__pycache__' | xargs rm -rf

%files common
%doc README.md
%license COPYING
%dir %{python3_sitelib}/bkr/
%{python3_sitelib}/bkr/__init__.py*
%{python3_sitelib}/bkr/common/
%{python3_sitelib}/bkr/log.py*
%{python3_sitelib}/%{name}_common-%{version}-py%{python3_version}.egg-info/

%files client
%dir %{_sysconfdir}/%{name}
%doc Client/client.conf.example
%{python3_sitelib}/bkr/client/
%{python3_sitelib}/%{name}_client-%{version}-py%{python3_version}-nspkg.pth
%{python3_sitelib}/%{name}_client-%{version}-py%{python3_version}.egg-info/
%{_bindir}/%{name}-wizard
%{_bindir}/bkr
%if %{with docs}
%{_mandir}/man1/beaker-wizard.1.gz
%{_mandir}/man1/bkr.1.gz
%{_mandir}/man1/bkr-*.1.gz
%endif
%{_datadir}/bash-completion

%changelog
%autochangelog
