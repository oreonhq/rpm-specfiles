%global source0_hash 091f1c14dcf13a094021334218cde363041816fa5b5037caee38719e4e6891c7
Name:           libss7
Version:        2.0.1
Release:        1%{?dist}
%global so_version 2.0
Summary:        SS7 protocol services to applications
License:        GPL-2.0-only WITH Asterisk-exception
SourceLicense:  %{license} AND GPL-2.0-or-later
URL:            https://www.asterisk.org/
%global src_base https://downloads.asterisk.org/pub/telephony/libss7/releases
Source0:        %{src_base}/%{name}-%{version}.tar.gz
Source1:        %{src_base}/libss7-%{version}.tar.gz.asc
Source2:        libss7.gpg
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  make
# /oreon:deps
%description
libss7 is a userspace library that is used for providing SS7 protocol
services to applications. It has a working MTP2, MTP3, and ISUP for ITU and
ANSI style SS7, however it was written in a manner that will easily allow
support for other various national specific variants in the future.

%package        devel
Summary:        Development files for libss7
Requires:       libss7%{?_isa} = %{version}-%{release}
%description    devel
The libss7-devel package contains libraries and header files for
developing applications that use libss7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%make_build
%install
%make_install libdir=%{_libdir}
find %{buildroot} -name '*.a' -print -delete
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libss7-devel -f %{oreon_filedir}/libss7-devel.list

%changelog

%autochangelog
