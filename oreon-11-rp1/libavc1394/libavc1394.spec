%global source0_hash 7cb1ff09506ae911ca9860bef4af08c2403f3e131f6c913a2cbd6ddca4215b53
Summary:        Audio/Video Control library for IEEE-1394 devices
Name:           libavc1394
Version:        0.5.4
Release:        27%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://sourceforge.net/projects/libavc1394/
Source0:        https://sourceforge.net/projects/libavc1394/files/libavc1394/libavc1394-%{version}.tar.gz
Patch1:         libavc1394-%{version}-librom.patch
ExcludeArch:    s390 s390x
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  libraw1394-devel
BuildRequires:  make
# /oreon:deps
%description
The libavc1394 library allows utilities to control IEEE-1394 devices
using the AV/C specification.  Audio/Video Control allows applications
to control devices like the tape on a VCR or camcorder.

%package devel
Summary: Development libs for libavc1394
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libraw1394-devel%{?_isa}
%description devel
Development libraries required to build applications using libavc1394.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N
%patch -P 1 -p1 -b .librom
chmod -x test/dvcont.c

%build

%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}
chrpath -d $RPM_BUILD_ROOT%{_libdir}/lib*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libavc1394-devel -f %{oreon_filedir}/libavc1394-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.4-27
- Prepare for Oreon 11 (RP1)
