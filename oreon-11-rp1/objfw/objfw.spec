%global source1_hash edd2c5b3ebd5ac33f038e346c772d1f3e7168481ae3e3f71248152a370a04860
%global source0_hash e637c32731dc07396b812c4019f34d1417a3f7aa39d450b7f27c9bcdc23b3e12
%global toolchain clang
%global _lto_cflags %nil
Name:          objfw
Version:       1.5.7
Release:        1%{?dist}
Summary:        Portable, lightweight framework for the Objective-C language
License:       LGPL-3.0-only
URL:           https://objfw.nil.im
Source0:        https://objfw.nil.im/downloads/objfw-%{version}.tar.gz
Source1:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz.sig
Source2:       gpgkey-%{name}.gpg
Requires:      libobjfw%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwtls%{_isa} = %{version}-%{release}
Requires:      libobjfwtls-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwhid%{_isa} = %{version}-%{release}
Requires:      libobjfwhid-devel%{_isa} = %{version}-%{release}
Requires:      ofarc%{_isa} = %{version}-%{release}
Requires:      ofdns%{_isa} = %{version}-%{release}
Requires:      ofhash%{_isa} = %{version}-%{release}
Requires:      ofhttp%{_isa} = %{version}-%{release}
Requires:      ofgctester%{_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  clang
BuildRequires:  doxygen
BuildRequires:  gnupg2
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gnutls)
# /oreon:deps
%description
ObjFW is a portable, lightweight framework for the Objective-C language. It
enables you to write an application in Objective-C that will run on any
platform supported by ObjFW without having to worry about differences between
operating systems or various frameworks you would otherwise need if you want to
be portable.

It supports all modern Objective-C features when using Clang, but is also
compatible with GCC ≥ 4.6 to allow maximum portability.

ObjFW also comes with its own lightweight and extremely fast Objective-C
runtime, which in real world use cases was found to be significantly faster
than both GNU's and Apple's runtime.

%package -n libobjfw
Summary:       ObjFW library
Requires:      libobjfwrt%{_isa} = %{version}-%{release}
%description -n libobjfw
The libobjfw package contains the library needed by programs using ObjFW.

%package -n libobjfw-devel
Summary:       Header files, libraries and tools for libobjfw
Requires:      clang
Requires:      libobjfw%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}
Requires:      lksctp-tools-devel%{_isa}
%description -n libobjfw-devel
The libobjfw-devel package contains the header files, libraries and tools to
develop programs using ObjFW.

%package -n libobjfwrt
Summary:       ObjFW Objective-C runtime library
%description -n libobjfwrt
The libobjfwrt package contains ObjFW's Objective-C runtime library.

%package -n libobjfwrt-devel
Summary:       Header files and libraries for libobjfwrt
Requires:      libobjfwrt%{_isa} = %{version}-%{release}
%description -n libobjfwrt-devel
The libobjfwrt-devel package contains header files and libraries for ObjFW's
Objective-C runtime library.

%package -n libobjfwtls
Summary:       TLS support for ObjFW
%description -n libobjfwtls
The libobjfwtls package contains TLS support for ObjFW.

%package -n libobjfwtls-devel
Summary:       Header files and libraries for libobjfwtls
Requires:      libobjfwtls%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}
%description -n libobjfwtls-devel
The libobjfwtls-devel package contains header files and libraries for TLS
support for ObjFW.

%package -n libobjfwhid
Summary:       HID support for ObjFW
%description -n libobjfwhid
The libobjfwhid package contains HID support for ObjFW.

%package -n libobjfwhid-devel
Summary:       Header files and libraries for libobjfwhid
Requires:      libobjfwhid%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}
%description -n libobjfwhid-devel
The libobjfwhid-devel package contains header files and libraries for HID
support for ObjFW.

%package -n ofarc
Summary:       Utility for handling ZIP, Tar, LHA and Zoo archives
%description -n ofarc
ofarc is a multi-format archive utility that allows creating, listing,
extracting and modifying ZIP, Tar, LHA and Zoo archives using ObjFW's classes
for various archive types.

%package -n ofdns
Summary:       Utility for performing DNS requests on the command line
%description -n ofdns
ofdns is an utility for performing DNS requests on the command line using
ObjFW's DNS resolver.

%package -n ofhash
Summary:       Utility to hash files with various cryptographic hash functions
%description -n ofhash
ofhash is an utility to hash files with various cryptographic hash functions
(even using different algorithms at once) using ObjFW's classes for various
cryptographic hashes.

%package -n ofhttp
Summary:       Command line downloader for HTTP(S)
%description -n ofhttp
ofhttp is a command line downloader for HTTP and HTTPS using ObjFW's
OFHTTPClient class. It supports all features one would expect from a modern
command line downloader such as resuming of downloads, using a SOCKS5 proxy, a
modern terminal-based UI, etc.

%package -n ofgctester
Summary:       Game controller tester for the terminal
%description -n ofgctester
ofgctester is a game controller tester for the terminal.

%package doc
Summary:       Documentation for ObjFW
BuildArch:     noarch
%description doc
Documentation for ObjFW.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0

%build

%configure OBJC=clang             \
           OBJCFLAGS="$CFLAGS"    \
           --with-tls=gnutls      \
           --disable-rpath        \
           --disable-silent-rules
%make_build
make docs
%install
%make_install
mkdir -p %{buildroot}%{_docdir}
cp -r docs %{buildroot}%{_docdir}/objfw
%oreon_autofiles libobjfw usr/*/lib*.so.*
%oreon_autofiles libobjfw-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libobjfwrt usr/*/lib*.so.*
%oreon_autofiles libobjfwrt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libobjfwtls usr/*/lib*.so.*
%oreon_autofiles libobjfwtls-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libobjfwhid usr/*/lib*.so.*
%oreon_autofiles libobjfwhid-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ofarc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ofdns usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ofhash usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ofhttp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ofgctester usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n libobjfw -f %{oreon_filedir}/libobjfw.list
%files -n libobjfw-devel -f %{oreon_filedir}/libobjfw-devel.list
%files -n libobjfwrt -f %{oreon_filedir}/libobjfwrt.list
%files -n libobjfwrt-devel -f %{oreon_filedir}/libobjfwrt-devel.list
%files -n libobjfwtls -f %{oreon_filedir}/libobjfwtls.list
%files -n libobjfwtls-devel -f %{oreon_filedir}/libobjfwtls-devel.list
%files -n libobjfwhid -f %{oreon_filedir}/libobjfwhid.list
%files -n libobjfwhid-devel -f %{oreon_filedir}/libobjfwhid-devel.list
%files -n ofarc -f %{oreon_filedir}/ofarc.list
%files -n ofdns -f %{oreon_filedir}/ofdns.list
%files -n ofhash -f %{oreon_filedir}/ofhash.list
%files -n ofhttp -f %{oreon_filedir}/ofhttp.list
%files -n ofgctester -f %{oreon_filedir}/ofgctester.list
%files -n objfw-doc -f %{oreon_filedir}/objfw-doc.list

%changelog

%autochangelog
