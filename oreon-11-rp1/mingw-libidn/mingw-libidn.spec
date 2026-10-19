%global source0_hash 499608bab3a65650a0ea52888c13a8deebe3f71408e319acd9ec52e02eb13959
%{?mingw_package_header}
Name:           mingw-libidn
Version:        1.44
Release:        1%{?dist}
Summary:        MinGW Windows Internationalized Domain Name support library
License:        (LGPL-3.0-or-later OR GPL-2.0-or-later) AND GPL-3.0-or-later AND GFDL-1.3-or-later
URL:            http://www.gnu.org/software/libidn/
Source0:        http://ftp.gnu.org/gnu/libidn/libidn-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  pkgconfig
# /oreon:deps
%description
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

# Win32
%package -n mingw32-libidn
Summary:        MinGW Windows zlib compression library for the win32 target
Requires:       pkgconfig
%description -n mingw32-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw32-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw32-libidn = %{version}-%{release}
%description -n mingw32-libidn-static
Static version of the MinGW Windows IDN library.

# Win64
%package -n mingw64-libidn
Summary:        MinGW Windows zlib compression library for the win64 target
Requires:       pkgconfig
%description -n mingw64-libidn
GNU Libidn is an implementation of the Stringprep, Punycode and
IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group, used for internationalized domain
names.

%package -n mingw64-libidn-static
Summary:        Static version of the MinGW Windows IDN library
Requires:       mingw64-libidn = %{version}-%{release}
%description -n mingw64-libidn-static
Static version of the MinGW Windows IDN library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libidn-%{version}
%oreon_prep
%build

%mingw_configure --disable-nls --disable-csharp --enable-static --enable-shared
%mingw_make_build
%install
%mingw_make_install
rm -r %{buildroot}%{mingw32_datadir}/emacs
rm -r %{buildroot}%{mingw64_datadir}/emacs
rm -r %{buildroot}%{mingw32_infodir}
rm -r %{buildroot}%{mingw64_infodir}
rm -r %{buildroot}%{mingw32_mandir}/man*
rm -r %{buildroot}%{mingw64_mandir}/man*
rm -f %{buildroot}%{mingw32_bindir}/libidn-12.def
rm -f %{buildroot}%{mingw64_bindir}/libidn-12.def
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-libidn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libidn-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libidn usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libidn-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libidn -f %{oreon_filedir}/mingw32-libidn.list
%files -n mingw32-libidn-static -f %{oreon_filedir}/mingw32-libidn-static.list
%files -n mingw64-libidn -f %{oreon_filedir}/mingw64-libidn.list
%files -n mingw64-libidn-static -f %{oreon_filedir}/mingw64-libidn-static.list

%changelog

%autochangelog
