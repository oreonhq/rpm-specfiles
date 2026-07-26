%global source0_hash 4f0961c15b54617d61bb03e722a10f2b1e589ece075f1c1bdf23931c43e0ccb0

%if 0%{?fedora}
# rhel/epel has no flexmock, pytest-capturelog
%global with_check 0
%endif

%global commit 7980ce59a95e2e2fac64f0d3aeec8cdcef297f4c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# set to 0 to create a normal release
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
Version:        1.15.0
%if "x%{postrelease}" != "x0"
Release:        %{release}.%{postrelease}.git.%{shortcommit}%{?dist}
%else
Release:        %{release}%{?dist}
%endif

Summary:        Python command line client for OpenShift Build Service
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/projectatomic/osbs-client
Source0:        https://github.com/projectatomic/osbs-client/archive/%{commit}/osbs-client-%{commit}.tar.gz

BuildArch:      noarch

Requires:       python3-osbs-client = %{version}-%{release}
Requires:       python3-requests
Requires:       python3-requests-kerberos

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?with_check}
BuildRequires:  git-core
BuildRequires:  python3-dateutil
BuildRequires:  python3-pytest
BuildRequires:  python3-flexmock
BuildRequires:  python3-six
BuildRequires:  python3-dockerfile-parse
BuildRequires:  python3-jsonschema
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-requests
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3-PyYAML
%endif # with_check

Provides:       osbs = %{version}-%{release}
Obsoletes:      osbs < %{osbs_obsolete_vr}

%description
It is able to query OpenShift v3 for various stuff related to building images.
It can initiate builds, list builds, get info about builds, get build logs...
This package contains osbs command line client.

%package -n python3-osbs-client
Summary:        Python 3 module for OpenShift Build Service
# Automatically converted from old format: BSD - review is highly recommended.
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

%if 0%{?with_check}
%check
py.test-3 -vv tests
%endif # with_check

%files
%doc README.md
%{_bindir}/osbs

%files -n python3-osbs-client
%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE
%{_bindir}/osbs
%{python3_sitelib}/osbs*
%dir %{_datadir}/osbs
%{_datadir}/osbs/*.json

%changelog
%autochangelog
