%global source0_hash a37b2f1b88fd1bfe74109586be463a434d34e773530fc2a74364cfcf734c032e

%{?mingw_package_header}

Name:           mingw-libmicrohttpd
Version:        0.9.73
Release:        13%{?dist}
Summary:        MinGW package for libmicrohttpd

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-gnutls

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-gnutls

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
# microspdy is not MinGW-compatible at this time
%mingw_configure --with-gnutls --enable-spdy=no --enable-https=yes
%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# remove documentation provided by native package
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/info
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man

# remove libtool files
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# remove libmicrospdy autotool files as we do not provide a dll
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/pkgconfig/libmicrospdy.pc
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/pkgconfig/libmicrospdy.pc

# Win32
%files -n mingw32-libmicrohttpd
%license COPYING
%{mingw32_bindir}/libmicrohttpd-12.dll
%{mingw32_includedir}/microhttpd.h
%{mingw32_libdir}/libmicrohttpd.dll.a
%{mingw32_libdir}/pkgconfig/libmicrohttpd.pc

%files -n mingw32-libmicrohttpd-static
%{mingw32_libdir}/libmicrohttpd.a

# Win64
%files -n mingw64-libmicrohttpd
%license COPYING
%{mingw64_bindir}/libmicrohttpd-12.dll
%{mingw64_includedir}/microhttpd.h
%{mingw64_libdir}/libmicrohttpd.dll.a
%{mingw64_libdir}/pkgconfig/libmicrohttpd.pc

%files -n mingw64-libmicrohttpd-static
%{mingw64_libdir}/libmicrohttpd.a

%changelog
%autochangelog
