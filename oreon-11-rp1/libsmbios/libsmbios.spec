%global source0_hash none

# these are all substituted by autoconf
%define pot_file  libsmbios
%define lang_dom  libsmbios-2.4

Name: libsmbios
Version: 2.4.3
Release: 22%{?dist}
Summary: Libsmbios C/C++ shared libraries

License: GPL-2.0-or-later or OSL-2.1
URL: https://github.com/dell/libsmbios
Source0:        https://github.com/dell/libsmbios/archive/refs/tags/v%{version}.tar.gz#/libsmbios-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gettext-devel
BuildRequires: help2man
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: strace
BuildRequires: valgrind

# libsmbios only ever makes sense on intel compatible arches
# no DMI tables on ppc, s390, etc.
ExclusiveArch: x86_64 %{ix86}

%description
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package provides the C-based libsmbios library, with a C interface.

%package -n python3-smbios
Summary: Python interface to Libsmbios C library
Requires: libsmbios = %{version}-%{release}
Requires: python3
Obsoletes: python-smbios < 2.4.1

%description -n python3-smbios
This package provides a Python interface to libsmbios

%package -n smbios-utils
Summary: Meta-package that pulls in all smbios binaries and python scripts
Requires: smbios-utils-bin
Requires: smbios-utils-python

%description -n smbios-utils
This is a meta-package that pulls in the binary libsmbios executables as well
as the python executables.

%package -n smbios-utils-bin
Summary: Binary utilities that use libsmbios
Requires: libsmbios = %{version}-%{release}

%description -n smbios-utils-bin
Get BIOS information, such as System product name, product id, service tag and
asset tag.

%package -n smbios-utils-python
Summary: Python executables that use libsmbios
Requires: python3-smbios = %{version}-%{release}
BuildArch: noarch

%description -n smbios-utils-python
Get BIOS information, such as System product name, product id, service tag and
asset tag. Set service and asset tags on Dell machines. Manipulate wireless
cards/bluetooth on Dell laptops. Set BIOS password on select Dell systems.
Update BIOS on select Dell systems. Set LCD brightness on select Dell laptops.

# name the devel package libsmbios-devel regardless of package name, per suse/fedora convention
%package -n libsmbios-devel
Summary: Development headers and archives
Requires: libsmbios = %{version}-%{release}

%description -n libsmbios-devel
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package contains the headers and .a files necessary to compile new client
programs against libsmbios.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libsmbios-2.4.3

find . -type d -exec chmod -f 755 {} \;
find doc src -type f -exec chmod -f 644 {} \;
chmod 755 src/cppunit/*.sh

%build
# this line lets us build an RPM directly from a git tarball
# and retains any customized version information we might have
[ -e ./configure ] || PACKAGE_VERSION=%{version} ./autogen.sh --no-configure

mkdir _build
cd _build
echo '../configure "$@"' > configure
chmod +x ./configure

%configure

mkdir -p out/libsmbios_c
%make_build CFLAGS+="%{optflags} -Werror" 2>&1 | tee build-%{_arch}.log

%check
runtest() {
    mkdir _$1$2
    pushd _$1$2
    ../configure
    make -e $1 CFLAGS="$CFLAGS -DDEBUG_OUTPUT_ALL"
    touch -r ../configure.ac
    make -e $1
    popd
}

VALGRIND="strace -f" runtest check strace > /dev/null || echo FAILED strace check
runtest valgrind > /dev/null || echo FAILED valgrind check
runtest check > /dev/null || echo FAILED check

%install
cd _build
TOPDIR=..
%make_install
rm -f %{buildroot}/%{_libdir}/lib*.{la,a}
find %{buildroot}/%{_includedir} out/libsmbios_c -exec touch -r $TOPDIR/configure.ac {} \;

rename %{pot_file}.mo %{lang_dom}.mo $(find %{buildroot}/%{_datadir} -name %{pot_file}.mo)
%find_lang %{lang_dom}

%ldconfig_scriptlets

%files -f _build/%{lang_dom}.lang
# Only need to include license once here
%license COPYING-GPL COPYING-OSL
%{_libdir}/libsmbios_c.so.*

%files -n libsmbios-devel
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%doc _build/out/libsmbios_c
%{_includedir}/smbios_c
%{_libdir}/libsmbios_c.so
%{_libdir}/pkgconfig/*.pc

%files -n smbios-utils

%files -n smbios-utils-bin
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%{_sbindir}/smbios-state-byte-ctl
%{_mandir}/man?/smbios-state-byte-ctl.*
%{_sbindir}/smbios-get-ut-data
%{_mandir}/man?/smbios-get-ut-data.*
%{_sbindir}/smbios-upflag-ctl
%{_mandir}/man?/smbios-upflag-ctl.*
%{_sbindir}/smbios-sys-info-lite
%{_mandir}/man?/smbios-sys-info-lite.*

%files -n python3-smbios
%{python3_sitearch}/*

%files -n smbios-utils-python
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%dir %{_sysconfdir}/libsmbios
%config(noreplace) %{_sysconfdir}/libsmbios/*

# python utilities
%{_sbindir}/smbios-battery-ctl
%{_mandir}/man?/smbios-battery-ctl.*
%{_sbindir}/smbios-sys-info
%{_mandir}/man?/smbios-sys-info.*
%{_sbindir}/smbios-token-ctl
%{_mandir}/man?/smbios-token-ctl.*
%{_sbindir}/smbios-passwd
%{_mandir}/man?/smbios-passwd.*
%{_sbindir}/smbios-wakeup-ctl
%{_mandir}/man?/smbios-wakeup-ctl.*
%{_sbindir}/smbios-wireless-ctl
%{_mandir}/man?/smbios-wireless-ctl.*
%{_sbindir}/smbios-lcd-brightness
%{_mandir}/man?/smbios-lcd-brightness.*
%{_sbindir}/smbios-keyboard-ctl
%{_mandir}/man?/smbios-keyboard-ctl.*
%{_sbindir}/smbios-thermal-ctl
%{_mandir}/man?/smbios-thermal-ctl.*

# data files
%{_datadir}/smbios-utils

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.3-22
- Import
