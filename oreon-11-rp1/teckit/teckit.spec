%global source0_hash none

Name:           teckit
Version:        2.5.13
Release:        2%{?dist}
Summary:        Encoding conversion library and mapping compiler
# COPYING:                      links to license/LICENSING.txt
# license/License_CPLv05.txt:   CPL-1.0 text, "0.5" version in the license
#                               title is irrelevant
#                               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/160>
# license/License_LGPLv21.txt:  LGPL-2.1 text
# license/LICENSING.txt:        license declarations
# SFconv/UtfCodec.cpp:      LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-2.0 (bundled Graphite2)
# SFconv/UtfCodec.h:        LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-2.0 (bundled Graphite2)
#                           MPL version clarified at <https://github.com/silnrsi/graphite/issues/58>,
# source/Engine.cpp:        LGPL-2.1-or-later OR CPL-1.0, CPL-1.0 identifier already
#                           encompases "or later" choice
#                           <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/160>
# source/TECkit_Format.h:   LGPL-2.1-or-later OR CPL-0.5-or-later
## Not in any binary package
# debian-src/copyright: LGPL-2.0-or-later
# perl_binaries:        precompiled source/Perl
# repackage.sh:         GPL-2.0-or-later
# SFconv/SFconv_ver.rc: LGPL-2.1-or-later OR CPL-0.5-or-later
# source/Compiler_ver.rc:   LGPL-2.1-or-later OR CPL-0.5-or-later
# source/Sample-tools/TECkit_Compile_ver.rc:    LGPL-2.1-or-later OR CPL-0.5-or-later
# source/Sample-tools/TxtConv_ver.rc:           LGPL-2.1-or-later OR CPL-0.5-or-later
# source/Sample-tools/version_defs.h:           LGPL-2.1-or-later OR CPL-0.5-or-later
# source/teckitjni/COPYING:     GPL-2.0 text
# source/teckitjni/java/org/sil/scripts/teckit/TecKitJni.java:  LGPL-2.1-or-later OR CPL-0.5-or-later
# source/teckitjni/ltmain.sh:   GPL-2.0-or-later WITH Autoconf-exception-generic
# source/teckitjni/missing:     GPL-2.0-or-later WITH Autoconf-exception-generic
# source/teckitjni/src/teckitjniTest.cpp:   GPL-2.0-or-later
# source/teckitjni/templates/cpp:           GPL-2.0-or-later
# source/teckitjni/templates/h:             GPL-2.0-or-later
# source/version_defs.h:        LGPL-2.1-or-later OR CPL-0.5-or-later
# test/NormalizationTest.txt:   Unicode-3.0
## Unbundled
# SFconv/expat/xmlparse/hashtable.c:    MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlparse/hashtable.h:    MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlparse/Makefile.in:    NPL-1.1
# SFconv/expat/xmlparse/makefile.win:   NPL-1.1
# SFconv/expat/xmlparse/xmlparse.c:     MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlparse/xmlparse.h:     MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/iasciitab.h:      MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/Makefile.in:      NPL-1.1
# SFconv/expat/xmltok/makefile.win:     NPL-1.1
# SFconv/expat/xmltok/utf8tab.h:        MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/xmldef.h:         MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/xmlrole.h:        MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/xmltok.h:         MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/xmltok_impl.c:    MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmltok/xmltok_impl.h:    MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/codepage.c:        MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/codepage.h:        MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/filemap.h:         MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/readfilemap.c:     MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/unixfilemap.c:     MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/win32filemap.c:    MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/xmlfile.c:         MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/xmlfile.h:         MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/xmltchar.h:        MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# SFconv/expat/xmlwf/xmlwf.c:           MPL-1.1 OR GPL-1.0-or-later (bundled expat)
# zlib-1.2.3:           "sse copyright notice in zlib.h"
# zlib-1.2.13/contrib/ada/*.adb:        "see zlib.ads"
# zlib-1.2.13/contrib/ada/zlib.ads:     GPL-2.0-or-later WITH GNAT-exception
# zlib-1.2.13/contrib/blast/blast.c:    "see blast.h"
# zlib-1.2.13/contrib/blast/blast.h:    Zlib
# zlib-1.2.13/contrib/dotzlib:  BSL-1.0
# zlib-1.2.13/contrib/gcc_gvmat64/gvmat64.S:    Zlib
# zlib-1.2.13/doc/rfc1950.txt:  ??? permissive
# zlib-1.2.13/zlib.h:    Zlib
## Removed when repackaging
# mac-installer/Resources/License.rtf:  "non-commercial"
#                                       <https://github.com/silnrsi/teckit/issues/34>
License:        (LGPL-2.1-or-later OR CPL-1.0) AND (LGPL-2.1-or-later OR GPL-2.0-or-later OR MPL-2.0)
SourceLicense:  %{license} AND LGPL-2.0-or-later AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Autoconf-exception-generic AND Unicode-3.0 AND (MPL-1.1 OR GPL-1.0-or-later) AND NPL-1.1 AND GPL-2.0-or-later WITH GNAT-exception AND Zlib AND BSL-1.0
URL:            https://software.sil.org/teckit/
# Archive repackaged with ./repackage.sh tool because of a bad license
# <https://github.com/silnrsi/teckit/issues/34>.
# Original URL is https://github.com/silnrsi/teckit/releases/download/v%%{version}/teckit-%%{version}.tar.xz
Source0:        teckit-%{version}_repackaged.tar.xz
Source1:        https://github.com/silnrsi/teckit/releases/download/v%{version}/teckit-%{version}.tar.xz.asc
# Exported from ppisar's keyring
Source2:        gpgkey-15D41BC02EB807D405EFFAF6C9183BEA0288CDEE.gpg
Source3:        repackage.sh
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake >= 1.11
BuildRequires:  coreutils
BuildRequires:  expat-devel
# gcc is not needed, the only source/NormalizationData.c is included into
# a C++ source/Engine.cpp compilation unit.
BuildRequires:  gcc-c++
# gnupg2 not used because of repackaging.
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  zlib-devel
# Tests:
BuildRequires:  perl-interpreter
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Provides:       bundels(graphite2)

