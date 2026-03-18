Summary:        Audio/Video Control library for IEEE-1394 devices
Name:           libavc1394
Version:        0.5.4
Release:        27%{?dist}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://sourceforge.net/projects/libavc1394/
Source:         https://sourceforge.net/projects/libavc1394/files/libavc1394/libavc1394-%{version}.tar.gz
Patch1:         libavc1394-%{version}-librom.patch
BuildRequires:  libraw1394-devel
BuildRequires:  chrpath, gcc
BuildRequires:  make

# libraw1394 is not built on s390*
ExcludeArch:    s390 s390x

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
%autosetup -N
%patch -P 1 -p1 -b .librom
chmod -x test/dvcont.c

%build
%configure
%make_build

%install
%make_install
# sigh, --disable-static doesn't work
rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}

chrpath -d $RPM_BUILD_ROOT%{_libdir}/lib*
chrpath -d $RPM_BUILD_ROOT%{_bindir}/*

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README ChangeLog TODO
%license COPYING
# binaries are GPLv2+
%{_bindir}/dvcont
%{_bindir}/mkrfc2734
%{_bindir}/panelctl
%{_mandir}/man1/dvcont.1*
%{_mandir}/man1/panelctl.1*
%{_mandir}/man1/mkrfc2734.1*
# libs are LGPLv2+
%{_libdir}/libavc1394.so.*
%{_libdir}/librom1394.so.*

%files devel
%{_includedir}/libavc1394/
%{_libdir}/pkgconfig/libavc1394.pc
%{_libdir}/libavc1394.so
%{_libdir}/librom1394.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.4-27
- Prepare for Oreon 11 (RP1)
