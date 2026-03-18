%{?mingw_package_header}

Name:           mingw-readline
Version:        8.3
Release:        3%{?dist}
Summary:        MinGW port of readline for editing typed command lines

License:        GPL-2.0-or-later
URL:            https://tiswww.case.edu/php/chet/readline/rltop.html
Source0:        https://git.savannah.gnu.org/cgit/readline.git/snapshot/readline-%{version}.tar.gz

# Remove RPATH, use CFLAGS
Patch1:         readline-8.0-shlib.patch
# Fix mingw build
Patch2:         readline_mingw.patch

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-termcap

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-termcap


%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.


# Win32
%package -n mingw32-readline
Summary:        MinGW port of readline for editing typed command lines

%description -n mingw32-readline
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.

%package -n mingw32-readline-static
Summary:        Static version of the cross compiled readline library
Requires:       mingw32-readline = %{version}-%{release}

%description -n mingw32-readline-static
Static version of the cross compiled readline library.

# Win64
%package -n mingw64-readline
Summary:        MinGW port of readline for editing typed command lines

%description -n mingw64-readline
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.

%package -n mingw64-readline-static
Summary:        Static version of the cross compiled readline library
Requires:       mingw64-readline = %{version}-%{release}

%description -n mingw64-readline-static
Static version of the cross compiled readline library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n readline-%{version}


%build
export MINGW32_CFLAGS="%{mingw32_cflags} -D_POSIX -D__USE_MINGW_ALARM=1"
export MINGW64_CFLAGS="%{mingw64_cflags} -D_POSIX -D__USE_MINGW_ALARM=1"
%mingw_configure --enable-shared
%mingw_make SHLIB_LIBS=-ltermcap


%install
%mingw_make_install

# Don't want the info files or manpages which duplicate the native package.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_infodir}

rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_infodir}

rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}

# The examples also duplicate the native package so they can be removed as well
rm -f %{buildroot}%{mingw32_datadir}/readline/*.c
rm -f %{buildroot}%{mingw64_datadir}/readline/*.c


# Win32
%files -n mingw32-readline
%license COPYING
%{mingw32_bindir}/libreadline8.dll
%{mingw32_bindir}/libhistory8.dll
%{mingw32_libdir}/libreadline.dll.a
%{mingw32_libdir}/libhistory.dll.a
%{mingw32_libdir}/pkgconfig/history.pc
%{mingw32_libdir}/pkgconfig/readline.pc
%{mingw32_includedir}/readline/

%files -n mingw32-readline-static
%{mingw32_libdir}/libhistory.a
%{mingw32_libdir}/libreadline.a

# Win64
%files -n mingw64-readline
%license COPYING
%{mingw64_bindir}/libreadline8.dll
%{mingw64_bindir}/libhistory8.dll
%{mingw64_libdir}/libreadline.dll.a
%{mingw64_libdir}/libhistory.dll.a
%{mingw64_libdir}/pkgconfig/history.pc
%{mingw64_libdir}/pkgconfig/readline.pc
%{mingw64_includedir}/readline/

%files -n mingw64-readline-static
%{mingw64_libdir}/libhistory.a
%{mingw64_libdir}/libreadline.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3-3
- Prepare for Oreon 11 (RP1)
