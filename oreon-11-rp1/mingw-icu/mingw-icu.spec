%global source0_hash none

%{?mingw_package_header}

%global underscore_version %(echo %{version} | sed 's/\\./_/g')
%global dash_version %(echo %{version} | sed 's/\\./-/g')
%global lib_version 77

Name:           mingw-icu
Version:        77.1
Release:        2%{?dist}
Summary:        MinGW compilation of International Components for Unicode Tools

License:        Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://icu-project.org
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{dash_version}/icu4c-%{underscore_version}-src.tgz

# Patch to fix the build from
# https://build.opensuse.org/package/show/windows:mingw:win32/mingw32-icu
Patch0:         icu4c_mingwbuild.patch

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

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
%autosetup -p1 -n icu


%build
pushd source

mkdir -p nativebuild
pushd nativebuild
../configure --enable-static --disable-shared
# Parallel build occasionally broken
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

# remove unneded files
rm -fr %{buildroot}%{mingw32_mandir}
rm -fr %{buildroot}%{mingw64_mandir}

rm %{buildroot}%{mingw32_bindir}/icu-config
rm %{buildroot}%{mingw64_bindir}/icu-config
rm %{buildroot}%{mingw32_libdir}/icu/Makefile.inc
rm %{buildroot}%{mingw64_libdir}/icu/Makefile.inc
rm %{buildroot}%{mingw32_libdir}/icu/pkgdata.inc
rm %{buildroot}%{mingw64_libdir}/icu/pkgdata.inc


# Win32
%files -n mingw32-icu
%license license.html

%{mingw32_bindir}/escapesrc.exe
%{mingw32_bindir}/genrb.exe
%{mingw32_bindir}/gencnval.exe
%{mingw32_bindir}/uconv.exe
%{mingw32_bindir}/gencmn.exe
%{mingw32_bindir}/makeconv.exe
%{mingw32_bindir}/genbrk.exe
%{mingw32_bindir}/gensprep.exe
%{mingw32_bindir}/pkgdata.exe
%{mingw32_bindir}/icuexportdata.exe
%{mingw32_bindir}/icupkg.exe
%{mingw32_bindir}/derb.exe
%{mingw32_bindir}/genccode.exe
%{mingw32_bindir}/gendict.exe
%{mingw32_bindir}/gencfu.exe
%{mingw32_bindir}/gennorm2.exe
%{mingw32_bindir}/icuinfo.exe

%{mingw32_bindir}/icuio%{lib_version}.dll
%{mingw32_bindir}/icuuc%{lib_version}.dll
%{mingw32_bindir}/icui18n%{lib_version}.dll
%{mingw32_bindir}/icutu%{lib_version}.dll
%{mingw32_bindir}/icudata%{lib_version}.dll
%{mingw32_bindir}/icutest%{lib_version}.dll

%{mingw32_libdir}/libicudata.dll.a
%{mingw32_libdir}/libicui18n.dll.a
%{mingw32_libdir}/libicuuc.dll.a
%{mingw32_libdir}/libicuio.dll.a
%{mingw32_libdir}/libicutest.dll.a
%{mingw32_libdir}/libicutu.dll.a
%{mingw32_libdir}/pkgconfig/icu-i18n.pc
%{mingw32_libdir}/pkgconfig/icu-io.pc
%{mingw32_libdir}/pkgconfig/icu-uc.pc
%{mingw32_includedir}/unicode
%{mingw32_libdir}/icu
%{mingw32_datadir}/icu

# Win64
%files -n mingw64-icu
%license license.html

%{mingw64_bindir}/escapesrc.exe
%{mingw64_bindir}/genrb.exe
%{mingw64_bindir}/gencnval.exe
%{mingw64_bindir}/uconv.exe
%{mingw64_bindir}/gencmn.exe
%{mingw64_bindir}/makeconv.exe
%{mingw64_bindir}/genbrk.exe
%{mingw64_bindir}/gensprep.exe
%{mingw64_bindir}/pkgdata.exe
%{mingw64_bindir}/icuexportdata.exe
%{mingw64_bindir}/icupkg.exe
%{mingw64_bindir}/derb.exe
%{mingw64_bindir}/genccode.exe
%{mingw64_bindir}/gendict.exe
%{mingw64_bindir}/gencfu.exe
%{mingw64_bindir}/gennorm2.exe
%{mingw64_bindir}/icuinfo.exe

%{mingw64_bindir}/icuio%{lib_version}.dll
%{mingw64_bindir}/icuuc%{lib_version}.dll
%{mingw64_bindir}/icui18n%{lib_version}.dll
%{mingw64_bindir}/icutu%{lib_version}.dll
%{mingw64_bindir}/icudata%{lib_version}.dll
%{mingw64_bindir}/icutest%{lib_version}.dll

%{mingw64_libdir}/libicudata.dll.a
%{mingw64_libdir}/libicui18n.dll.a
%{mingw64_libdir}/libicuuc.dll.a
%{mingw64_libdir}/libicuio.dll.a
%{mingw64_libdir}/libicutest.dll.a
%{mingw64_libdir}/libicutu.dll.a
%{mingw64_libdir}/pkgconfig/icu-i18n.pc
%{mingw64_libdir}/pkgconfig/icu-io.pc
%{mingw64_libdir}/pkgconfig/icu-uc.pc
%{mingw64_includedir}/unicode
%{mingw64_libdir}/icu
%{mingw64_datadir}/icu


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 77.1-2
- Prepare for Oreon 11 (RP1)
