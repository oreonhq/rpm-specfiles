%global source0_hash none

%{?mingw_package_header}

Name:           mingw-gdb
Version:        17.1
Release:        2%{?dist}
Summary:        MinGW Windows port of the GDB debugger

# Same License tag as the native gdb package has:
License:        GPL-3.0-or-later AND BSD-3-Clause AND FSFAP AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later AND LGPL-2.0-or-later WITH GCC-exception-2.0 AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNU-compiler-exception
URL:            http://gnu.org/software/gdb/
Source0:        https://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  automake autoconf libtool
BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-mpfr
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-mpfr
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib

BuildRequires:  texinfo

Provides: bundled(libiberty)

%description
This is the MinGW Windows port of the GDB, the GNU debugger.

# Win32
%package -n mingw32-gdb
Summary:        MinGW Windows port of the GDB debugger
# Provide upgrade path for the gdb packages distributed at
# http://mingw-cross.sourceforge.net
Obsoletes:      mingw32-gdb-gdbserver < 6.8.50.20090302-2

%description -n mingw32-gdb
This is the MinGW Windows port of the GDB, the GNU debugger.

# Win64
%package -n mingw64-gdb
Summary:        MinGW Windows port of the GDB debugger

%description -n mingw64-gdb
This is the MinGW Windows port of the GDB, the GNU debugger.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n gdb-%{version}

%build
%mingw_configure
%mingw_make_build

%install
%mingw_make_install

# Remove bfd and opcodes libraries
rm -rf %{buildroot}%{mingw32_datadir}/locale/
rm -rf %{buildroot}%{mingw32_includedir}/
rm -rf %{buildroot}%{mingw32_libdir}/

rm -rf %{buildroot}%{mingw64_datadir}/locale/
rm -rf %{buildroot}%{mingw64_includedir}/
rm -rf %{buildroot}%{mingw64_libdir}/

# Remove documentation which is duplicate with native gdb package
rm -rf %{buildroot}%{mingw32_datadir}/info/
rm -rf %{buildroot}%{mingw32_mandir}/

rm -rf %{buildroot}%{mingw64_datadir}/info/
rm -rf %{buildroot}%{mingw64_mandir}/

# Remove unusefull gdb-add-index, gstack scripts
rm %{buildroot}%{mingw64_bindir}/{gdb-add-index,gstack}
rm %{buildroot}%{mingw32_bindir}/{gdb-add-index,gstack}

%files -n mingw32-gdb
%license COPYING3 COPYING COPYING.LIB
%{mingw32_bindir}/gdb.exe
%{mingw32_bindir}/gdbserver.exe
%{mingw32_datadir}/gdb/

%files -n mingw64-gdb
%license COPYING3 COPYING COPYING.LIB
%{mingw64_bindir}/gdb.exe
%{mingw64_bindir}/gdbserver.exe
%{mingw64_datadir}/gdb/

%changelog
%autochangelog
