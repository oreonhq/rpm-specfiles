%global source0_hash 80ae32cb9f568af4dc7ee4d3c05a4c31fc513fc3e31730fed0ce7378237273a9

%{?mingw_package_header}

%global mingw_pkg_name lcms

Name:           mingw-%{mingw_pkg_name}
Version:        1.19
Release:        29%{?dist}
Summary:        MinGW Color Management System
License:        MIT
URL:            http://www.littlecms.com/
Source0:        http://downloads.sourceforge.net/%{mingw_pkg_name}/%{mingw_pkg_name}-%{version}.tar.gz
Patch0:         %{mingw_pkg_name}-1.19-rhbz675186.patch
# bug 992979 / CVE-2013-4276
# Stack-based buffer overflows in ColorSpace conversion calculator
# and TIFF compare utility
Patch1:         %{mingw_pkg_name}-1.19-rhbz991757.patch
# bug 1003950
Patch2:         %{mingw_pkg_name}-1.19-rhbz1003950.patch
Patch3:         %{mingw_pkg_name}-c99.patch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw64-libtiff
BuildRequires:  pkgconfig
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildArch:      noarch

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw32-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw32-%{mingw_pkg_name} development
Requires: mingw32-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw32-%{mingw_pkg_name}-static
The mingw32-%{mingw_pkg_name}-static package contains static library for
mingw32-%{mingw_pkg_name} development.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:                %{summary}

%description -n mingw64-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw64-%{mingw_pkg_name} development
Requires: mingw64-%{mingw_pkg_name} = %{version}-%{release}

%description -n mingw64-%{mingw_pkg_name}-static
The mingw64-%{mingw_pkg_name}-static package contains static library for
mingw64-%{mingw_pkg_name} development.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{mingw_pkg_name}-%{version}
%autopatch -p1

find . -type f -name '*.[ch]' -exec chmod -x '{}' \;
chmod 0644 AUTHORS COPYING ChangeLog NEWS README.1ST doc/TUTORIAL.TXT doc/LCMSAPI.TXT

# Convert not UTF-8 files
pushd doc
mkdir -p __temp
for f in LCMSAPI.TXT TUTORIAL.TXT ;do
cp -p $f __temp/$f
iconv -f ISO-8859-1 -t UTF-8 __temp/$f > $f
touch -r __temp/$f $f
done
rm -rf __temp
popd

%build
export MINGW32_CFLAGS="%{mingw32_cflags} -Wno-error=incompatible-pointer-types"
export MINGW64_CFLAGS="%{mingw64_cflags} -Wno-error=incompatible-pointer-types"
%mingw_configure --without-python --enable-shared

# remove rpath from libtool
#sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

rm include/icc34.h

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.exe" -exec rm -f {} ';'
rm -rf ${RPM_BUILD_ROOT}/%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}/%{mingw64_mandir}

%files -n mingw32-%{mingw_pkg_name}
%doc README.1ST doc/TUTORIAL.TXT AUTHORS COPYING NEWS doc/LCMSAPI.TXT
%{mingw32_includedir}/*
%{mingw32_libdir}/liblcms.dll.a
%{mingw32_bindir}/liblcms-1.dll
%{mingw32_libdir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/liblcms.a

%files -n mingw64-%{mingw_pkg_name}
%doc README.1ST doc/TUTORIAL.TXT AUTHORS COPYING NEWS doc/LCMSAPI.TXT
%{mingw64_includedir}/*
%{mingw64_libdir}/liblcms.dll.a
%{mingw64_bindir}/liblcms-1.dll
%{mingw64_libdir}/pkgconfig/%{mingw_pkg_name}.pc

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/liblcms.a

%changelog
%autochangelog
