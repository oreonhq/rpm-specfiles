%global source0_hash e7713409882813991d2269d125e40dad1f54a019a52b78b3962941c1d4a6f86f

Name:		pciutils
Version:	3.14.0
Release:	3%{?dist}
Summary:	PCI bus related utilities
License:	GPL-2.0-or-later
URL:		https://mj.ucw.cz/sw/pciutils/

Source0:        https://www.kernel.org/pub/software/utils/pciutils/%{name}-%{version}.tar.xz
Source1:	multilibconfigh
Source2:	libpci_symbols.lst

#change pci.ids directory to hwdata, fedora/rhel specific
Patch1:		pciutils-2.2.1-idpath.patch

#add support for directory with another pci.ids, rejected by upstream, rhbz#195327
Patch2:		pciutils-dir-d.patch

Requires:	hwdata
Requires:	%{name}-libs = %{version}-%{release}
BuildRequires:	gcc make sed kmod-devel
Provides:	/sbin/lspci /sbin/setpci
Provides:	/bin/lspci

%description
The pciutils package contains various utilities for inspecting and
setting devices connected to the PCI bus.

%package devel
Summary: Linux PCI development library
Requires: zlib-devel pkgconfig %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%package libs
Summary: Linux PCI library

%description libs
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%package devel-static
Summary: Linux PCI static library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description devel-static
This package contains a static library for inspecting and setting
devices connected to the PCI bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%global common_opts ZLIB="no" LIBKMOD=yes STRIP="" OPT="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" PREFIX="%{_prefix}" LIBDIR="%{_libdir}" IDSDIR="/usr/share/hwdata" PCI_IDS="pci.ids"
 
%make_build SHARED="no" %{common_opts}
mv lib/libpci.a lib/libpci.a.toinstall

make clean

%make_build SHARED="yes" %{common_opts}

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{7,8},%{_libdir},%{_libdir}/pkgconfig,%{_includedir}/pci}

install -p pcilmr $RPM_BUILD_ROOT%{_bindir}
install -p lspci setpci update-pciids $RPM_BUILD_ROOT%{_sbindir}
%if "%{_sbindir}" != "%{_bindir}"
ln -sr $RPM_BUILD_ROOT%{_sbindir}/lspci $RPM_BUILD_ROOT%{_bindir}/lspci
%endif
install -p -m 644 lspci.8 pcilmr.8 setpci.8 update-pciids.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 pcilib.7 $RPM_BUILD_ROOT%{_mandir}/man7
install -p lib/libpci.so.* $RPM_BUILD_ROOT%{_libdir}/
ln -s $(basename $RPM_BUILD_ROOT%{_libdir}/*.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libpci.so

mv lib/libpci.a.toinstall lib/libpci.a
install -p -m 644 lib/libpci.a $RPM_BUILD_ROOT%{_libdir}
install -p -m 644 lib/pci.h $RPM_BUILD_ROOT%{_includedir}/pci
install -p -m 644 lib/header.h $RPM_BUILD_ROOT%{_includedir}/pci
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/pci/config.h
install -p -m 644 lib/config.h $RPM_BUILD_ROOT%{_includedir}/pci/config.%{_lib}.h
install -p -m 644 lib/types.h $RPM_BUILD_ROOT%{_includedir}/pci
install -p -m 644 lib/libpci.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig

%ldconfig_scriptlets libs

%check
nm -gDC $RPM_BUILD_ROOT/%{_libdir}/libpci.so.%{version} | sed -n -e 's/@@/@/g' -e 's/^.* \([^ ]*@LIBPCI_.*\)$/\1/p' | sort | uniq >libpci_symbols_new.lst
diff -u %{SOURCE2} libpci_symbols_new.lst

%files
%doc README ChangeLog pciutils.lsm
%{_bindir}/lspci
%{_bindir}/pcilmr
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/lspci
%endif
%{_sbindir}/setpci
%{_sbindir}/update-pciids
%{_mandir}/man8/*

%files libs
%license COPYING
%{_libdir}/libpci.so.*

%files devel-static
%{_libdir}/libpci.a

%files devel
%{_libdir}/pkgconfig/libpci.pc
%{_libdir}/libpci.so
%{_includedir}/pci
%{_mandir}/man7/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.14.0-3
- Prepare for Oreon 11 (RP1)
