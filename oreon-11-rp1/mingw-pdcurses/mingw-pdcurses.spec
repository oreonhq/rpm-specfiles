%global source0_hash b88356684aa3e77069f07d8cfb1d35b6d146d1b1c711ad41fa56edc6ea046446

%?mingw_package_header

Name:           mingw-pdcurses
Version:        3.8
Release:        16%{?dist}
Summary:        Curses library for MinGW

License:        LicenseRef-Fedora-Public-Domain
URL:            http://pdcurses.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pdcurses/PDCurses-%{version}.tar.gz

BuildArch:      noarch

Patch0001:      0001-build-sys-add-WINDRES-variable.patch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

# For applying patches.
BuildRequires:  git

%?mingw_debug_package

%description
PDCurses is a public domain curses library for DOS, OS/2, Win32, X11
and SDL, implementing most of the functions available in X/Open and
System V R4 curses. It supports many compilers for these
platforms. The X11 port lets you recompile existing text-mode curses
programs to produce native X11 applications.

Note that ncurses is not available for MinGW / Windows.  Applications
which need curses functionality can use this package, provided they
don't use any of the extensions specific to ncurses.


%package -n mingw32-pdcurses
Summary:        Curses library for MinGW32

%description -n mingw32-pdcurses
PDCurses is a public domain curses library for DOS, OS/2, Win32, X11
and SDL, implementing most of the functions available in X/Open and
System V R4 curses. It supports many compilers for these
platforms. The X11 port lets you recompile existing text-mode curses
programs to produce native X11 applications.

Note that ncurses is not available for MinGW / Windows.  Applications
which need curses functionality can use this package, provided they
don't use any of the extensions specific to ncurses.

%package -n mingw64-pdcurses
Summary:        Curses library for MinGW64

%description -n mingw64-pdcurses
PDCurses is a public domain curses library for DOS, OS/2, Win32, X11
and SDL, implementing most of the functions available in X/Open and
System V R4 curses. It supports many compilers for these
platforms. The X11 port lets you recompile existing text-mode curses
programs to produce native X11 applications.

Note that ncurses is not available for MinGW / Windows.  Applications
which need curses functionality can use this package, provided they
don't use any of the extensions specific to ncurses.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git_am -n PDCurses-%{version}

cp -a wincon win32
cp -a wincon win64

%build
pushd win32
make \
  CC=%{mingw32_cc} \
  LINK=%{mingw32_cc} \
  STRIP=%{mingw32_strip} \
  WINDRES=%{mingw32_windres} \
  WIDE=Y UTF8=Y DLL=Y
popd

pushd win64
make \
  CC=%{mingw64_cc} \
  LINK=%{mingw64_cc} \
  STRIP=%{mingw64_strip} \
  WINDRES=%{mingw64_windres} \
  WIDE=Y UTF8=Y DLL=Y
popd

%install
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_libdir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir}

install win32/pdcurses.dll $RPM_BUILD_ROOT%{mingw32_bindir}/pdcurses.dll
install win32/pdcurses.a $RPM_BUILD_ROOT%{mingw32_libdir}/libpdcurses.dll.a
install -m 0644 curses.h panel.h $RPM_BUILD_ROOT%{mingw32_includedir}


mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_libdir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_includedir}

install win64/pdcurses.dll $RPM_BUILD_ROOT%{mingw64_bindir}/pdcurses.dll
install win64/pdcurses.a $RPM_BUILD_ROOT%{mingw64_libdir}/libpdcurses.dll.a
install -m 0644 curses.h panel.h $RPM_BUILD_ROOT%{mingw64_includedir}


%files -n mingw32-pdcurses
%{mingw32_bindir}/pdcurses.dll
%{mingw32_libdir}/libpdcurses.dll.a
%{mingw32_includedir}/curses.h
%{mingw32_includedir}/panel.h

%files -n mingw64-pdcurses
%{mingw64_bindir}/pdcurses.dll
%{mingw64_libdir}/libpdcurses.dll.a
%{mingw64_includedir}/curses.h
%{mingw64_includedir}/panel.h


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.8-16
- Prepare for Oreon 11 (RP1)
