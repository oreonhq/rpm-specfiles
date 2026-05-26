Summary: Spell checker
Name: aspell
Version: 0.60.8.1
Release: 7%{?dist}
Epoch: 12
# LGPLv2+ .. common/gettext.h
# LGPLv2  .. modules/speller/default/phonet.hpp,
#            modules/speller/default/phonet.cpp,
#            modules/speller/default/affix.cpp
# GPLv2+  .. ltmain.sh, misc/po-filter.c
# BSD     .. myspell/munch.c
License: LGPL-2.0-or-later AND LGPL-2.1-only AND GPL-2.0-or-later AND BSD-2-Clause
URL: http://aspell.net/
Source: https://ftp.gnu.org/gnu/aspell/aspell-%{version}.tar.gz

Patch0: aspell-0.60.7-fileconflict.patch
Patch1: aspell-0.60.7-pspell_conf.patch
Patch2: aspell-0.60.7-mp.patch
# https://github.com/GNUAspell/aspell/commit/ee6cbb1.patch
Patch3: aspell-0.60.8-gcc15.patch
# oreon url source checksums begin
%global source0_sha256 d6da12b34d42d457fa604e435ad484a74b2effcd120ff40acd6bb3fb2887d21b
%global source0_file aspell-0.60.8.1.tar.gz
# oreon url source checksums end

# IMPORTANT
# This package has been deprecated since Fedora 39
# The reason behind this was that there were no upstream releases for 4 years
# and there are other variants like hunspell or enchant which had active upstream
# FESCo approval is located here: https://pagure.io/fesco/issue/3009
# Change proposal is located here: https://fedoraproject.org/wiki/Changes/AspellDeprecation
Provides:  deprecated()

BuildRequires: gcc-c++
BuildRequires: chrpath, gettext, ncurses-devel, pkgconfig, perl-interpreter
BuildRequires: make

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

# For details, see above
Provides:  deprecated()

%description devel
The aspell-devel package includes libraries
and header files needed for Aspell development.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/aspell-0.60.8.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d6da12b34d42d457fa604e435ad484a74b2effcd120ff40acd6bb3fb2887d21b" || { echo "oreon: Source0 SHA256 mismatch for aspell-0.60.8.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1 -b .fc
%patch -P1 -p1 -b .mlib
%patch -P2 -p1 -b .ai
%patch -P3 -p1 -b .gcc15

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

%files -f %{name}.lang
%doc README TODO COPYING examples/aspell-import examples/aspell-import.1
%dir %{_libdir}/aspell-0.60
%{_bindir}/a*
%{_bindir}/ispell
%{_bindir}/pr*
%{_bindir}/run-with-aspell
%{_bindir}/spell
%{_bindir}/word-list-compress
%{_libdir}/lib*.so.*
%{_libdir}/aspell-0.60/*
%{_infodir}/aspell.*
%{_mandir}/man1/aspell.1.*
%{_mandir}/man1/run-with-aspell.1*
%{_mandir}/man1/word-list-compress.1*
%{_mandir}/man1/prezip-bin.1.*

%files devel
%dir %{_includedir}/pspell
%{_bindir}/pspell-config
%{_includedir}/aspell.h
%{_includedir}/pspell/pspell.h
%{_libdir}/lib*spell.so
%{_libdir}/pkgconfig/*
%{_infodir}/aspell-dev.*
%{_mandir}/man1/pspell-config.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.60.8.1-7
- Prepare for Oreon 11 (RP1)
