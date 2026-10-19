%global source0_hash 66ec82a577395fe9d471504267e6dd04615c76517c61af7c6b9c19e5e34e73c8
%define double_profiling_build 1
Name:      hunspell
Summary:        A spell checker and morphological analyzer library
Version:   1.7.4
Release:        1%{?dist}
Source0:        https://github.com/hunspell/hunspell/releases/download/v%{version}/hunspell-%{version}.tar.gz
URL:       https://github.com/hunspell/hunspell
License:   LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-1.1
%ifarch %{ix86} x86_64
%endif
%if %{double_profiling_build}
%endif
Requires:  hunspell-en-US
Requires:  hunspell-filesystem = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
BuildRequires:  words
# /oreon:deps
%description
Hunspell is a spell checker and morphological analyzer library and program
designed for languages with rich morphology and complex word compounding or
character encoding. Hunspell interfaces: Ispell-like terminal interface using
Curses library, Ispell pipe interface, LibreOffice UNO module.

%package devel
Requires: hunspell = %{version}-%{release}, pkgconfig
Summary: Files for developing with hunspell
%description devel
Includes and definitions for developing with hunspell

%package filesystem
Summary: Hunspell filesystem layout
%description filesystem
Provides a directory in which to store dictionaries provided by other
packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vfi
configureflags="--disable-rpath --disable-static --with-ui --with-readline"
%define profilegenerate \
    CFLAGS="${RPM_OPT_FLAGS} -fprofile-generate"\
    CXXFLAGS="${RPM_OPT_FLAGS} -fprofile-generate"
%define profileuse \
    CFLAGS="${RPM_OPT_FLAGS} -fprofile-use"\
    CXXFLAGS="${RPM_OPT_FLAGS} -fprofile-use"
%if !%{double_profiling_build}
%configure $configureflags
%make_build
%else
head -n $((`cat /usr/share/dict/words | wc -l`/2)) /usr/share/dict/words |\
    sed '/\//d'> words
%{profilegenerate} %configure $configureflags
%make_build
./src/tools/affixcompress words > /dev/null 2>&1
./src/tools/hunspell -d words -l /usr/share/dict/words > /dev/null
make check
make distclean
%{profileuse} %configure $configureflags
%make_build
%endif
%check

%ifarch %{ix86} x86_64
VALGRIND=memcheck make check
make check
%endif
%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
mkdir $RPM_BUILD_ROOT/%{_datadir}/hunspell
mkdir $RPM_BUILD_ROOT/%{_datadir}/myspell
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hunspell-devel -f %{oreon_filedir}/hunspell-devel.list
%files -n hunspell-filesystem -f %{oreon_filedir}/hunspell-filesystem.list

%changelog

%autochangelog
