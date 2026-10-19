%global source1_hash 3e931150d0e290a7243fe4247376cc910b10cb88932b452fc73c8becedcce8b8
%global source0_hash de18463bf7c0cb639a3228ad47e69eb7f78a5a197802d325f3a5ed7e1c56d57f
%define adplugdbver 2006-07-07
Name:           adplug
Version:        2.4
Release:        1%{?dist}
Summary:        Software library for AdLib (OPL2/3) emulation
URL:            https://adplug.github.io/
Source0:        https://github.com/adplug/adplug/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        https://download.sourceforge.net/%{name}/adplugdb-%{adplugdbver}.tar.gz
License:        LGPL-2.1-or-later AND GFDL-1.1-or-later
%define shareddata %{_localstatedir}/lib
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libbinio-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  texinfo
# /oreon:deps
%description
AdPlug is a free software, cross-platform, hardware independent AdLib
sound player library, mainly written in C++. AdPlug plays sound data, 
originally created for the AdLib (OPL2/3) audio board, directly from
its original format on top of an OPL2/3 emulator or by using the real
hardware. No OPL2/3 chips are required for playback.

%package devel
Summary:        Development files for AdPlug
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libbinio-devel
%description devel
This package contains development files for the AdPlug AdLib (OPL2/3)
emulator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
tar xvfz %{SOURCE1}
# Include these by different name
mv %{adplugdbver}/README README.adplugdb
mv %{adplugdbver}/NEWS NEWS.adplugdb

%build

%configure --disable-static --sharedstatedir=%{shareddata}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
install -D -p -m 644 %{adplugdbver}/adplug.db $RPM_BUILD_ROOT%{shareddata}/%{name}/adplug.db
%ldconfig_scriptlets
%oreon_autofiles adplug-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n adplug-devel -f %{oreon_filedir}/adplug-devel.list

%changelog

%autochangelog
