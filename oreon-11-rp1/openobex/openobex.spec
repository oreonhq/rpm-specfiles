%global source0_hash 158860aaea52f0fce0c8e4b64550daaae06df2689e05834697b7e8c7d73dd4fc

%global udevdir %{_prefix}/lib/udev

%undefine __cmake_in_source_build

Summary: Library for using OBEX
Name: openobex
Version: 1.7.2
Release: 30%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: http://openobex.sourceforge.net
# git clone https://git.gitorious.org/openobex/mainline.git
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}-Source.tar.gz
Patch0:  openobex-apps-flush.patch
Patch1:  openobex-1.7-obex_push.patch
Patch2:  openobex-1.7-udev_rule.patch
Patch3:  openobex-1.7-strtoul.patch
# compatibility for Cmake 3.1 was removed, raise the min version
Patch4:  openobex-min-cmake.patch

# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses autosetup
BuildRequires: git-core

BuildRequires: bluez-libs-devel, libusb1-devel
BuildRequires: cmake, doxygen, libxslt, docbook-style-xsl
# cmake uses make internally
BuildRequires: make
ExcludeArch: s390 s390x

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

%autosetup -n %{name}-%{version}-Source -S git

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
# we do not want .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
# don't ship obex_test program, that is for testing purposes only
# and has some problems (multiple buffer overflows etc.)
rm -f $RPM_BUILD_ROOT%{_bindir}/obex_test
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/obex_test.1*

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog README
# the HTML doc is distributed in the %%{name}-devel subpackage
%exclude %{_pkgdocdir}/html
%{_libdir}/libopenobex.so.1.7.2
%{_libdir}/libopenobex.so.2
%{_sbindir}/obex-check-device
%{udevdir}/rules.d/60-openobex.rules

%files devel
%doc %{_pkgdocdir}/html
%{_libdir}/libopenobex*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/openobex.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/OpenObex-%{version}

%files apps
%{_bindir}/irobex_palm3
%{_mandir}/man1/irobex_palm3.1*
%{_bindir}/irxfer
%{_mandir}/man1/irxfer.1*
%{_bindir}/ircp
%{_mandir}/man1/ircp.1*
%{_bindir}/obex_tcp
%{_mandir}/man1/obex_tcp.1*
%{_bindir}/obex_find
%{_mandir}/man1/obex_find.1*
%{_bindir}/obex_push
%{_mandir}/man1/obex_push.1*

%changelog
%autochangelog
