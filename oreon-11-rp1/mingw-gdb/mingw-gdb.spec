%global source0_hash 1c036c0d72e4b3d1fb5c94c88632add6f9d76f4d7c4d2ea793c12a9f19a3228c
%{?mingw_package_header}
Name:           mingw-gdb
Version:        17.2
Release:        1%{?dist}
Summary:        MinGW Windows port of the GDB debugger
License:        GPL-3.0-or-later AND BSD-3-Clause AND FSFAP AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later AND LGPL-2.0-or-later WITH GCC-exception-2.0 AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNU-compiler-exception
URL:            http://gnu.org/software/gdb/
Source0:        https://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz
BuildArch:      noarch
Provides: bundled(libiberty)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-mpfr
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-mpfr
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  texinfo
# /oreon:deps
%description
This is the MinGW Windows port of the GDB, the GNU debugger.

# Win32
%package -n mingw32-gdb
Summary:        MinGW Windows port of the GDB debugger
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
%global oreon_srcdir gdb-%{version}
%oreon_prep
%build

%mingw_configure
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/locale/
rm -rf %{buildroot}%{mingw32_includedir}/
rm -rf %{buildroot}%{mingw32_libdir}/
rm -rf %{buildroot}%{mingw64_datadir}/locale/
rm -rf %{buildroot}%{mingw64_includedir}/
rm -rf %{buildroot}%{mingw64_libdir}/
rm -rf %{buildroot}%{mingw32_datadir}/info/
rm -rf %{buildroot}%{mingw32_mandir}/
rm -rf %{buildroot}%{mingw64_datadir}/info/
rm -rf %{buildroot}%{mingw64_mandir}/
rm %{buildroot}%{mingw64_bindir}/{gdb-add-index,gstack}
rm %{buildroot}%{mingw32_bindir}/{gdb-add-index,gstack}
%oreon_autofiles mingw32-gdb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gdb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gdb -f %{oreon_filedir}/mingw32-gdb.list
%files -n mingw64-gdb -f %{oreon_filedir}/mingw64-gdb.list

%changelog

%autochangelog
