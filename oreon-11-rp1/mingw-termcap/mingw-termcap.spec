%global source0_hash 91a0e22e5387ca4467b5bcb18edf1c51b930262fd466d5fda396dd9d26719100
%?mingw_package_header
%global mingw_build_win32 1
%global mingw_build_win64 1
Name:           mingw-termcap
Version:        1.3.1
Release:        1%{?dist}
Summary:        MinGW terminal feature database
License:        GPL-2.0-or-later
URL:            https://ftp.gnu.org/gnu/termcap/
Source0:        https://mirrors.kernel.org/gnu/termcap/termcap-%{version}.tar.gz
Patch0:         termcap-1.3.1-implicit.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
This is the GNU termcap library -- a library of C functions that
enable programs to send control strings to terminals in a way
independent of the terminal type.  The GNU termcap library does not
place an arbitrary limit on the size of termcap entries, unlike most
other termcap libraries.

This package contains libraries and development tools for the MinGW
cross-compiled version.

# Win32
%package -n mingw32-termcap
Summary:        MinGW terminal feature database
%description -n mingw32-termcap
This is the GNU termcap library -- a library of C functions that
enable programs to send control strings to terminals in a way
independent of the terminal type.  The GNU termcap library does not
place an arbitrary limit on the size of termcap entries, unlike most
other termcap libraries.

This package contains libraries and development tools for the MinGW
cross-compiled version.

%package -n mingw32-termcap-static
Summary:        Static version of the cross compiled termcap library
Requires:       mingw32-termcap = %{version}-%{release}
%description -n mingw32-termcap-static
Static version of the cross compiled termcap library.

# Win64
%package -n mingw64-termcap
Summary:        MinGW terminal feature database
%description -n mingw64-termcap
This is the GNU termcap library -- a library of C functions that
enable programs to send control strings to terminals in a way
independent of the terminal type.  The GNU termcap library does not
place an arbitrary limit on the size of termcap entries, unlike most
other termcap libraries.

This package contains libraries and development tools for the MinGW
cross-compiled version.

%package -n mingw64-termcap-static
Summary:        Static version of the cross compiled termcap library
Requires:       mingw64-termcap = %{version}-%{release}
%description -n mingw64-termcap-static
Static version of the cross compiled termcap library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n termcap-%{version}
%patch -P0 -p1

# Packaged script doesn't understand --bindir, so rebuild:
autoconf

%build

%mingw_configure
%mingw_make %{?_smp_mflags} CFLAGS="$CFLAGS -std=gnu89"
pushd build_win32
%{mingw32_cc} -shared \
  -Wl,--out-implib,libtermcap.dll.a \
  -o libtermcap-0.dll \
  termcap.o tparam.o version.o
popd
pushd build_win64
%{mingw64_cc} -shared \
  -Wl,--out-implib,libtermcap.dll.a \
  -o libtermcap-0.dll \
  termcap.o tparam.o version.o
popd
%install
make install -C build_win32 \
  prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
  exec_prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
  oldincludedir=
make install -C build_win64 \
  prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
  exec_prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
  oldincludedir=
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
install -m 0755 build_win32/libtermcap-0.dll $RPM_BUILD_ROOT%{mingw32_bindir}
install -m 0755 build_win32/libtermcap.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
install -m 0755 build_win64/libtermcap-0.dll $RPM_BUILD_ROOT%{mingw64_bindir}
install -m 0755 build_win64/libtermcap.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_infodir}
mv $RPM_BUILD_ROOT%{mingw32_prefix}/info/* $RPM_BUILD_ROOT%{mingw32_infodir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_infodir}
mv $RPM_BUILD_ROOT%{mingw64_prefix}/info/* $RPM_BUILD_ROOT%{mingw64_infodir}
%oreon_autofiles mingw32-termcap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-termcap-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-termcap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-termcap-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-termcap -f %{oreon_filedir}/mingw32-termcap.list
%files -n mingw32-termcap-static -f %{oreon_filedir}/mingw32-termcap-static.list
%files -n mingw64-termcap -f %{oreon_filedir}/mingw64-termcap.list
%files -n mingw64-termcap-static -f %{oreon_filedir}/mingw64-termcap-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-40
- Import
