%global source2_hash 64619d3c1a2b68da837014b2ab02a049ed2c69aaebfa10a20a4f29dab003ecb8
%global source1_hash f5618c9356a1d5a8059d6cf64015d86547f06b2b8b1f542fbbaf381a736c8075
%global source0_hash d9ec76cbe34db98eec3539fe2c899d26b0c837cb3eb466a56b0f109cabf658f7
%?mingw_package_header
Name:           mingw-libssh2
Version:        1.11.1
Release:        3%{?dist}
Summary:        MinGW Windows library implementation of the SSH2 protocol
License:        BSD-3-Clause
URL:            https://www.libssh2.org/
Source0:        https://libssh2.org/download/libssh2-%{version}.tar.gz
Source1:        https://libssh2.org/download/libssh2-%{version}.tar.gz.asc
Source2:        https://daniel.haxx.se/mykey.asc
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

# Win32
%package -n mingw32-libssh2
Summary:        MinGW Windows library implementation of the SSH2 protocol
Requires:       pkgconfig
%description -n mingw32-libssh2
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n mingw32-libssh2-static
Summary:        Static version of the MinGW Windows SSH2 library
Requires:       mingw32-libssh2 = %{version}-%{release}
%description -n mingw32-libssh2-static
Static version of the MinGW Windows SSH2 library.

# Win64
%package -n mingw64-libssh2
Summary:        MinGW Windows library implementation of the SSH2 protocol
Requires:       pkgconfig
%description -n mingw64-libssh2
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package -n mingw64-libssh2-static
Summary:        Static version of the MinGW Windows SSH2 library
Requires:       mingw64-libssh2 = %{version}-%{release}
%description -n mingw64-libssh2-static
Static version of the MinGW Windows SSH2 library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n libssh2-%{version}

%build

%mingw_configure --disable-silent-rules --enable-static --enable-shared
%mingw_make %{?_smp_mflags}
%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man3
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man3
%oreon_autofiles mingw32-libssh2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libssh2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libssh2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libssh2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libssh2 -f %{oreon_filedir}/mingw32-libssh2.list
%files -n mingw32-libssh2-static -f %{oreon_filedir}/mingw32-libssh2-static.list
%files -n mingw64-libssh2 -f %{oreon_filedir}/mingw64-libssh2.list
%files -n mingw64-libssh2-static -f %{oreon_filedir}/mingw64-libssh2-static.list

%changelog

%autochangelog
