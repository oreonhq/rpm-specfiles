%global source1_hash e1824361a2047f0770e503aa96bd3c9a53bcb9a9afb9f99d65c006d93ef1fb09
%global source0_hash dc79ab072779be4403b45b60cd044dd13780d4bb9675d27abf1932ada7c8a88d
%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D
Name:           nss_wrapper
Version:        1.1.16
Release:        1%{?dist}
License:        BSD-3-Clause
Summary:        A wrapper for the user, group and hosts NSS API
Url:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        nss_wrapper.keyring
Patch0:         nwrap-fix-tests.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libcmocka-devel
BuildRequires:  perl-generators
# /oreon:deps
%description
There are projects which provide daemons needing to be able to create, modify
and delete Unix users. Or just switch user ids to interact with the system e.g.
a user space file server. To be able to test that you need the privilege to
modify the passwd and groups file. With nss_wrapper it is possible to define
your own passwd and groups file which will be used by software to act correctly
while under test.

If you have a client and server under test they normally use functions to
resolve network names to addresses (dns) or vice versa. The nss_wrappers allow
you to create a hosts file to setup name resolution for the addresses you use
with socket_wrapper.

To use it set the following environment variables:

LD_PRELOAD=libuid_wrapper.so
NSS_WRAPPER_PASSWD=/path/to/passwd
NSS_WRAPPER_GROUP=/path/to/group
NSS_WRAPPER_HOSTS=/path/to/host

This package doesn't have a devel package cause this project is for
development/testing.

%package libs
Summary: nss_library shared library only
%description libs
The %{name}-libs package provides only the shared library.
For a minimal footprint, install just this package.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

%cmake \
  -DUNIT_TESTING=ON
%cmake_build
%install
%cmake_install
sed -i '1 s|/usr/bin/env\ perl|/usr/bin/perl|' %{buildroot}%{_bindir}/nss_wrapper.pl
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n nss_wrapper-libs -f %{oreon_filedir}/nss_wrapper-libs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.16-1
- Prepare for Oreon 11 (RP1)
