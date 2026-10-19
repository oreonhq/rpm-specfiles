%global source0_hash 158860aaea52f0fce0c8e4b64550daaae06df2689e05834697b7e8c7d73dd4fc
%global udevdir %{_prefix}/lib/udev
%undefine __cmake_in_source_build
Summary:        Library for using OBEX
Name: openobex
Version: 1.7.2
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: http://openobex.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-Source.tar.gz
Patch0:  openobex-apps-flush.patch
Patch1:  openobex-1.7-obex_push.patch
Patch2:  openobex-1.7-udev_rule.patch
Patch3:  openobex-1.7-strtoul.patch
Patch4:  openobex-min-cmake.patch
ExcludeArch: s390 s390x
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  cmake
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libusb1-devel
BuildRequires:  libxslt
BuildRequires:  make
# /oreon:deps
%description
OBEX (OBject EXchange) is a protocol usually used by various mobile
devices to exchange all kind of objects like files, pictures, calendar
entries (vCal) and business cards (vCard).  This package contains the
Open OBEX shared C library.

%package devel
Summary: Files for development of applications which will use OBEX
Requires: %{name} = %{version}-%{release}
Requires: bluez-libs-devel libusb1-devel
%description devel
Header files for development of applications which use OpenOBEX.

%package apps
Summary: Applications for using OBEX
%description apps
Open OBEX Applications to exchange all kind of objects like files, pictures,
calendar entries (vCal) and business cards (vCard) using the OBEX protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}-Source
%oreon_prep
%build

export CFLAGS="%{optflags} -std=gnu99 -D_POSIX_C_SOURCE=200809L -D_DEFAULT_SOURCE"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_SKIP_RPATH=YES \
       -DCMAKE_VERBOSE_MAKEFILE=YES \
       -DCMAKE_INSTALL_DOCDIR=%{_pkgdocdir} \
       -DCMAKE_INSTALL_UDEVRULESDIR=%{udevdir}/rules.d
%cmake_build
%cmake_build --target openobex-apps
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_bindir}/obex_test
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/obex_test.1*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openobex-devel -f %{oreon_filedir}/openobex-devel.list
%files -n openobex-apps -f %{oreon_filedir}/openobex-apps.list

%changelog

%autochangelog
