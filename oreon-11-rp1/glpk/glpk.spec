%global source0_hash 4a1013eebb50f728fc601bdd833b0b2870333c3b3e5a816eeba921d95bec6f15

Name:           glpk
Version:        5.0
Release:        16%{?dist}
Summary:        GNU Linear Programming Kit

# GPL-3.0-or-later: the project as a whole
# MIT: the bundled minisat2 code
License:        GPL-3.0-or-later AND MIT
URL:            https://www.gnu.org/software/glpk/
Source0:        https://ftp.gnu.org/gnu/glpk/glpk-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/glpk/glpk-%{version}.tar.gz.sig
# Public key 0x5981E818, Andrew Makhorin <mao@mai2.rcnet.ru>
Source2:        gpgkey-D17BF2305981E818.gpg
# Un-bundle zlib (#1102855). Upstream won't accept; they want to be
# ANSI-compatible, and zlib makes POSIX assumptions.
Patch:          %{name}-4.65-unbundle-zlib.patch
# Unbundle suitesparse
Patch:          %{name}-4.65-unbundle-suitesparse.patch
# Fix violations of the ANSI C strict aliasing rules
Patch:          %{name}-4.65-alias.patch
# Do not define bool, true, or false for C23 compatibility
Patch:          %{name}-5.0-bool.patch
# Use zlib-ng directly instead of via the compatibility interface
Patch:          %{name}-5.0-zlib-ng.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gmp-devel
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  pkgconfig(libiodbc)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  suitesparse-devel

Provides:       bundled(minisat) = 1.14.1

%description
The GLPK (GNU Linear Programming Kit) package is intended for solving
large-scale linear programming (LP), mixed integer programming (MIP), and
other related problems. It is a set of routines written in ANSI C and
organized in the form of a callable library.

GLPK supports the GNU MathProg language, which is a subset of the AMPL
language.

The GLPK package includes the following main components:

 * Revised simplex method.
 * Primal-dual interior point method.
 * Branch-and-bound method.
 * Translator for GNU MathProg.
 * Application program interface (API).
 * Stand-alone LP/MIP solver. 

%package        doc
# The content is GFDL-1.3-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Latin Modern: LPPL-1.3a
# XY: GPL-1.0-or-later
License:        GFDL-1.3-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND LPPL-1.3a
Summary:        Documentation for %{name}

%description    doc
Documentation subpackage for %{name}.

%package devel
Summary:        Development headers and files for GLPK
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
The glpk-devel package contains libraries and headers for developing
applications which use GLPK (GNU Linear Programming Kit).

%package utils
Summary:        GLPK-related utilities and examples
Requires:       %{name}%{_isa} = %{version}-%{release}

%description utils
The glpk-utils package contains the standalone solver program glpsol that uses
GLPK (GNU Linear Programming Kit).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Verify the source file
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

%conf
# Unbundle zlib and suitesparse
rm -fr src/{amd,colamd,zlib}

%build
export CPPFLAGS="$(pkg-config --cflags libmariadb)"
export LIBS=-ldl

# Need to rebuild src/Makefile.in from src/Makefile.am
autoreconf -ifs

%configure --disable-static --with-gmp \
           --enable-dl=dlfcn --enable-odbc --enable-mysql
# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
 sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
     -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
     -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
     -i libtool
%make_build

%install
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} libdir=$RPM_BUILD_ROOT%{_libdir} \
	includedir=$RPM_BUILD_ROOT%{_includedir}

%check
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$RPM_BUILD_ROOT%{_libdir}"
make check
## Clean up directories that are included in docs
rm -Rf examples/{.deps,.libs,Makefile*,glpsol,glpsol.o} doc/*.tex

%files
%doc README
%license COPYING
%{_libdir}/libglpk.so.40{,.*}

%files devel
%doc ChangeLog AUTHORS NEWS
%{_includedir}/glpk.h
%{_libdir}/libglpk.so

%files utils
%{_bindir}/glpsol

%files doc
%doc doc examples

%changelog
%autochangelog
