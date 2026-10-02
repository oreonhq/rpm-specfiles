%global source0_hash 550a70a07defc770daffce0b2f89f7b3baec7c2d8da5670b31e5ff22b17ad789

Name: subscription-manager-rhsm-certificates
Version: 20220623
Release: 1%{?dist}
Summary: Certificates required to communicate with a Red Hat Unified Entitlement Platform
URL: https://www.candlepinproject.org/
%if 0%{?suse_version}
Group: Development/Libraries/Python
License: GPL-2.0
%else
License: GPL-2.0-only
%endif

# How to create the source tarball:
#
# git clone https://github.com/candlepin/subscription-manager-rhsm-certificates.git
# dnf install tito
# tito build --tag subscription-manager-rhsm-certificates-$VERSION-$RELEASE --tgz
Source0:        https://github.com/candlepin/subscription-manager-rhsm-certificates/archive/refs/tags/subscription-manager-rhsm-certificates-%{version}-1.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: openssl

%description
This package contains certificates required for communicating with the REST interface
of a Red Hat Unified Entitlement Platform, used for the management of system entitlements
and to receive access to content.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n subscription-manager-rhsm-certificates-subscription-manager-rhsm-certificates-%{version}-1

%build
# Nothing to do for building

%install
%make_install \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir}

%check
make check

%files
%license COPYING
%dir %{_sysconfdir}/rhsm
%dir %{_sysconfdir}/rhsm/ca
%{_sysconfdir}/rhsm/ca/*.pem

%changelog
%autochangelog