%description
TECkit is a low-level toolkit intended to be used by other applications that
need to perform encoding conversions (e.g., when importing legacy data into
a Unicode-based application). The primary component of the TECkit package is
therefore a library that performs conversions; this is the "TECkit engine".
The engine relies on mapping tables in a specific binary format (for which
documentation is available); there is a compiler that creates such tables from
a human-readable mapping description (a simple text file).

%package devel
Summary:        Developmental files for TECkit library
License:        LGPL-2.1-or-later OR CPL-1.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files, pkg-config module, and documentation for developing application
that use TECkit, a character encoding and mapping, library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%dnl verification skipped because of repackaging
%dnl %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Remove bundled libraries
rm -r zlib-*/*.{c,h} SFconv/expat
# Remove pre-build executables
rm -r perl_binaries

%build
# Regenerate a build script
autoreconf -fi
%configure \
    --disable-debug \
    --disable-final \
    --without-old-lib-names \
    --disable-profile \
    --disable-profilefn \
    --enable-shared \
    --disable-static \
    --with-system-zlib \
    --disable-tetex-build
%{make_build}

%install
%{make_install}
rm -f %{buildroot}%{_libdir}/*.la

%check
%{make_build} check

%files
# COPYING is unhelpful
%license license/*
# ChangeLog is unhelpful
%doc AUTHORS NEWS README
%{_bindir}/sfconv
%{_bindir}/teckit_compile
%{_bindir}/txtconv
%{_libdir}/libTECkit.so.0
%{_libdir}/libTECkit.so.0.*
%{_libdir}/libTECkit_Compiler.so.0
%{_libdir}/libTECkit_Compiler.so.0.*
%{_mandir}/man1/sfconv.*
%{_mandir}/man1/teckit_compile.*
%{_mandir}/man1/txtconv.*

%files devel
%doc docs/*.pdf
%{_includedir}/teckit
%{_libdir}/libTECkit.so
%{_libdir}/libTECkit_Compiler.so
%{_libdir}/pkgconfig/teckit.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5.13-2
- Import
