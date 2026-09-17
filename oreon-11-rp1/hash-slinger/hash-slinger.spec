%global source0_hash 5a03bfeba39134773e0a98b1607521b5b70fba58173a20deb7e032cc7e949bcb

%bcond_with man

Summary: Generate and verify various DNS records such as SSHFP, TLSA and OPENPGPKEY
Name: hash-slinger
Version: 3.5
Release: 1%{?dist}
License: GPL-2.0-or-later
Url:  https://github.com/letoams/%{name}/
Source:  %{url}archive/%{version}/%{name}-%{version}.tar.gz
%if %{with man}
# Only to regenerate the man page, which is shipped per default
Buildrequires: xmlto
%endif
BuildRequires: python3-devel, make
Requires: python3 >= 3.4
Requires: python3-dns, python3-unbound
Requires: openssh-clients >= 4, python3-gnupg >= 0.3.7
Requires: python3-cryptography
BuildArch: noarch
Obsoletes: sshfp < 2.0
Provides: sshfp  = %{version}

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

%autosetup -p1

%build
%make_build all

%install
%make_install

%files 
%license COPYING
%doc BUGS CHANGES README
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
%autochangelog
