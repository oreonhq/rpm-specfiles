%global source0_hash fe5383204467828cd495ee8d1d3c037a7eba1389c22bc6a041f627976f9061cc
%{?mingw_package_header}
Name:           mingw-readline
Version:        8.3
Release:        3%{?dist}
Summary:        MinGW port of readline for editing typed command lines
License:        GPL-2.0-or-later
URL:            https://tiswww.case.edu/php/chet/readline/rltop.html
Source0:        https://mirrors.kernel.org/gnu/readline/readline-%{version}.tar.gz
Patch1:         readline-8.0-shlib.patch
Patch2:         readline_mingw.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-termcap
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-termcap
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir readline-%{version}
%oreon_prep
%build

export MINGW32_CFLAGS="%{mingw32_cflags} -D_POSIX -D__USE_MINGW_ALARM=1"
export MINGW64_CFLAGS="%{mingw64_cflags} -D_POSIX -D__USE_MINGW_ALARM=1"
%mingw_configure --enable-shared
%mingw_make SHLIB_LIBS=-ltermcap
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_infodir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_infodir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -f %{buildroot}%{mingw32_datadir}/readline/*.c
rm -f %{buildroot}%{mingw64_datadir}/readline/*.c
%oreon_autofiles mingw32-readline usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-readline-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-readline usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-readline-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-readline -f %{oreon_filedir}/mingw32-readline.list
%files -n mingw32-readline-static -f %{oreon_filedir}/mingw32-readline-static.list
%files -n mingw64-readline -f %{oreon_filedir}/mingw64-readline.list
%files -n mingw64-readline-static -f %{oreon_filedir}/mingw64-readline-static.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3-3
- Import
