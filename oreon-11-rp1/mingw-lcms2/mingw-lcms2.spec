%global source0_hash bfc54f7bab59fbc921012014a8032e4cba4abd46db47d46b76416a8c0b2815c8
%{?mingw_package_header}
%global mingw_pkg_name lcms2
Name:           mingw-%{mingw_pkg_name}
Version:        2.19.1
Release:        1%{?dist}
Summary:        MinGW Color Management Engine
License:        MIT
URL:            http://www.littlecms.com/
Source0:        https://sourceforge.net/projects/lcms/files/lcms/%{version}/%{mingw_pkg_name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW Color Management Engine
%description -n mingw32-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package -n mingw32-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw32-%{mingw_pkg_name} development
Requires: mingw32-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw32-%{mingw_pkg_name}-static
The mingw32-%{mingw_pkg_name}-static package contains static library for
mingw32-%{mingw_pkg_name} development.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW Color Management Engine
%description -n mingw64-%{mingw_pkg_name}
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form. LCMS2 is the current version of LCMS, and can be
parallel installed with the original (deprecated) lcms.

%package -n mingw64-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw64-%{mingw_pkg_name} development
Requires: mingw64-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw64-%{mingw_pkg_name}-static
The mingw64-%{mingw_pkg_name}-static package contains static library for
mingw64-%{mingw_pkg_name} development.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
#setup -q -n %{mingw_pkg_name}-%{version}%{prerelease}
%setup -q -n %{mingw_pkg_name}-%{version}
iconv -f ISO-8859-1 -t UTF-8 AUTHORS > AUTHORS.x
mv -f AUTHORS.x AUTHORS

%build

%mingw_configure --enable-static --program-suffix=2
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p"
find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.exe" -exec rm -f {} ';'
install -D -m 644 include/lcms2.h $RPM_BUILD_ROOT%{mingw32_includedir}/lcms2.h
install -D -m 644 include/lcms2.h $RPM_BUILD_ROOT%{mingw64_includedir}/lcms2.h
install -D -m 644 include/lcms2_plugin.h $RPM_BUILD_ROOT%{mingw32_includedir}/lcms2_plugin.h
install -D -m 644 include/lcms2_plugin.h $RPM_BUILD_ROOT%{mingw64_includedir}/lcms2_plugin.h
rm -rf ${RPM_BUILD_ROOT}/%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}/%{mingw64_mandir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-lcms2 -f %{oreon_filedir}/mingw32-lcms2.list
%files -n mingw32-lcms2-static -f %{oreon_filedir}/mingw32-lcms2-static.list
%files -n mingw64-lcms2 -f %{oreon_filedir}/mingw64-lcms2.list
%files -n mingw64-lcms2-static -f %{oreon_filedir}/mingw64-lcms2-static.list

%changelog

%autochangelog
