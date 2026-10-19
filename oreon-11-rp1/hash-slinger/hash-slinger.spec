%global source0_hash fa920ec229994e3d84399c3ef473d94f0dc6af36f11a4775d1e1b334b771a887
%bcond_with man
Summary:        Generate and verify various DNS records such as SSHFP, TLSA and OPENPGPKEY
Name: hash-slinger
Version: 3.6
Release:        1%{?dist}
License: GPL-2.0-or-later
Url:  https://github.com/letoams/%{name}/
Source0:        https://github.com/letoams/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with man}
%endif
Requires: python3 >= 3.4
Requires: python3-dns, python3-unbound
Requires: openssh-clients >= 4, python3-gnupg >= 0.3.7
Requires: python3-cryptography
BuildArch: noarch
Obsoletes: sshfp < 2.0
Provides: sshfp  = %{version}
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
# /oreon:deps
%description
This package contains various tools to generate special DNS records:

sshfp       Generate RFC-4255 SSHFP DNS records from known_hosts files
            or ssh-keyscan
tlsa        Generate RFC-6698  TLSA DNS records via TLS
openpgpkey  Generate RFC-7929 DNS records from OpenPGP
            keyrings
ipseckey    Generate RFC-4025 IPSECKEY DNS records on Libreswan
            IPsec servers

This package has incorporated the old 'sshfp' and 'swede' commands/packages

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build all
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
