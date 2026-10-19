%global source0_hash 933be3dac6fd55f6e752331a170efb7e33800e40fae1156d8434cc8c85379a1b
%{?mingw_package_header}
%global pkgname hunspell
Name:          mingw-%{pkgname}
Version:       1.7.3
Release:        1%{?dist}
Summary:        MinGW Windows spell checker and morphological analyzer library
URL:           http://hunspell.github.io/
License:       LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
Source0:        https://github.com/%{pkgname}/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-readline
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-readline
# /oreon:deps
%description
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell.

# Win32
%package -n mingw32-%{pkgname}
Summary:       MinGW Windows spell checker and morphological analyzer library
%description -n mingw32-%{pkgname}
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell.

%package -n mingw32-%{pkgname}-static
Summary:        Static version of the MinGW Windows hunspell library
Requires:       mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-static
Static version of the MinGW Windows hunspell spell checking library.

%package -n mingw32-%{pkgname}-tools
Summary:        MinGW Windows hunspell library tools
Requires:       mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-tools
MinGW Windows hunspell library tools.

# Win64
%package -n mingw64-%{pkgname}
Summary:       MinGW Windows spell checker and morphological analyzer library
%description -n mingw64-%{pkgname}
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, OpenOffice.org UNO module.

This is the MinGW build of Hunspell

%package -n mingw64-%{pkgname}-static
Summary:        Static version of the MinGW Windows hunspell library
Requires:       mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-static
Static version of the MinGW Windows hunspell spell checking library.

%package -n mingw64-%{pkgname}-tools
Summary:        MinGW Windows hunspell library tools
Requires:       mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-tools
MinGW Windows hunspell library tools.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

autoreconf -ifv
%mingw_configure --enable-static --enable-shared --with-ui --with-readline --enable-threads=win32
%mingw_make_build
%install
%mingw_make_install
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/man
rm -rf %{buildroot}%{mingw64_datadir}/man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-hunspell -f %{oreon_filedir}/mingw32-hunspell.list
%files -n mingw32-hunspell-static -f %{oreon_filedir}/mingw32-hunspell-static.list
%files -n mingw32-hunspell-tools -f %{oreon_filedir}/mingw32-hunspell-tools.list
%files -n mingw64-hunspell -f %{oreon_filedir}/mingw64-hunspell.list
%files -n mingw64-hunspell-static -f %{oreon_filedir}/mingw64-hunspell-static.list
%files -n mingw64-hunspell-tools -f %{oreon_filedir}/mingw64-hunspell-tools.list

%changelog

%autochangelog
