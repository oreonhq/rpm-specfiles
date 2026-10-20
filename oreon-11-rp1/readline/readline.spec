%global source0_hash fe5383204467828cd495ee8d1d3c037a7eba1389c22bc6a041f627976f9061cc
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: readline
Version: 8.3.6
Release: 1%{?dist}
Summary: GNU Readline
License: GPL-3.0-or-later
URL: https://tiswww.case.edu/php/chet/readline/rltop.html
Source0: https://ftp.gnu.org/gnu/readline/readline-8.3.tar.gz
Patch1: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-001
Patch2: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-002
Patch3: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-003
Patch4: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-004
Patch5: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-005
Patch6: https://ftp.gnu.org/gnu/readline/readline-8.3-patches/readline83-006

BuildRequires: oreon-rpm-macros
BuildRequires: ncurses-devel
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
The Readline library provides a set of functions for use by applications that allow users to edit command lines as they are typed in. Both Emacs and vi editing modes are available. The Readline library includes additional functions to maintain a list of previously-entered command lines, to recall and perhaps reedit those lines, and perform csh-like history expansion on previous commands.

The history facilities are also placed into a separate library, the History library, as part of the build process. The History library may be used without Readline in applications which desire its capabilities.

%package devel
Summary: GNU Readline
Requires: readline%{?_isa} = %{version}-%{release}
Provides: pkgconfig(readline)
Provides: pkgconfig(history)

%description devel
The Readline library provides a set of functions for use by applications that allow users to edit command lines as they are typed in. Both Emacs and vi editing modes are available. The Readline library includes additional functions to maintain a list of previously-entered command lines, to recall and perhaps reedit those lines, and perform csh-like history expansion on previous commands.

The history facilities are also placed into a separate library, the History library, as part of the build process. The History library may be used without Readline in applications which desire its capabilities.

%prep
%oreon_sha256
%autosetup -n readline-8.3 -p0
sed -i 's|-Wl,-rpath,$(libdir) ||' support/shobj-conf

%build
%oreon_configure --disable-static --with-curses
%oreon_make SHLIB_LIBS=-lncursesw

%install
%oreon_make_install SHLIB_LIBS=-lncursesw
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir

%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
