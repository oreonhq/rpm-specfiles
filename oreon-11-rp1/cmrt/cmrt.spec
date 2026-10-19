%global source0_hash ca22e905a2717fc740e703e65a0061a0e11f4ea513ba970bbc10b3bd6d28e6e0
Name:           cmrt
Version:        1.0.6
Release:        27%{?dist}
Summary:        C for Media Runtime
License:        MIT
URL:            https://github.com/intel/cmrt
Source0:        https://github.com/intel/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         cmrt-1.0.6_replace_obsolete_AC_PROG_LIBTOOL.patch
ExclusiveArch:  %{ix86} x86_64 ia64
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libva)
# /oreon:deps
%description
Media GPU kernel manager for Intel G45 & HD Graphics family. Allows to
interface between Intel GPU's driver and a host program through a high 
level language.

%package devel
Summary:        Development files for the C for Media Runtime
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Media GPU kernel manager for Intel G45 & HD Graphics family, 
development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure
%make_build
%install
%make_install 
find %{buildroot} -name "*.la" -delete
%ldconfig_scriptlets
%oreon_autofiles cmrt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cmrt-devel -f %{oreon_filedir}/cmrt-devel.list

%changelog

%autochangelog
