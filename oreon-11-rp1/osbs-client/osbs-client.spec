%global source0_hash 4f0961c15b54617d61bb03e722a10f2b1e589ece075f1c1bdf23931c43e0ccb0
%global commit 7980ce59a95e2e2fac64f0d3aeec8cdcef297f4c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global dev_release 0
%if 0%{?dev_release}
%global postrelease dev
%global release 23
%else
%global postrelease 0
%global release 6
%endif
%global osbs_obsolete_vr 0.14-2
Name:           osbs-client
Version:        2.8.1
%if "x%{postrelease}" != "x0"
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Summary:        Python command line client for OpenShift Build Service
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/projectatomic/osbs-client
Source0:        https://github.com/projectatomic/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch
Requires:       python3-osbs-client = %{version}-%{release}
Requires:       python3-requests
Requires:       python3-requests-kerberos
%if 0%{?with_check}
%endif # with_check
Provides:       osbs = %{version}-%{release}
Obsoletes:      osbs < %{osbs_obsolete_vr}
# oreon:deps
BuildRequires:  git-core
BuildRequires:  python3-PyYAML
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-dockerfile-parse
BuildRequires:  python3-flexmock
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-requests
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
# /oreon:deps
%description
It is able to query OpenShift v3 for various stuff related to building images.
It can initiate builds, list builds, get info about builds, get build logs...
This package contains osbs command line client.

%package -n python3-osbs-client
Summary:        Python 3 module for OpenShift Build Service
License:        LicenseRef-Callaway-BSD
Requires:       python3-dockerfile-parse
Requires:       python3-jsonschema
Requires:       python3-requests
Requires:       python3-requests-kerberos
Requires:       python3-dateutil
Requires:       python3-setuptools
Requires:       python3-six
Requires:       krb5-workstation
Requires:       python3-PyYAML
Requires:       git-core
Provides:       python3-osbs = %{version}-%{release}
Obsoletes:      python3-osbs < %{osbs_obsolete_vr}
%{?python_provide:%python_provide python3-osbs-client}
%description -n python3-osbs-client
It is able to query OpenShift v3 for various stuff related to building images.
It can initiate builds, list builds, get info about builds, get build logs...
This package contains osbs Python 3 bindings.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

# Remove this test, it tries to hit httpbin.org which fails the build in koji
rm -f tests/test_http.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-osbs-client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?with_check}
%check

py.test-3 -vv tests
%endif # with_check
%files -f %{oreon_filedir}/main.list
%files -n python3-osbs-client -f %{oreon_filedir}/python3-osbs-client.list

%changelog

%autochangelog
