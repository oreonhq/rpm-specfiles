%global source0_hash 3c55aa86c82e54a4e3109786f0463530d53b36b6d1cfd14616454f985dd2aa43
Name:           libpciaccess
Version:        0.19
Release:        1%{?dist}
Summary:        PCI access library
License:        HPND AND MIT
URL:            https://www.x.org/
Source0:        https://www.x.org/archive/individual/lib/%{name}-%{version}.tar.xz
Source1:        make-libpciaccess-snapshot.sh
Patch2:		libpciaccess-rom-size.patch
Requires:       hwdata
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Development package for libpciaccess.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -fi
%configure --disable-static
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpciaccess-devel -f %{oreon_filedir}/libpciaccess-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.16-17
- Prepare for Oreon 11 (RP1)
