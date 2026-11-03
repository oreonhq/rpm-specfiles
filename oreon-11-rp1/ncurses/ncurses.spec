%global source0_hash 355b4cbbed880b0381a04c46617b7656e362585d52e9cf84a67e2009b749ff11
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: ncurses
Version: 6.6
Release: 5%{?dist}
Summary: ncurses (new curses)
License: MIT
URL: https://invisible-island.net/ncurses/
Source0: https://ftp.gnu.org/gnu/ncurses/ncurses-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

Requires: ncurses-libs%{?_isa} = %{version}-%{release}


%description
The ncurses (new curses) library is a free software emulation of curses in System V Release 4.0 (SVr4), and more. It uses terminfo format, supports pads and color and multiple highlights and forms characters and function-key mapping, and has all the other SVr4-curses enhancements over BSD curses.

%package base
Summary: Descriptions of common terminals
BuildArch: noarch

%description base
Terminfo database and tab set files used by ncurses.

%package libs
Summary: ncurses libraries
Requires: ncurses-base = %{version}-%{release}

%description libs
Shared ncursesw, formw, menuw, panelw, and tinfo libraries.

%package devel
Summary: Development files for ncurses
Requires: ncurses-libs%{?_isa} = %{version}-%{release}

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

rm -rf %{_builddir}/ncurses-tinfo
mkdir -p %{_builddir}/ncurses-tinfo
tar -xzf %{SOURCE0} -C %{_builddir}/ncurses-tinfo --strip-components=1
cd %{_builddir}/ncurses-tinfo
CFLAGS='%{_oreon_cflags}' LDFLAGS='%{_oreon_ldflags}' \
  ./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --with-shared \
  --without-normal \
  --without-debug \
  --without-cxx \
  --without-ada \
  --without-manpages \
  --without-progs \
  --without-tests \
  --with-termlib=tinfo \
  --disable-widec
make -j1
mkdir -p %{_builddir}/ncurses-tinfo-root
make install.libs DESTDIR=%{_builddir}/ncurses-tinfo-root
cp -a %{_builddir}/ncurses-tinfo-root%{_libdir}/libtinfo.so* %{buildroot}%{_libdir}/
cd %{_builddir}/ncurses-%{version}

rm -f %{buildroot}%{_libdir}/pkgconfig/ncurses++w.pc

%ldconfig_scriptlets libs

%files
%license COPYING
%{_bindir}/captoinfo
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/infotocap
%{_bindir}/reset
%{_bindir}/tabs
%{_bindir}/tic
%{_bindir}/toe
%{_bindir}/tput
%{_bindir}/tset
%{_mandir}/man1/captoinfo.1m*
%{_mandir}/man1/clear.1*
%{_mandir}/man1/infocmp.1m*
%{_mandir}/man1/infotocap.1m*
%{_mandir}/man1/reset.1*
%{_mandir}/man1/tabs.1*
%{_mandir}/man1/tic.1m*
%{_mandir}/man1/toe.1m*
%{_mandir}/man1/tput.1*
%{_mandir}/man1/tset.1*
%{_mandir}/man5/scr_dump.5*
%{_mandir}/man5/term.5*
%{_mandir}/man5/terminfo.5*
%{_mandir}/man5/user_caps.5*
%{_mandir}/man7/term.7*

%files base
%license COPYING
%{_datadir}/terminfo/
%{_datadir}/tabset/
%{_prefix}/lib/terminfo

%files libs
%license COPYING
%{_libdir}/libformw.so.6
%{_libdir}/libformw.so.6.*
%{_libdir}/libmenuw.so.6
%{_libdir}/libmenuw.so.6.*
%{_libdir}/libncursesw.so.6
%{_libdir}/libncursesw.so.6.*
%{_libdir}/libpanelw.so.6
%{_libdir}/libpanelw.so.6.*
%{_libdir}/libtinfo.so.6
%{_libdir}/libtinfo.so.6.*

%files devel
%{_bindir}/ncursesw6-config
%{_includedir}/*.h
%{_libdir}/libformw.so
%{_libdir}/libmenuw.so
%{_libdir}/libncursesw.so
%{_libdir}/libpanelw.so
%{_libdir}/libtinfo.so
%{_libdir}/pkgconfig/formw.pc
%{_libdir}/pkgconfig/menuw.pc
%{_libdir}/pkgconfig/ncursesw.pc
%{_libdir}/pkgconfig/panelw.pc
%{_mandir}/man1/ncursesw6-config.1*
%{_mandir}/man3/*.3*
