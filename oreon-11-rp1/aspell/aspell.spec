%global source0_hash 57fe4863eae6048f72245a8575b44b718fb85ca14b9f8c0afc41b254dfd76919
Summary:        Spell checker
Name: aspell
Version: 0.60.8.2
Release:        1%{?dist}
Epoch: 12
License: LGPL-2.0-or-later AND LGPL-2.1-only AND GPL-2.0-or-later AND BSD-2-Clause
URL: http://aspell.net/
Source0:        https://mirrors.kernel.org/gnu/aspell/aspell-%{version}.tar.gz
Patch0: aspell-0.60.7-fileconflict.patch
Patch1: aspell-0.60.7-pspell_conf.patch
Patch2: aspell-0.60.7-mp.patch
Provides:  deprecated()
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
# /oreon:deps
%description
GNU Aspell is a spell checker designed to eventually replace Ispell. It can
either be used as a library or as an independent spell checker. Its main
feature is that it does a much better job of coming up with possible
suggestions than just about any other spell checker out there for the
English language, including Ispell and Microsoft Word. It also has many
other technical enhancements over Ispell such as using shared memory for
dictionaries and intelligently handling personal dictionaries when more
than one Aspell process is open at once.

%package devel
Summary: Libraries and header files for Aspell development
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: pkgconfig
Provides:  deprecated()
%description devel
The aspell-devel package includes libraries
and header files needed for Aspell development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .fc
%patch -P1 -p1 -b .mlib
%patch -P2 -p1 -b .ai

iconv -f iso-8859-2 -t utf-8 < manual/aspell.info > manual/aspell.info.aux
mv manual/aspell.info.aux manual/aspell.info

%build

%configure --disable-rpath
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
cp scripts/aspell-import examples/aspell-import
chmod 644 examples/aspell-import
cp manual/aspell-import.1 examples/aspell-import.1
%install
%make_install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60
mv ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/ispell ${RPM_BUILD_ROOT}%{_bindir}
mv ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/spell ${RPM_BUILD_ROOT}%{_bindir}
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//nroff-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//sgml-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//context-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//email-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//tex-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//texinfo-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60//markdown-filter.so
chrpath --delete ${RPM_BUILD_ROOT}%{_bindir}/aspell
chrpath --delete ${RPM_BUILD_ROOT}%{_libdir}/libpspell.so.*
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libaspell.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libpspell.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/aspell-0.60/*-filter.la
rm -f ${RPM_BUILD_ROOT}%{_bindir}/aspell-import
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/aspell-import.1
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir
%find_lang %{name}
%oreon_autofiles aspell-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n aspell-devel -f %{oreon_filedir}/aspell-devel.list

%changelog

%autochangelog
