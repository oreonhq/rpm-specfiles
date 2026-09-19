%global source0_hash 43e58d7cd22b3a4c4dc8dcf8542a269ebcb4d8f6ceea0577b9fc882898f09a47

Name:           libirman
Epoch:          1
Version:        0.5.2
Release:        25%{?dist}
Summary:        Library for IRMAN hardware

#The files which make up the library are covered under the GNU Library
#General Public License, which is in the file COPYING.lib.
#The files which make up the test programs and the documentation are covered
#under the GNU General Public License, which is in the file COPYING.
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/libirman/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf, automake, libtool
BuildRequires:  lirc-devel >= 0.9.4
BuildRequires: make

%description
Runtime libraries for accessing the IrMan hardware.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description    devel
Libraries and header files for developing applications that use %{name}.

The IrMan hardware((http://www.intolect.com/irmandetail.htm) is  nowadays
discontinued. However, some modern hardware (notably the irtoy) is able to
emulate the irman protocol.

%package  -n    lirc-drv-irman
Summary:        lircd(8) plugin for handling IrMan devices.
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       lirc >= 0.9.4

%description  -n lirc-drv-irman
A lirc plugin with a single driver, replacing the irman support which
was built-in in lirc prior to 0.9.4.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
libtoolize --force --copy --install
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete
rm  $RPM_BUILD_ROOT%{_docdir}/libirman/TECHNICAL

%ldconfig_scriptlets

%files
%doc COPYING* README TODO NEWS
%config(noreplace) %{_sysconfdir}/irman.conf
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%doc TECHNICAL
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libirman.pc

%files -n lirc-drv-irman
%{_libdir}/lirc/plugins/irman.so
%{_docdir}/lirc/plugindocs/irman.html
%{_datadir}/lirc/configs/irman.conf

%changelog
%autochangelog
