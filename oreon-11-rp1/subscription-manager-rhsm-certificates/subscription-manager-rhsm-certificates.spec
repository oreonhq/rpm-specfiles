%global source0_hash 9aad7c71a2eb099f94e0ff1edb668ea23c43b2953c60a519a956460eb515f1d6

Name: subscription-manager-rhsm-certificates
Version: 20220623
Release: 8%{?dist}
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
Source0:        https://github.com/candlepin/subscription-manager-rhsm-certificates/archive/%{version}/%{name}-%{version}.tar.gz#/subscription-manager-rhsm-certificates-20220623.tar.gz

BuildArch: noarch

BuildRequires: make
BuildRequires: openssl

%description
This package contains certificates required for communicating with the REST interface
of a Red Hat Unified Entitlement Platform, used for the management of system entitlements
and to receive access to content.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20220623-8
- Import
