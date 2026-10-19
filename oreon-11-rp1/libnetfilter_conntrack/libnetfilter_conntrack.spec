%global source1_hash 8fb7bfa4d9e0104249f331dddbd975930740cc7b2e59a2d760a0966aa7ce0abb
%global source0_hash 769d3eaf57fa4fbdb05dd12873b6cb9a5be7844d8937e222b647381d44284820
%global source2_key_fpr 8C5F7146A1757A65E2422A94D70D1A666ACF2B21
Name:           libnetfilter_conntrack
Version:        1.1.1
Release:        1%{?dist}
Summary:        Netfilter conntrack userspace library
License:        GPL-2.0-or-later
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz
Source1:        http://netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  libmnl-devel
BuildRequires:  libnfnetlink-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
libnetfilter_conntrack is a userspace library providing a programming 
interface (API) to the in-kernel connection tracking state table.

%package        devel
Summary:        Netfilter conntrack userspace library
Requires:       %{name} = %{version}-%{release}, libnfnetlink-devel >= 1.0.1
Requires:       kernel-headers
%description    devel
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

%prep

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build

autoreconf -vi
%configure --disable-static --disable-rpath
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnetfilter_conntrack-devel -f %{oreon_filedir}/libnetfilter_conntrack-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-1
- Prepare for Oreon 11 (RP1)
