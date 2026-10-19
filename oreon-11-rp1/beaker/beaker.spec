%global source0_hash 1ce331d92a6775a7470d07ae17f29035e512b86b5243a6d5022a22f1f8a42ff6
%global upstream_name beaker
%bcond docs %[ 0%{?fedora} || 0%{?rhel} < 10 ]
Name:           %{upstream_name}
Version:        29.3
Release:        1%{?dist}
Summary:        Full-stack software and hardware integration testing system
License:        GPL-2.0-or-later
URL:            https://beaker-project.org/
Source0:        https://%{name}-project.org/releases/%{name}-%{version}.tar.xz
BuildArch:      noarch
%if %{with docs}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-gssapi
BuildRequires:  python3-libxml2
BuildRequires:  python3-lxml
BuildRequires:  python3-prettytable
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-httpdomain
# /oreon:deps
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
rm -rf %{buildroot}%{_mandir}/man8/
%oreon_autofiles beaker-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles beaker-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export BKR_PY3=1
find %{buildroot} -name '__pycache__' | xargs rm -rf
%files -f %{oreon_filedir}/main.list
%files -n beaker-common -f %{oreon_filedir}/beaker-common.list
%files -n beaker-client -f %{oreon_filedir}/beaker-client.list

%changelog

%autochangelog
