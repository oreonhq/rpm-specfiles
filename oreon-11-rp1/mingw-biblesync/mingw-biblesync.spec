%global source0_hash 9083fcacc4d85f2b8c3a3254112129c02d940d20db8c0c5bcb6239b115e8d0e8

%?mingw_package_header

%global __soversion 2.0
%global _pkg_name biblesync

Name:		mingw-%{_pkg_name}
Version:	2.1.0
Release:	17%{?dist}
Summary:	A Cross-platform library for sharing Bible navigation

Group:		System Environment/Libraries
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.xiphos.org
Source0:	https://github.com/karlkleinpaste/%{_pkg_name}/releases/download/%{version}/%{_pkg_name}-%{version}.tar.gz
# https://github.com/karlkleinpaste/biblesync/commit/4b00f9fd3d0c858947eee18206ef44f9f6bd2283.patch
Patch0:		4b00f9fd3d0c858947eee18206ef44f9f6bd2283.patch

BuildArch:		noarch

BuildRequires: make
BuildRequires:	cmake

BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-gettext

BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-gcc-c++
BuildRequires:	mingw64-gettext

%description
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

# Win32
%package -n mingw32-%{_pkg_name}
Summary:	A MinGW build of the biblesync library

%description -n mingw32-%{_pkg_name}
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

# Win64
%package -n mingw64-%{_pkg_name}
Summary:	A MinGW build of the biblesync library

%description -n mingw64-%{_pkg_name}
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{_pkg_name}-%{version}
%autopatch

%build
%mingw_cmake -DBIBLESYNC_SOVERSION=%{__soversion}
%mingw_make

%install
%mingw_make install DESTDIR=%{buildroot}

find "%{buildroot}" -name man7 | xargs rm -rf
mkdir -p "%{buildroot}%{mingw32_bindir}"
mkdir -p "%{buildroot}%{mingw64_bindir}"
mv "%{buildroot}%{mingw32_libdir}/"*.dll "%{buildroot}%{mingw32_bindir}/"
mv "%{buildroot}%{mingw64_libdir}/"*.dll "%{buildroot}%{mingw64_bindir}/"

%files -n mingw32-%{_pkg_name}
%doc AUTHORS ChangeLog README.md WIRESHARK
%license COPYING
%license LICENSE
%{mingw32_bindir}/lib%{_pkg_name}.dll
%{mingw32_includedir}/%{_pkg_name}
%{mingw32_libdir}/pkgconfig/%{_pkg_name}.pc
%{mingw32_libdir}/lib%{_pkg_name}.dll.a

%files -n mingw64-%{_pkg_name}
%doc AUTHORS ChangeLog README.md WIRESHARK
%license COPYING
%license LICENSE
%{mingw64_bindir}/lib%{_pkg_name}.dll
%{mingw64_includedir}/%{_pkg_name}
%{mingw64_libdir}/pkgconfig/%{_pkg_name}.pc
%{mingw64_libdir}/lib%{_pkg_name}.dll.a

%changelog
%autochangelog
