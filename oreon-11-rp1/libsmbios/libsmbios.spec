%global source0_hash 36c36a0f6b59190d6b4fef11696886e4511091929a5eb7ae7cf5fea0c32d3f58
%define pot_file  libsmbios
%define lang_dom  libsmbios-2.4
Name: libsmbios
Version: 2.4.3
Release:        22%{?dist}
Summary:        Libsmbios C/C++ shared libraries
License: GPL-2.0-or-later or OSL-2.1
URL: https://github.com/dell/libsmbios
Source0:        https://github.com/dell/libsmbios/archive/refs/tags/v%{version}.tar.gz#/libsmbios-%{version}.tar.gz
ExclusiveArch: x86_64 %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  strace
BuildRequires:  valgrind
# /oreon:deps
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
%oreon_autofiles python3-smbios usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles smbios-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles smbios-utils-bin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles smbios-utils-python usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libsmbios-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n python3-smbios -f %{oreon_filedir}/python3-smbios.list
%files -n smbios-utils -f %{oreon_filedir}/smbios-utils.list
%files -n smbios-utils-bin -f %{oreon_filedir}/smbios-utils-bin.list
%files -n smbios-utils-python -f %{oreon_filedir}/smbios-utils-python.list
%files -n libsmbios-devel -f %{oreon_filedir}/libsmbios-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.3-22
- Import
