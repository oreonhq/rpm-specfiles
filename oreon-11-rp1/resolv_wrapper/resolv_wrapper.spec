%global source0_hash none

%global source2_key_fpr 8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D

Name:           resolv_wrapper
Version:        1.1.8
Release:        11%{?dist}

Summary:        A wrapper for dns name resolving or dns faking
License:        BSD-3-Clause
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        resolv_wrapper.keyring

Patch0:         resolv_wrapper-fix-cmocka-1.1.6+-support.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  cmake
BuildRequires:  libcmocka-devel
BuildRequires:  socket_wrapper

Recommends:     cmake
Recommends:     pkgconfig

%description
It is likely that if you have a server/client architecture, you need to do DNS
queries or a third party library, like Kerberos needs to be able to do queries.
In the case of Kerberos the client needs to look the address of the KDC up via a
SRV record. resolv_wrapper is able to either redirect all DNS queries to your
DNS server implementation, or fake DNS replies!

To use it set the following environment variables:

LD_PRELOAD=libresolv_wrapper.so
RESOLV_WRAPPER_CONF=./my_resolv.conf

This package doesn't have a devel package because this project is for
development/testing.

%prep
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake \
  -DUNIT_TESTING=ON

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%check
%ctest

LD_PRELOAD=%{__cmake_builddir}/src/libpam_wrapper.so bash -c '>/dev/null'

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libresolv_wrapper.so*
%dir %{_libdir}/cmake/resolv_wrapper
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config-version.cmake
%{_libdir}/cmake/resolv_wrapper/resolv_wrapper-config.cmake
%{_libdir}/pkgconfig/resolv_wrapper.pc
%{_mandir}/man1/resolv_wrapper.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.8-11
- Prepare for Oreon 11 (RP1)
