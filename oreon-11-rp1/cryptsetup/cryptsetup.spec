%global source0_hash 3acfa685f2dd7fcc832e0b77bc7093aa7da554a51ce8dafbb4138eaa854eee35
Summary:        Utility for setting up encrypted disks
Name: cryptsetup
Version: 2.8.8
Release:        1%{?dist}
License: GPL-2.0-or-later WITH cryptsetup-OpenSSL-exception AND LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception
URL: https://gitlab.com/cryptsetup/cryptsetup
Requires: cryptsetup-libs = %{version}-%{release}
Requires: libpwquality >= 1.2.0
Obsoletes: %{name}-reencrypt <= %{version}
Provides: %{name}-reencrypt = %{version}
%global upstream_version %{version_no_tilde}
Source0:        https://www.kernel.org/pub/linux/utils/%{name}/v2.8/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  device-mapper-devel
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  json-c-devel
BuildRequires:  libblkid-devel
BuildRequires:  libpwquality-devel
BuildRequires:  libssh-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
# /oreon:deps
%description
The cryptsetup package contains a utility for setting up
disk encryption using dm-crypt kernel module.

%package devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Summary: Headers and libraries for using encrypted file systems
%description devel
The cryptsetup-devel package contains libraries and header files
used for writing code that makes use of disk encryption.

%package libs
Summary: Cryptsetup shared library
%description libs
This package contains the cryptsetup shared library, libcryptsetup.

%package ssh-token
Summary: Cryptsetup LUKS2 SSH token
Requires: cryptsetup-libs = %{version}-%{release}
%description ssh-token
This package contains the LUKS2 SSH token.

%package -n veritysetup
Summary: A utility for setting up dm-verity volumes
Requires: cryptsetup-libs = %{version}-%{release}
%description -n veritysetup
The veritysetup package contains a utility for setting up
disk verification using dm-verity kernel module.

%package -n integritysetup
Summary: A utility for setting up dm-integrity volumes
Requires: cryptsetup-libs = %{version}-%{release}
%description -n integritysetup
The integritysetup package contains a utility for setting up
disk integrity protection using dm-integrity kernel module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n cryptsetup-%{upstream_version} -p 1

%build

rm -f man/*.8
./autogen.sh
%configure --enable-fips --enable-pwquality --enable-asciidoc --enable-internal-sse-argon2
%make_build
%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/%{name}/*.la
%find_lang cryptsetup
%ldconfig_scriptlets -n cryptsetup-libs
%oreon_autofiles cryptsetup-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cryptsetup-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cryptsetup-ssh-token usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles veritysetup usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles integritysetup usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cryptsetup-devel -f %{oreon_filedir}/cryptsetup-devel.list
%files -n cryptsetup-libs -f %{oreon_filedir}/cryptsetup-libs.list
%files -n cryptsetup-ssh-token -f %{oreon_filedir}/cryptsetup-ssh-token.list
%files -n veritysetup -f %{oreon_filedir}/veritysetup.list
%files -n integritysetup -f %{oreon_filedir}/integritysetup.list

%changelog

%autochangelog
