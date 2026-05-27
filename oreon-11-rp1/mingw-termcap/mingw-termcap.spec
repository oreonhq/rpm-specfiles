%global source0_hash none

# Note: Termcap was deprecated and removed from Fedora after F-8.  It
# has been replaced by ncurses.  However ncurses cannot be compiled on
# Windows so we have to supply termcap.  In addition, the last stand-
# alone Fedora termcap package was actually just /etc/termcap from
# ncurses.  So here we are using the GNU termcap library which is
# regretably GPL'd.

%?mingw_package_header

%global mingw_build_win32 1
%global mingw_build_win64 1

Name:           mingw-termcap
Version:        1.3.1
Release:        40%{?dist}
Summary:        MinGW terminal feature database

License:        GPL-2.0-or-later
URL:            ftp://ftp.gnu.org/gnu/termcap/
Source0:        ftp://ftp.gnu.org/gnu/termcap/termcap-%{version}.tar.gz
# Fix implicit function declarations
Patch0:         termcap-1.3.1-implicit.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  autoconf


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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n termcap-%{version}
%patch -P0 -p1

# Packaged script doesn't understand --bindir, so rebuild:
autoconf


%build
%mingw_configure
%mingw_make %{?_smp_mflags} CFLAGS="$CFLAGS -std=gnu89"

# Build a shared library.  No need for -fPIC on Windows.
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
# We can't use the %%mingw_make_install macro here as
# the Makefile doesn't support the DESTDIR=... flag
make install -C build_win32 \
  prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
  exec_prefix=$RPM_BUILD_ROOT%{mingw32_prefix} \
  oldincludedir=
make install -C build_win64 \
  prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
  exec_prefix=$RPM_BUILD_ROOT%{mingw64_prefix} \
  oldincludedir=

# Move the shared library to the correct locations.
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
install -m 0755 build_win32/libtermcap-0.dll $RPM_BUILD_ROOT%{mingw32_bindir}
install -m 0755 build_win32/libtermcap.dll.a $RPM_BUILD_ROOT%{mingw32_libdir}

mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
install -m 0755 build_win64/libtermcap-0.dll $RPM_BUILD_ROOT%{mingw64_bindir}
install -m 0755 build_win64/libtermcap.dll.a $RPM_BUILD_ROOT%{mingw64_libdir}

# Move the info files to the correct location.
mkdir -p $RPM_BUILD_ROOT%{mingw32_infodir}
mv $RPM_BUILD_ROOT%{mingw32_prefix}/info/* $RPM_BUILD_ROOT%{mingw32_infodir}

mkdir -p $RPM_BUILD_ROOT%{mingw64_infodir}
mv $RPM_BUILD_ROOT%{mingw64_prefix}/info/* $RPM_BUILD_ROOT%{mingw64_infodir}



%files -n mingw32-termcap
%doc COPYING
%{mingw32_bindir}/libtermcap-0.dll
%{mingw32_libdir}/libtermcap.dll.a
%{mingw32_includedir}/termcap.h
# Note that we want the info files in this package because
# there is no equivalent native Fedora package.
%{mingw32_infodir}/*

%files -n mingw32-termcap-static
%{mingw32_libdir}/libtermcap.a

%files -n mingw64-termcap
%doc COPYING
%{mingw64_bindir}/libtermcap-0.dll
%{mingw64_libdir}/libtermcap.dll.a
%{mingw64_includedir}/termcap.h
%{mingw64_infodir}/*

%files -n mingw64-termcap-static
%{mingw64_libdir}/libtermcap.a


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.1-40
- Import
