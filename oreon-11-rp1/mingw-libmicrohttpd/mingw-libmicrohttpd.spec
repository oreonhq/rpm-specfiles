%global source0_hash 04bfe8ef75db7d629a33de767599765cecadc56274a39822d5d081030d577685
%{?mingw_package_header}
Name:           mingw-libmicrohttpd
Version:        1.0.10
Release:        1%{?dist}
Summary:        MinGW package for libmicrohttpd
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw64-libgcrypt
# /oreon:deps
%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.

# Mingw32
%package -n mingw32-libmicrohttpd
Summary:        MinGW package for libmicrohttpd
%description -n mingw32-libmicrohttpd
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.

%package -n mingw32-libmicrohttpd-static
Summary:        Static version of the libmicrohttpd library
Requires:       mingw32-libmicrohttpd = %{version}-%{release}
%description -n mingw32-libmicrohttpd-static
Static version of the libmicrohttpd library.

# Mingw64
%package -n mingw64-libmicrohttpd
Summary:        MinGW package for libmicrohttpd
%description -n mingw64-libmicrohttpd
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.

%package -n mingw64-libmicrohttpd-static
Summary:        Static version of the libmicrohttpd library
Requires:       mingw64-libmicrohttpd = %{version}-%{release}
%description -n mingw64-libmicrohttpd-static
Static version of the libmicrohttpd library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libmicrohttpd-%{version}

%build

%mingw_configure --with-gnutls --enable-spdy=no --enable-https=yes
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/libmicrospdy.pc
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/libmicrospdy.pc
%oreon_autofiles mingw32-libmicrohttpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libmicrohttpd-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libmicrohttpd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libmicrohttpd-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libmicrohttpd -f %{oreon_filedir}/mingw32-libmicrohttpd.list
%files -n mingw32-libmicrohttpd-static -f %{oreon_filedir}/mingw32-libmicrohttpd-static.list
%files -n mingw64-libmicrohttpd -f %{oreon_filedir}/mingw64-libmicrohttpd.list
%files -n mingw64-libmicrohttpd-static -f %{oreon_filedir}/mingw64-libmicrohttpd-static.list

%changelog

%autochangelog
