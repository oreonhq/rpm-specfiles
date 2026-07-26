%global source0_hash ca22e905a2717fc740e703e65a0061a0e11f4ea513ba970bbc10b3bd6d28e6e0

Name:           cmrt
Version:        1.0.6
Release:        27%{?dist}
Summary:        C for Media Runtime
License:        MIT
URL:            https://github.com/intel/cmrt
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:         cmrt-1.0.6_replace_obsolete_AC_PROG_LIBTOOL.patch

#This library depends on specific intel instructions like sse, avx…
ExclusiveArch:  %{ix86} x86_64 ia64

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libdrm) >= 2.4.23
BuildRequires:  pkgconfig(libva) >= 0.34
BuildRequires: make

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

%autosetup -p1

%build
autoreconf -vif
%configure
%make_build

%install
%make_install 
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license AUTHORS COPYING
%doc NEWS README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/cm_rt.h
%{_includedir}/cm_rt_linux.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libcmrt.pc

%changelog
%autochangelog
