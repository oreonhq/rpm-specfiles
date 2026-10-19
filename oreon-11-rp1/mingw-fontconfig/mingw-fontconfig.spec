%global source0_hash bc1a90697eb8ec6c3eed118105ef9cbdfdd676e563905bf1cb571a705598300e
%{?mingw_package_header}
Name:           mingw-fontconfig
Version:        2.17.1
Release:        1%{?dist}
Summary:        MinGW Windows Fontconfig library
License:        MIT
URL:            http://fontconfig.org
Source0:        https://gitlab.freedesktop.org/fontconfig/fontconfig/-/archive/%{version}/fontconfig-%{version}.tar.bz2
Patch0:         fontconfig_tests.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-win-iconv
BuildRequires:  pkgconfig
BuildRequires:  python3
# /oreon:deps
%description
MinGW Windows Fontconfig library.

# Win32
%package -n mingw32-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig
%description -n mingw32-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw32-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw32-fontconfig = %{version}-%{release}
%description -n mingw32-fontconfig-static
Static version of the cross compiled Fontconfig library.

# Win64
%package -n mingw64-fontconfig
Summary:        MinGW Windows Fontconfig library
Requires:       pkgconfig
%description -n mingw64-fontconfig
MinGW Windows Fontconfig library.

%package -n mingw64-fontconfig-static
Summary:       Static version of the cross compiled Fontconfig library
Requires:      mingw64-fontconfig = %{version}-%{release}
%description -n mingw64-fontconfig-static
Static version of the cross compiled Fontconfig library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fontconfig-%{version}
%oreon_prep
%build

export MINGW32_CONFIGURE_ARGS="--with-arch=i686"
export MINGW64_CONFIGURE_ARGS="--with-arch=x86_64"
autoreconf -ifv
%mingw_configure --disable-docs --disable-tests --enable-static --enable-shared
%mingw_make_build
%install
%mingw_make_install
rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias
rm -f %{buildroot}%{mingw32_libdir}/fontconfig.def
rm -f %{buildroot}%{mingw64_libdir}/fontconfig.def
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc
%oreon_autofiles mingw32-fontconfig usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-fontconfig-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-fontconfig usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-fontconfig-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-fontconfig -f %{oreon_filedir}/mingw32-fontconfig.list
%files -n mingw32-fontconfig-static -f %{oreon_filedir}/mingw32-fontconfig-static.list
%files -n mingw64-fontconfig -f %{oreon_filedir}/mingw64-fontconfig.list
%files -n mingw64-fontconfig-static -f %{oreon_filedir}/mingw64-fontconfig-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.17.1-3
- Prepare for Oreon 11 (RP1)
