%global source0_hash 3a2e7a47604ba702f345878308e6fefeca612ee895cf4a5f222e7955fabfe0c0
%{?mingw_package_header}
%global underscore_version %(echo %{version} | sed 's/\\./_/g')
%global dash_version %(echo %{version} | sed 's/\\./-/g')
%global lib_version 78
Name:           mingw-icu
Version:        78.3
Release:        1%{?dist}
Summary:        MinGW compilation of International Components for Unicode Tools
License:        Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://icu-project.org
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{version}/icu4c-%{version}-sources.tgz
Patch0:         icu4c_mingwbuild.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

# Win32
%package -n mingw32-icu
Summary:        MinGW compilation of International Components for Unicode Tools
%description -n mingw32-icu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

# Win64
%package -n mingw64-icu
Summary:        MinGW compilation of International Components for Unicode Tools
%description -n mingw64-icu
ICU is a set of C and C++ libraries that provides robust and
full-featured Unicode and locale support. The library provides calendar
support, conversions for many character sets, language sensitive
collation, date and time formatting, support for many locales, message
catalogs and resources, message formatting, normalization, number and
currency formatting, time zone support, transliteration, and word,
line, and sentence breaking, etc.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir icu
%oreon_prep
%build

pushd source
mkdir -p nativebuild
pushd nativebuild
../configure --enable-static --disable-shared
%make_build || make
popd
%mingw_configure \
        --enable-shared --disable-static \
        --with-cross-build=$(pwd)/nativebuild \
        --with-data-packaging=library
%mingw_make_build
popd
%install
pushd source
%mingw_make_install
popd
rm -fr %{buildroot}%{mingw32_mandir}
rm -fr %{buildroot}%{mingw64_mandir}
rm %{buildroot}%{mingw32_bindir}/icu-config
rm %{buildroot}%{mingw64_bindir}/icu-config
rm %{buildroot}%{mingw32_libdir}/icu/Makefile.inc
rm %{buildroot}%{mingw64_libdir}/icu/Makefile.inc
rm %{buildroot}%{mingw32_libdir}/icu/pkgdata.inc
rm %{buildroot}%{mingw64_libdir}/icu/pkgdata.inc
%oreon_autofiles mingw32-icu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-icu usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-icu -f %{oreon_filedir}/mingw32-icu.list
%files -n mingw64-icu -f %{oreon_filedir}/mingw64-icu.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 77.1-2
- Prepare for Oreon 11 (RP1)
