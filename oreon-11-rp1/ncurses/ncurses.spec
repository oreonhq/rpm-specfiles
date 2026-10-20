%global source0_hash 355b4cbbed880b0381a04c46617b7656e362585d52e9cf84a67e2009b749ff11
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ncurses
Version: 6.6
Release: 1%{?dist}
Summary: ncurses (new curses)
License: MIT
URL: https://invisible-island.net/ncurses/
Source0: https://ftp.gnu.org/gnu/ncurses/ncurses-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

Provides: ncurses-libs = %{version}-%{release}
Obsoletes: ncurses-libs < %{version}-%{release}

%description
The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. It uses terminfo format, supports pads and color and multiple highlights and forms characters and function-key mapping, and has all the other SVr4-curses enhancements over BSD curses.

%package devel
Summary: ncurses (new curses)
Requires: ncurses%{?_isa} = %{version}-%{release}
Provides: pkgconfig(ncursesw)
Provides: pkgconfig(formw)
Provides: pkgconfig(menuw)
Provides: pkgconfig(panelw)
Provides: pkgconfig(tinfow)

%description devel
The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. It uses terminfo format, supports pads and color and multiple highlights and forms characters and function-key mapping, and has all the other SVr4-curses enhancements over BSD curses.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --with-shared --without-normal --without-debug --enable-widec --enable-pc-files --with-pkg-config-libdir=%{_libdir}/pkgconfig --without-ada --without-tests
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.a %{buildroot}%{_libdir}/*.la

%oreon_filelist_devel

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
